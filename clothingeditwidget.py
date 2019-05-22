# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clothingeditwidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_articleDisplayWidget(object):
    def setupUi(self, articleDisplayWidget):
        articleDisplayWidget.setObjectName("articleDisplayWidget")
        articleDisplayWidget.resize(781, 100)
        articleDisplayWidget.setMinimumSize(QtCore.QSize(320, 100))
        articleDisplayWidget.setMaximumSize(QtCore.QSize(800, 100))
        articleDisplayWidget.setBaseSize(QtCore.QSize(320, 480))
        self.deleteButton = QtWidgets.QPushButton(articleDisplayWidget)
        self.deleteButton.setGeometry(QtCore.QRect(620, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.bleachLabel = QtWidgets.QLabel(articleDisplayWidget)
        self.bleachLabel.setGeometry(QtCore.QRect(240, 20, 71, 61))
        self.bleachLabel.setText("")
        self.bleachLabel.setPixmap(QtGui.QPixmap("img/bleach_no.png"))
        self.bleachLabel.setScaledContents(True)
        self.bleachLabel.setObjectName("bleachLabel")
        self.itemNumLabel = QtWidgets.QLabel(articleDisplayWidget)
        self.itemNumLabel.setGeometry(QtCore.QRect(20, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.itemNumLabel.setFont(font)
        self.itemNumLabel.setObjectName("itemNumLabel")
        self.washLabel = QtWidgets.QLabel(articleDisplayWidget)
        self.washLabel.setGeometry(QtCore.QRect(140, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.washLabel.setFont(font)
        self.washLabel.setText("")
        self.washLabel.setPixmap(QtGui.QPixmap("img/wash_30c.png"))
        self.washLabel.setScaledContents(True)
        self.washLabel.setWordWrap(True)
        self.washLabel.setObjectName("washLabel")
        self.ironLabel = QtWidgets.QLabel(articleDisplayWidget)
        self.ironLabel.setGeometry(QtCore.QRect(340, 20, 71, 61))
        self.ironLabel.setText("")
        self.ironLabel.setPixmap(QtGui.QPixmap("img/iron_low.png"))
        self.ironLabel.setScaledContents(True)
        self.ironLabel.setObjectName("ironLabel")
        self.dryLabel = QtWidgets.QLabel(articleDisplayWidget)
        self.dryLabel.setGeometry(QtCore.QRect(440, 15, 71, 71))
        self.dryLabel.setText("")
        self.dryLabel.setPixmap(QtGui.QPixmap("img/tumbledry_low.png"))
        self.dryLabel.setScaledContents(True)
        self.dryLabel.setObjectName("dryLabel")

        self.retranslateUi(articleDisplayWidget)
        QtCore.QMetaObject.connectSlotsByName(articleDisplayWidget)

    def retranslateUi(self, articleDisplayWidget):
        _translate = QtCore.QCoreApplication.translate
        self.deleteButton.setText(_translate("articleDisplayWidget", "Delete Item"))
        self.itemNumLabel.setText(_translate("articleDisplayWidget", "Item #1"))

