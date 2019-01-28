# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfirmMenu(object):
    def setupUi(self, ConfirmMenu):
        ConfirmMenu.setObjectName("ConfirmMenu")
        ConfirmMenu.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfirmMenu.sizePolicy().hasHeightForWidth())
        ConfirmMenu.setSizePolicy(sizePolicy)
        ConfirmMenu.setMinimumSize(QtCore.QSize(800, 480))
        ConfirmMenu.setMaximumSize(QtCore.QSize(800, 512))
        ConfirmMenu.setBaseSize(QtCore.QSize(800, 480))
        self.confirmMenuWidget = QtWidgets.QWidget(ConfirmMenu)
        self.confirmMenuWidget.setMinimumSize(QtCore.QSize(320, 480))
        self.confirmMenuWidget.setMaximumSize(QtCore.QSize(800, 480))
        self.confirmMenuWidget.setBaseSize(QtCore.QSize(320, 480))
        self.confirmMenuWidget.setObjectName("confirmMenuWidget")
        self.detectedSymbolFrame = QtWidgets.QFrame(self.confirmMenuWidget)
        self.detectedSymbolFrame.setGeometry(QtCore.QRect(0, 60, 801, 80))
        self.detectedSymbolFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.detectedSymbolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detectedSymbolFrame.setObjectName("detectedSymbolFrame")
        self.itemDetectedLabel = QtWidgets.QLabel(self.confirmMenuWidget)
        self.itemDetectedLabel.setGeometry(QtCore.QRect(0, 10, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.itemDetectedLabel.setFont(font)
        self.itemDetectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.itemDetectedLabel.setObjectName("itemDetectedLabel")
        self.confirmScanBtn = QtWidgets.QPushButton(self.confirmMenuWidget)
        self.confirmScanBtn.setGeometry(QtCore.QRect(230, 390, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.confirmScanBtn.setFont(font)
        self.confirmScanBtn.setObjectName("confirmScanBtn")
        self.retryScanBtn = QtWidgets.QPushButton(self.confirmMenuWidget)
        self.retryScanBtn.setGeometry(QtCore.QRect(430, 390, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.retryScanBtn.setFont(font)
        self.retryScanBtn.setObjectName("retryScanBtn")
        self.hamperSectionView = QtWidgets.QLabel(self.confirmMenuWidget)
        self.hamperSectionView.setGeometry(QtCore.QRect(190, 160, 431, 201))
        self.hamperSectionView.setText("")
        self.hamperSectionView.setPixmap(QtGui.QPixmap("img/place_tl.png"))
        self.hamperSectionView.setScaledContents(True)
        self.hamperSectionView.setObjectName("hamperSectionView")
        ConfirmMenu.setCentralWidget(self.confirmMenuWidget)
        self.mainToolBar = QtWidgets.QToolBar(ConfirmMenu)
        self.mainToolBar.setMaximumSize(QtCore.QSize(0, 0))
        self.mainToolBar.setObjectName("mainToolBar")
        ConfirmMenu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(ConfirmMenu)
        QtCore.QMetaObject.connectSlotsByName(ConfirmMenu)

    def retranslateUi(self, ConfirmMenu):
        _translate = QtCore.QCoreApplication.translate
        ConfirmMenu.setWindowTitle(_translate("ConfirmMenu", "Laundry Manager and Optimizer"))
        self.itemDetectedLabel.setText(_translate("ConfirmMenu", "Symbols Detected"))
        self.confirmScanBtn.setText(_translate("ConfirmMenu", "Confirm"))
        self.retryScanBtn.setText(_translate("ConfirmMenu", "Retry"))

