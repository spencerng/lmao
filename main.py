import os
from os import sys

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QThread
from PyQt5.QtGui import QPixmap, QImage

import io
import time
import cv2
import numpy as np

import mainmenu
import scanmenu
import confirmmenu

PICAM_INSTALLED = True

try:
	import picamera
except ModuleNotFoundError as e:
	PICAM_INSTALLED = False



class MainWindow(QMainWindow, mainmenu.Ui_MainMenu):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		self.stackedWidget = QStackedWidget()
		self.stackedWidget.addWidget(self)
		self.stackedWidget.addWidget(ScanMenu(self.stackedWidget))
		self.stackedWidget.addWidget(ConfirmScreen(self.stackedWidget))
		self.stackedWidget.setCurrentIndex(0)
		self.stackedWidget.show()
		
		self.scanItemFrame.mouseReleaseEvent = self.onScanItemFrameClick
		self.settingsFrame.mouseReleaseEvent = self.onSettingsFrameClick
		self.viewEditItemFrame.mouseReleaseEvent = self.onViewEditItemFrameClick
		self.washClothesFrame.mouseReleaseEvent = self.onWashClothesFrameClick
		

	def onSettingsFrameClick(self, mouseEvent):
		print("Settings pressed")

	def onViewEditItemFrameClick(self, mouseEvent):
		print('view edit pressed')

	def onWashClothesFrameClick(self, mouseEvent):
		print('wash clothes clicked')

	def onScanItemFrameClick(self, mouseEvent):
		self.stackedWidget.setCurrentIndex(1)
		

class ScanMenu(QMainWindow, scanmenu.Ui_ScanMenu):
	def __init__(self, stackedWidget):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.stackedWidget = stackedWidget
		self.homeButton.mouseReleaseEvent = self.onHomeButtonClick
		self.scanItemBtn.mouseReleaseEvent = self.onScanItemButtonClick

		if PICAM_INSTALLED:
			#this stream code is untested!!
			self.camFeed = CameraStream(self, self.cameraFeedLabel)
			self.camFeed.currentPixmap.connect(self.setPreview)
			self.camFeed.start()

	def onScanItemButtonClick(self, mouseEvent):
		currentImage = self.cameraFeedLabel.pixmap()
		currentRecognizedSymbols = self.getLaundrySymbolsFromImage(currentImage)
		self.stackedWidget.widget(2).setLaundrySymbols(currentRecognizedSymbols)
		self.stackedWidget.setCurrentIndex(2)

	def getLaundrySymbolsFromImage(self, cvImage):
		#TODO write this
		return []

	def onHomeButtonClick(self, mouseEvent):
		self.stackedWidget.setCurrentIndex(0)

	def setPreview(self, image):
		self.cameraFeedLabel.setPixmap(QPixmap.fromImage(image))

class ConfirmScreen(QMainWindow, confirmmenu.Ui_ConfirmMenu):
	def __init__(self, stackedWidget):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.stackedWidget = stackedWidget

	def setLaundrySymbols(self, laundrySymbols):
		#TODO write this
		self.autoSetHamperSection()
		pass

	def autoSetHamperSection(self):
		#TODO write this
		pass


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