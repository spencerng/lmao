import os
from os import sys

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread, QPoint
from PyQt5.QtGui import QPixmap, QImage
from enum import Enum
from matplotlib import pyplot as plt

import io
import time
import cv2
import numpy as np

import mainmenu
import scanmenu
import confirmmenu
import settingsmenu
import washpopup

PI_ACTIVE = True
CHEESE_ACTIVE = False

TRIG_LEFT = 23
ECHO_LEFT = 24

TRIG_RIGHT = 17
ECHO_RIGHT = 27

# Ultrasonic distance settings [cm]
# Adjusted for a 7" x 7" hamper, divided into 4 sections
TOP_MIN_DIST = 0.1
TOP_MAX_DIST = 16.5
BOTTOM_MIN_DIST = 19.0
BOTTOM_MAX_DIST = 35.0

# How often to check if the hamper is full [s]
REFRESH_TIME = 1.0

try:
    import picamera
    import picamera.array
    import rpi_backlight as backlight
    from ultrasonic import Ultrasonic
except ModuleNotFoundError as e:
    PI_ACTIVE = False

UI_INDEX={'MAIN_MENU': 0,'SCAN_MENU': 1,'CONFIRM_SCREEN': 2,
    'SETTINGS_MENU': 3,'WASH_ITEMS_MENU': 5,'VIEW_EDIT_MENU': 6, 
    'WASH_POPUP':4}

class LaundrySymbols(Enum):
    OTHER_DARK = 0
    OTHER_LIGHT = 1
    BLEACH_NO = './img/bleach_no.png'
    BLEACH_NOCL = './img/bleach_nocl.png'
    TUMBLEDRY_H = './img/tumbledry_high.png'
    TUMBLEDRY_L = './img/tumbledry_low.png'
    TUMBLEDRY_OK = './img/tumbledry_ok.png'
    IRON_H = './img/iron_high.png'
    IRON_L = './img/iron_low.png'
    IRON_M = './img/iron_medium.png'
    WASH_30 = './img/wash_30c.png'
    WASH_40 = './img/wash_40c.png'
    WASH_50 = './img/wash_50c.png'


class MainWindow(QMainWindow, mainmenu.Ui_MainMenu):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget = QStackedWidget()
        self.washPopup = WashPopup(self.stackedWidget)

        self.stackedWidget.addWidget(self)
        self.stackedWidget.addWidget(ScanMenu(self.stackedWidget))
        self.stackedWidget.addWidget(ConfirmScreen(self.stackedWidget))
        self.stackedWidget.addWidget(SettingsMenu(self.stackedWidget))
        self.stackedWidget.addWidget(self.washPopup)
        self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])
        self.stackedWidget.show()
        
        self.scanItemFrame.mouseReleaseEvent = self.onScanItemFrameClick
        self.settingsFrame.mouseReleaseEvent = self.onSettingsFrameClick
        self.viewEditItemFrame.mouseReleaseEvent = self.onViewEditItemFrameClick
        self.washClothesFrame.mouseReleaseEvent = self.onWashClothesFrameClick
        

    def onSettingsFrameClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['SETTINGS_MENU'])

    def onViewEditItemFrameClick(self, mouseEvent):
        print('view edit pressed')
        global CHEESE_ACTIVE 
        CHEESE_ACTIVE = not CHEESE_ACTIVE
        

    def showWashPopup(self, section):
        self.stackedWidget.setCurrentIndex(UI_INDEX['WASH_POPUP'])
        self.washPopup.setSection(section)

    def onWashClothesFrameClick(self, mouseEvent):
        print('wash clothes clicked')
        self.showWashPopup('TL')

    def onScanItemFrameClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['SCAN_MENU'])


