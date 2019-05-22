# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'washmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsMenu(object):
    def setupUi(self, SettingsMenu):
        SettingsMenu.setObjectName("SettingsMenu")
        SettingsMenu.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsMenu.sizePolicy().hasHeightForWidth())
        SettingsMenu.setSizePolicy(sizePolicy)
        SettingsMenu.setMinimumSize(QtCore.QSize(800, 480))
        SettingsMenu.setMaximumSize(QtCore.QSize(800, 512))
        SettingsMenu.setBaseSize(QtCore.QSize(800, 480))
        self.centralWidget = QtWidgets.QWidget(SettingsMenu)
        self.centralWidget.setMinimumSize(QtCore.QSize(320, 480))
        self.centralWidget.setMaximumSize(QtCore.QSize(800, 480))
        self.centralWidget.setBaseSize(QtCore.QSize(320, 480))
        self.centralWidget.setObjectName("centralWidget")
        self.homeButton = QtWidgets.QLabel(self.centralWidget)
        self.homeButton.setGeometry(QtCore.QRect(660, 340, 131, 131))
        self.homeButton.setText("")
        self.homeButton.setPixmap(QtGui.QPixmap("img/icon_home.png"))
        self.homeButton.setScaledContents(True)
        self.homeButton.setObjectName("homeButton")
        self.brightnessPrompt = QtWidgets.QLabel(self.centralWidget)
        self.brightnessPrompt.setGeometry(QtCore.QRect(300, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.brightnessPrompt.setFont(font)
        self.brightnessPrompt.setAlignment(QtCore.Qt.AlignCenter)
        self.brightnessPrompt.setObjectName("brightnessPrompt")
        self.brightnessLvlLabel = QtWidgets.QLabel(self.centralWidget)
        self.brightnessLvlLabel.setGeometry(QtCore.QRect(60, 60, 641, 361))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.brightnessLvlLabel.setFont(font)
        self.brightnessLvlLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.brightnessLvlLabel.setObjectName("brightnessLvlLabel")
        SettingsMenu.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(SettingsMenu)
        self.mainToolBar.setEnabled(False)
        self.mainToolBar.setMaximumSize(QtCore.QSize(0, 0))
        self.mainToolBar.setObjectName("mainToolBar")
        SettingsMenu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(SettingsMenu)
        QtCore.QMetaObject.connectSlotsByName(SettingsMenu)

    def retranslateUi(self, SettingsMenu):
        _translate = QtCore.QCoreApplication.translate
        SettingsMenu.setWindowTitle(_translate("SettingsMenu", "Laundry Manager and Optimizer"))
        self.brightnessPrompt.setText(_translate("SettingsMenu", "Wash Instructions"))
        self.brightnessLvlLabel.setText(_translate("SettingsMenu", "1. Remove all items from the bottom-left section of the hamper\n"
"2. Set the washing machine to 30 degrees\n"
"3. Add detergent and wash. Add bleach without chlorine\n"
"4. Remove clothes and tumble dry on a LOW setting\n"
"\n"
"1. Remove all items from the bottom-right section of the hamper\n"
"2. Add the miscellaneous dark items from the top-right section\n"
"3. Set the washing machine to 40 degrees Celsius\n"
"4. Add detergent and wash. Do NOT add bleach\n"
"5. Remove clothes and tumble dry on a HIGH setting\n"
"\n"
""))

