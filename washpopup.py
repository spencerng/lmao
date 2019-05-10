# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'washpopup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WashPopup(object):
    def setupUi(self, WashPopup):
        WashPopup.setObjectName("WashPopup")
        WashPopup.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WashPopup.sizePolicy().hasHeightForWidth())
        WashPopup.setSizePolicy(sizePolicy)
        WashPopup.setMinimumSize(QtCore.QSize(800, 480))
        WashPopup.setMaximumSize(QtCore.QSize(800, 512))
        WashPopup.setBaseSize(QtCore.QSize(800, 480))
        self.washPopupWidget = QtWidgets.QWidget(WashPopup)
        self.washPopupWidget.setMinimumSize(QtCore.QSize(320, 480))
        self.washPopupWidget.setMaximumSize(QtCore.QSize(800, 480))
        self.washPopupWidget.setBaseSize(QtCore.QSize(320, 480))
        self.washPopupWidget.setObjectName("washPopupWidget")
        self.fullDetectedLabel = QtWidgets.QLabel(self.washPopupWidget)
        self.fullDetectedLabel.setGeometry(QtCore.QRect(0, 40, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.fullDetectedLabel.setFont(font)
        self.fullDetectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fullDetectedLabel.setObjectName("fullDetectedLabel")
        self.confirmWashBtn = QtWidgets.QPushButton(self.washPopupWidget)
        self.confirmWashBtn.setGeometry(QtCore.QRect(230, 380, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.confirmWashBtn.setFont(font)
        self.confirmWashBtn.setObjectName("confirmWashBtn")
        self.cancelWashBtn = QtWidgets.QPushButton(self.washPopupWidget)
        self.cancelWashBtn.setGeometry(QtCore.QRect(430, 380, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.cancelWashBtn.setFont(font)
        self.cancelWashBtn.setObjectName("cancelWashBtn")
        self.hamperSectionView = QtWidgets.QLabel(self.washPopupWidget)
        self.hamperSectionView.setGeometry(QtCore.QRect(120, 120, 561, 201))
        self.hamperSectionView.setText("")
        self.hamperSectionView.setPixmap(QtGui.QPixmap("img/wash_tl.png"))
        self.hamperSectionView.setScaledContents(True)
        self.hamperSectionView.setObjectName("hamperSectionView")
        WashPopup.setCentralWidget(self.washPopupWidget)
        self.mainToolBar = QtWidgets.QToolBar(WashPopup)
        self.mainToolBar.setMaximumSize(QtCore.QSize(0, 0))
        self.mainToolBar.setObjectName("mainToolBar")
        WashPopup.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(WashPopup)
        QtCore.QMetaObject.connectSlotsByName(WashPopup)

    def retranslateUi(self, WashPopup):
        _translate = QtCore.QCoreApplication.translate
        WashPopup.setWindowTitle(_translate("WashPopup", "Laundry Manager and Optimizer"))
        self.fullDetectedLabel.setText(_translate("WashPopup", "Hamper section detected as full!"))
        self.confirmWashBtn.setText(_translate("WashPopup", "Confirm"))
        self.cancelWashBtn.setText(_translate("WashPopup", "Cancel"))