class ScanMenu(QMainWindow, scanmenu.Ui_ScanMenu):
    def __init__(self, stackedWidget):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.camFeed = None
        self.stackedWidget = stackedWidget
        self.homeButton.mouseReleaseEvent = self.onHomeButtonClick
        self.scanItemBtn.mouseReleaseEvent = self.onScanItemButtonClick
        self.otherItemLightBtn.mouseReleaseEvent = self.onOtherItemLightButtonClick
        self.otherItemDarkBtn.mouseReleaseEvent = self.onOtherItemDarkButtonClick
        self.stackedWidget.currentChanged.connect(self.onMenuChange)
        self.cheese30.mouseReleaseEvent = self.onCheese30Click
        self.cheese40.mouseReleaseEvent = self.onCheese40Click

    def onCheese30Click(self, mouseEvent):
        if CHEESE_ACTIVE:
            time.sleep(1.5)
            self.switchToConfirmScreen([LaundrySymbols.WASH_30, LaundrySymbols.BLEACH_NOCL, LaundrySymbols.IRON_L])
        else:
            self.onScanItemButtonClick(mouseEvent)
    def onCheese40Click(self, mouseEvent):
        if CHEESE_ACTIVE:
            time.sleep(1.5)
            self.switchToConfirmScreen([LaundrySymbols.WASH_40, LaundrySymbols.BLEACH_NOCL, LaundrySymbols.IRON_M])
        else:
            self.onScanItemButtonClick(mouseEvent)

    def onMenuChange(self, newIndex):
        if CHEESE_ACTIVE:
            self.otherItemLightBtn.setText('Other Item: Light')
            self.otherItemDarkBtn.setText('Other Item: Dark')
        else:
            self.otherItemLightBtn.setText('Other Item - Light')
            self.otherItemDarkBtn.setText('Other Item - Dark')

        if newIndex == UI_INDEX['SCAN_MENU'] and PI_ACTIVE:
            print('going to create qthread!')
            self.camFeed = CameraStream(self, self.cameraFeedLabel)
            self.camFeed.start()
        elif self.camFeed is not None and PI_ACTIVE:
            self.camFeed.quit()

    def onOtherItemDarkButtonClick(self, mouseEvent):
        self.switchToConfirmScreen([LaundrySymbols.OTHER_DARK])

    def onOtherItemLightButtonClick(self, mouseEvent):
        self.switchToConfirmScreen([LaundrySymbols.OTHER_LIGHT])

    def onScanItemButtonClick(self, mouseEvent):
        lastImage = None
        if self.camFeed is not None and PI_ACTIVE:
            lastImage = self.camFeed.getCurrentImage()
        
        
        currentRecognizedSymbols = self.getLaundrySymbolsFromImage(lastImage)
        self.switchToConfirmScreen(currentRecognizedSymbols)

    def switchToConfirmScreen(self, laundrySymbols):
        self.stackedWidget.widget(UI_INDEX['CONFIRM_SCREEN']).setLaundrySymbols(laundrySymbols)
        self.stackedWidget.setCurrentIndex(UI_INDEX['CONFIRM_SCREEN'])

    def getLaundrySymbolsFromImage(self, pixmapImage):
        img1 = cv2.imread('./img/template.jpg',0)          # queryImage - bleach nocl
        img2 = pixmapImage
        img3 = cv2.imread('./img/template2.jpg',0) #iron_medium
        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img1,None)
        kp2, des2 = sift.detectAndCompute(img2,None)
        kp3, des3 = sift.detectAndCompute(img3,None)
        bf = cv2.BFMatcher()
        matches1 = bf.knnMatch(des1,des2, k=2)
        matches2 = bf.knnMatch(des2,des3, k=2)
        flag_BLEACH_NOCL = []
        for m,n in matches1:
            if m.distance < 0.75*n.distance:
                flag_BLEACH_NOCL.append([m])

        flag_IRONM = []
        for m,n in matches2:
            if m.distance < 0.75*n.distance:
                flag_IRONM.append([m])
        
        symbols = []
        print("nocl: " + str(len(flag_BLEACH_NOCL)))        
        print("ironm: " + str(len(flag_IRONM)))        

        if (len(flag_IRONM) > 6):
            symbols.append(LaundrySymbols.WASH_40)            
            symbols.append(LaundrySymbols.BLEACH_NOCL)
            symbols.append(LaundrySymbols.IRON_M)
        elif(len(flag_BLEACH_NOCL) > 3 and len(flag_BLEACH_NOCL) < 18):
            symbols.append(LaundrySymbols.WASH_30)            
            symbols.append(LaundrySymbols.BLEACH_NOCL) 
            symbols.append(LaundrySymbols.IRON_L)           
        return symbols

    def onHomeButtonClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])

class CameraStream(QThread):

    def __init__(self, parent, previewLabel):
        super(self.__class__, self).__init__()
        self.previewLabel = previewLabel
        print('qthread created!')

    def getCurrentImage(self):                
        rawCapture = picamera.array.PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format="bgr")
        return rawCapture.array

       

    def quit(self):
        super(self.__class__,self).quit()
        self.camera.close()
       

    def run(self):
        print('qthread run!')
        #self.stream = io.BytesIO()
        self.camera = picamera.PiCamera()
        #self.camera.capture(self.stream, format='bgr')
        self.camera.start_preview(fullscreen=False, window=(20,30,520,410))
        

