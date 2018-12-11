import os
from os import sys

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap


import mainmenu

def clickable(widget):
 
	class Filter(QObject):
     
		clicked = pyqtSignal()
	 
	def eventFilter(self, obj, event):
	 
		if obj == widget:
			if event.type() == QEvent.MouseButtonRelease:
				if obj.rect().contains(event.pos()):
					self.clicked.emit()
					return True
	     
		return False
     
	filter = Filter(widget)
	widget.installEventFilter(filter)
	return filter.clicked

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainmenu.Ui_MainMenu):
	def pressedPreviewButton(self):
		print("Pressed Preview!")
		myPixmap = QPixmap()
		myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		self.lblCamView.setPixmap(myScaledPixmap)

	def pressedSnapButton(self):
		print("Pressed Snap")
		self.lblCamView.clear()

	def pressedSettingsButton(self):
		print("Settings pressed")

	def onScanItemFrameClick(self):
		print('frame clicked')


	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI file


		self.scanItemFrame.mousePressEvent = self.onScanItemFrameClick()
		scene = QGraphicsScene()
		img = QPixmap(os.getcwd() + '/img/barcode-scan.png')
		scene.addPixmap(img)
		scene.addText('Hello  world')
		self.scanItemIcon.setScene(scene)
		self.scanItemIcon.show()
		#self.scanItemFrame.connect(lambda: self.onScanItemFrameClick())





if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	
	sys.exit(app.exec_()) # need this to keep window alive
