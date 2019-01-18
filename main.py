import os
from os import sys

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread, QPoint
from PyQt5.QtGui import QPixmap, QImage
from enum import Enum

import io
import time
import cv2
import numpy as np
import rpi_backlight as backlight

import mainmenu
import scanmenu
import confirmmenu
import settingsmenu

PI_ACTIVE = True

try:
	import picamera
except ModuleNotFoundError as e:
	PI_ACTIVE = False

UI_INDEX={'MAIN_MENU': 0,'SCAN_MENU': 1,'CONFIRM_SCREEN': 2,
	'SETTINGS_MENU': 3,'WASH_ITEMS_MENU': 4,'VIEW_EDIT_MENU': 5}

class LaundrySymbols(Enum):
	OTHER_DARK = 0
	OTHER_LIGHT = 1
	BLEACH_NO = 2
	BLEACH_NOCL = 3
	TUMBLEDRY_H = 4
	TUMBLEDRY_L = 5
	IRON_H = 6
	IRON_L = 7
	IRON_M = 8
	TUMBLEDRY_OK = 9
	WASH_30 = 10
	WASH_40 = 11
	WASH_50 = 12


class MainWindow(QMainWindow, mainmenu.Ui_MainMenu):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		self.stackedWidget = QStackedWidget()
		self.stackedWidget.addWidget(self)
		self.stackedWidget.addWidget(ScanMenu(self.stackedWidget))
		self.stackedWidget.addWidget(ConfirmScreen(self.stackedWidget))
		self.stackedWidget.addWidget(SettingsMenu(self.stackedWidget))
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

	def onWashClothesFrameClick(self, mouseEvent):
		print('wash clothes clicked')

	def onScanItemFrameClick(self, mouseEvent):
		self.stackedWidget.setCurrentIndex(UI_INDEX['SCAN_MENU'])

class SettingsMenu(QMainWindow, settingsmenu.Ui_SettingsMenu):
	def __init__(self, stackedWidget):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.stackedWidget = stackedWidget
		self.homeButton.mouseReleaseEvent = self.onHomeButtonClick
		self.brightnessSlider.mouseReleaseEvent = self.onBrightnessSliderChange
		if PI_ACTIVE:
			self.brightnessSlider.setValue(backlight.get_actual_brightness())

	def onBrightnessSliderChange(self, mouseEvent):
		brightness = int(100*self.brightnessSlider.value() / 255)
		self.brightnessLvlLabel.setText('Current level: ' + str(brightness))
		if PI_ACTIVE:
			backlight.set_brightness(self.brightnessSlider.value(), smooth=True, duration=1.5)

	def onHomeButtonClick(self, mouseEvent):
		self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])


class ScanMenu(QMainWindow, scanmenu.Ui_ScanMenu):
	def __init__(self, stackedWidget):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.stackedWidget = stackedWidget
		self.homeButton.mouseReleaseEvent = self.onHomeButtonClick
		self.scanItemBtn.mouseReleaseEvent = self.onScanItemButtonClick
		self.otherItemLightBtn.mouseReleaseEvent = self.onOtherItemLightButtonClick
		self.otherItemDarkBtn.mouseReleaseEvent = self.onOtherItemDarkButtonClick

		if PI_ACTIVE:
			#this stream code is untested!!
			self.camFeed = CameraStream(self, self.cameraFeedLabel)
			self.camFeed.currentPixmap.connect(self.setPreview)
			self.camFeed.start()

	def onOtherItemDarkButtonClick(self, mouseEvent):
		self.switchToConfirmScreen([LaundrySymbols.OTHER_DARK])

	def onOtherItemLightButtonClick(self, mouseEvent):
		self.switchToConfirmScreen([LaundrySymbols.OTHER_LIGHT])

	def onScanItemButtonClick(self, mouseEvent):
		currentImage = self.cameraFeedLabel.pixmap()
		currentRecognizedSymbols = self.getLaundrySymbolsFromImage(currentImage)
		self.switchToConfirmScreen(currentRecognizedSymbols)

	def switchToConfirmScreen(self, laundrySymbols):
		self.stackedWidget.widget(2).setLaundrySymbols(laundrySymbols)
		self.stackedWidget.setCurrentIndex(UI_INDEX['CONFIRM_SCREEN'])

	def getLaundrySymbolsFromImage(self, cvImage):
		#TODO write this
		symbols = []
		for i in range(2):
			symbols.append(LaundrySymbols.WASH_30)
		return symbols

	def onHomeButtonClick(self, mouseEvent):
		self.stackedWidget.setCurrentIndex(UI_INDEX['MAIN_MENU'])

	def setPreview(self, image):
		self.cameraFeedLabel.setPixmap(QPixmap.fromImage(image))



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
		#TODO write this
		self.laundrySymbols = laundrySymbols
		if len(laundrySymbols) == 0:
			return
		if laundrySymbols[0] == LaundrySymbols.OTHER_LIGHT:
			self.itemDetectedLabel.setText('Other item - light')

		elif laundrySymbols[0] == LaundrySymbols.OTHER_DARK:
			self.itemDetectedLabel.setText('Other item - dark')

		else:
			for i in range(len(laundrySymbols)):
				symbolHolder = QLabel(self.detectedSymbolFrame)

				totalWidth = 100 * len(laundrySymbols) - 20 * (len(laundrySymbols) - 1)

				symbolHolder.move(QPoint(-totalWidth/2+100*i-5*(len(laundrySymbols)-1), -40) + self.detectedSymbolFrame.rect().center())
				
				symbolHolder.setFixedWidth(100)			
				symbolGraphic = QPixmap('./img/wash_30c.png')
				symbolHolder.setPixmap(symbolGraphic.scaled(100,80,Qt.KeepAspectRatio))

		self.autoSetHamperSection()

	def autoSetHamperSection(self):
		#TODO finish writing this
		#based on algorithm, set images
		sectionGraphic = QPixmap('./img/place_tr.png')

		self.hamperSectionView.setPixmap(sectionGraphic)


class CameraStream(QThread):
	currentPixmap = pyqtSignal(QImage)

	def __init__(self, parent, previewLabel):
		super(self.__class__, self).__init__()
		self.previewLabel = previewLabel

	def run(self):
		stream = io.BytesIO()
		with picamera.PiCamera() as camera:
		    camera.start_preview()
		    time.sleep(2)
		    camera.capture(stream, format='jpeg')
		
		while True:
			time.sleep(1000/30.0)
			data = np.fromstring(stream.getvalue(), dtype=np.uint8)
			# "Decode" the image from the array, preserving colour
			image = cv2.imdecode(data, 1)
			# OpenCV returns an array with data in BGR order. If you want RGB instead
			# use the following...
			image = image[:, :, ::-1]

			qtImage = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)

			scaledImage = qtImage.scaled(self.previewLabel.size(), Qt.KeepAspectRatio)
			self.currentPixmap.emit(scaledImage)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	
	sys.exit(app.exec_())