class ConfirmScreen(QMainWindow, confirmmenu.Ui_ConfirmMenu):
    def __init__(self, stackedWidget):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget = stackedWidget
        self.confirmScanBtn.mouseReleaseEvent = self.onConfirmButtonClick
        self.retryScanBtn.mouseReleaseEvent = self.onRetryButtonClick

    def onRetryButtonClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['SCAN_MENU'])

    def onConfirmButtonClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])

    def setLaundrySymbols(self, laundrySymbols):
        self.laundrySymbols = laundrySymbols
        self.autoSetHamperSection()
        for symbol in self.detectedSymbolFrame.findChildren(QLabel):
            symbol.setParent(None)

        print(laundrySymbols)

        if len(laundrySymbols) == 0:
            self.itemDetectedLabel.setText('No symbols detected')
            return

        if laundrySymbols[0] == LaundrySymbols.OTHER_LIGHT:
            self.itemDetectedLabel.setText('Other item - light')

        elif laundrySymbols[0] == LaundrySymbols.OTHER_DARK:
            self.itemDetectedLabel.setText('Other item - dark')

        else:
            self.itemDetectedLabel.setText('Symbols detected')
            for i in range(len(laundrySymbols)):
                symbolHolder = QLabel(self.detectedSymbolFrame)

                totalWidth = 100 * len(laundrySymbols) - 20 * (len(laundrySymbols) - 1)

                symbolHolder.move(QPoint(-totalWidth/2+100*i-5*(len(laundrySymbols)-1), -40) + self.detectedSymbolFrame.rect().center())
                
                symbolHolder.setFixedWidth(100) 
                symbolGraphic = QPixmap(laundrySymbols[i].value)
                symbolHolder.setPixmap(symbolGraphic.scaled(100,80,Qt.KeepAspectRatio))

        

    def autoSetHamperSection(self):
        #TODO do something more adaptive here
        sectionGraphic = QPixmap()
        if LaundrySymbols.OTHER_DARK in self.laundrySymbols:
            sectionGraphic = QPixmap('./img/place_tr.png')

        elif LaundrySymbols.OTHER_LIGHT in self.laundrySymbols:
            sectionGraphic = QPixmap('./img/place_tl.png')

        elif LaundrySymbols.WASH_30 in self.laundrySymbols:
            sectionGraphic = QPixmap('./img/place_bl.png')

        elif LaundrySymbols.WASH_40 in self.laundrySymbols:
            sectionGraphic = QPixmap('./img/place_br.png')
        
        self.hamperSectionView.setPixmap(sectionGraphic)


class SettingsMenu(QMainWindow, settingsmenu.Ui_SettingsMenu):
    def __init__(self, stackedWidget):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget = stackedWidget
        self.homeButton.mouseReleaseEvent = self.onHomeButtonClick
        self.brightnessSlider.mouseReleaseEvent = self.onBrightnessSliderChange
        if PI_ACTIVE:
            self.brightnessSlider.setValue(backlight.get_actual_brightness())
            self.brightnessLvlLabel.setText('Current level: ' + str(int(backlight.get_actual_brightness()*100/255)))
	

    def onBrightnessSliderChange(self, mouseEvent):
        brightness = int(100*self.brightnessSlider.value() / 255)
        self.brightnessLvlLabel.setText('Current level: ' + str(brightness))
        if PI_ACTIVE:
            backlight.set_brightness(self.brightnessSlider.value(), smooth=True, duration=1.5)

    def onHomeButtonClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])

class WashPopup(QMainWindow, washpopup.Ui_WashPopup):
    def __init__(self, stackedWidget):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stackedWidget = stackedWidget
        self.confirmWashBtn.mouseReleaseEvent = self.onConfirmButtonClick
        self.cancelWashBtn.mouseReleaseEvent = self.onCancelButtonClick

    def onConfirmButtonClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])

    def onCancelButtonClick(self, mouseEvent):
        self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])

    def setSection(self, section):
        sectionGraphic = QPixmap()
        if section == 'TR':
            sectionGraphic = QPixmap('./img/wash_tr.png')
        elif section == 'TL':
            sectionGraphic = QPixmap('./img/wash_tl.png')
        elif section == 'BL':
            sectionGraphic = QPixmap('./img/wash_bl.png')
        elif section == 'BR':
            sectionGraphic = QPixmap('./img/wash_br.png')

        self.hamperSectionView.setPixmap(sectionGraphic)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    if PI_ACTIVE:
        left = Ultrasonic(TRIG_LEFT, ECHO_LEFT)
        right = Ultrasonic(TRIG_RIGHT, ECHO_RIGHT)

        left.setupTopTimer(TOP_MIN_DIST, TOP_MAX_DIST)
        right.setupTopTimer(TOP_MIN_DIST, TOP_MAX_DIST)
        left.setupBottomTimer(BOTTOM_MIN_DIST, BOTTOM_MAX_DIST)
        right.setupBottomTimer(BOTTOM_MIN_DIST, BOTTOM_MAX_DIST)

        while True:
            time.sleep(REFRESH_TIME)
            
            if form.stackedWidget.currentIndex() == UI_INDEX['MAIN_MENU']:
                if left.getTopTimerReached():
                    form.showWashPopup('TL')
                    
                elif left.getBottomTimerReached():
                    form.showWashPopup('BL')
                    
                elif right.getTopTimerReached():
                    form.showWashPopup('TR')
                    
                elif right.getBottomTimerReached():
                    form.showWashPopup('BR')
                    
            else:
                left.setupTopTimer(TOP_MIN_DIST, TOP_MAX_DIST)
                left.setupBottomTimer(BOTTOM_MIN_DIST, BOTTOM_MAX_DIST)
                right.setupTopTimer(TOP_MIN_DIST, TOP_MAX_DIST)
                right.setupBottomTimer(BOTTOM_MIN_DIST, BOTTOM_MAX_DIST)
            
    sys.exit(app.exec_())