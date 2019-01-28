# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScanMenu(object):
    def setupUi(self, ScanMenu):
        ScanMenu.setObjectName("ScanMenu")
        ScanMenu.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScanMenu.sizePolicy().hasHeightForWidth())
        ScanMenu.setSizePolicy(sizePolicy)
        ScanMenu.setMinimumSize(QtCore.QSize(800, 480))
        ScanMenu.setMaximumSize(QtCore.QSize(800, 512))
        ScanMenu.setBaseSize(QtCore.QSize(800, 480))
        self.centralWidget = QtWidgets.QWidget(ScanMenu)
        self.centralWidget.setMinimumSize(QtCore.QSize(320, 480))
        self.centralWidget.setMaximumSize(QtCore.QSize(800, 480))
        self.centralWidget.setBaseSize(QtCore.QSize(320, 480))
        self.centralWidget.setObjectName("centralWidget")
        self.scanItemBtn = QtWidgets.QPushButton(self.centralWidget)
        self.scanItemBtn.setGeometry(QtCore.QRect(570, 38, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.scanItemBtn.setFont(font)
        self.scanItemBtn.setObjectName("scanItemBtn")
        self.otherItemLightBtn = QtWidgets.QPushButton(self.centralWidget)
        self.otherItemLightBtn.setGeometry(QtCore.QRect(570, 128, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.otherItemLightBtn.setFont(font)
        self.otherItemLightBtn.setObjectName("otherItemLightBtn")
        self.otherItemDarkBtn = QtWidgets.QPushButton(self.centralWidget)
        self.otherItemDarkBtn.setGeometry(QtCore.QRect(570, 208, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.otherItemDarkBtn.setFont(font)
        self.otherItemDarkBtn.setObjectName("otherItemDarkBtn")
        self.homeButton = QtWidgets.QLabel(self.centralWidget)
        self.homeButton.setGeometry(QtCore.QRect(600, 320, 131, 131))
        self.homeButton.setText("")
        self.homeButton.setPixmap(QtGui.QPixmap("img/icon_home.png"))
        self.homeButton.setScaledContents(True)
        self.homeButton.setObjectName("homeButton")
        self.cameraFeedLabel = QtWidgets.QLabel(self.centralWidget)
        self.cameraFeedLabel.setGeometry(QtCore.QRect(30, 30, 521, 411))
        self.cameraFeedLabel.setText("")
        self.cameraFeedLabel.setObjectName("cameraFeedLabel")
        self.cheese30 = QtWidgets.QFrame(self.centralWidget)
        self.cheese30.setGeometry(QtCore.QRect(570, 30, 101, 81))
        self.cheese30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cheese30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cheese30.setObjectName("cheese30")
        self.cheese40 = QtWidgets.QFrame(self.centralWidget)
        self.cheese40.setGeometry(QtCore.QRect(670, 30, 120, 71))
        self.cheese40.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cheese40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cheese40.setObjectName("cheese40")
        ScanMenu.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(ScanMenu)
        self.mainToolBar.setEnabled(False)
        self.mainToolBar.setMaximumSize(QtCore.QSize(0, 0))
        self.mainToolBar.setObjectName("mainToolBar")
        ScanMenu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(ScanMenu)
        QtCore.QMetaObject.connectSlotsByName(ScanMenu)

    def retranslateUi(self, ScanMenu):
        _translate = QtCore.QCoreApplication.translate
        ScanMenu.setWindowTitle(_translate("ScanMenu", "Laundry Manager and Optimizer"))
        self.scanItemBtn.setText(_translate("ScanMenu", "Scan Tag"))
        self.otherItemLightBtn.setText(_translate("ScanMenu", "Other Item - Light"))
        self.otherItemDarkBtn.setText(_translate("ScanMenu", "Other Item - Dark"))

