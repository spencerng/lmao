# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vieweditmenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewEditMenu(object):
    def setupUi(self, ViewEditMenu):
        ViewEditMenu.setObjectName("ViewEditMenu")
        ViewEditMenu.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewEditMenu.sizePolicy().hasHeightForWidth())
        ViewEditMenu.setSizePolicy(sizePolicy)
        ViewEditMenu.setMinimumSize(QtCore.QSize(800, 480))
        ViewEditMenu.setMaximumSize(QtCore.QSize(800, 512))
        ViewEditMenu.setBaseSize(QtCore.QSize(800, 480))
        self.centralWidget = QtWidgets.QWidget(ViewEditMenu)
        self.centralWidget.setMinimumSize(QtCore.QSize(320, 480))
        self.centralWidget.setMaximumSize(QtCore.QSize(800, 480))
        self.centralWidget.setBaseSize(QtCore.QSize(320, 480))
        self.centralWidget.setObjectName("centralWidget")
        self.homeButton = QtWidgets.QLabel(self.centralWidget)
        self.homeButton.setGeometry(QtCore.QRect(680, 370, 111, 111))
        self.homeButton.setText("")
        self.homeButton.setPixmap(QtGui.QPixmap("img/icon_home.png"))
        self.homeButton.setScaledContents(True)
        self.homeButton.setObjectName("homeButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 461))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.blTab = QtWidgets.QWidget()
        self.blTab.setObjectName("blTab")
        self.scrollAreaBl = QtWidgets.QScrollArea(self.blTab)
        self.scrollAreaBl.setGeometry(QtCore.QRect(0, 0, 801, 431))
        self.scrollAreaBl.setWidgetResizable(True)
        self.scrollAreaBl.setObjectName("scrollAreaBl")
        self.scrollBlContents = QtWidgets.QWidget()
        self.scrollBlContents.setGeometry(QtCore.QRect(0, 0, 799, 429))
        self.scrollBlContents.setObjectName("scrollBlContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollBlContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 791, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.scrollBlLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.scrollBlLayout.setContentsMargins(11, 11, 11, 11)
        self.scrollBlLayout.setSpacing(6)
        self.scrollBlLayout.setObjectName("scrollBlLayout")
        self.scrollAreaBl.setWidget(self.scrollBlContents)
        self.tabWidget.addTab(self.blTab, "")
        self.brTab = QtWidgets.QWidget()
        self.brTab.setObjectName("brTab")
        self.scrollAreaBr = QtWidgets.QScrollArea(self.brTab)
        self.scrollAreaBr.setGeometry(QtCore.QRect(-1, 0, 801, 431))
        self.scrollAreaBr.setWidgetResizable(True)
        self.scrollAreaBr.setObjectName("scrollAreaBr")
        self.scrollBrContents = QtWidgets.QWidget()
        self.scrollBrContents.setGeometry(QtCore.QRect(0, 0, 799, 429))
        self.scrollBrContents.setObjectName("scrollBrContents")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollBrContents)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 791, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.scrollBrLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.scrollBrLayout.setContentsMargins(11, 11, 11, 11)
        self.scrollBrLayout.setSpacing(6)
        self.scrollBrLayout.setObjectName("scrollBrLayout")
        self.scrollAreaBr.setWidget(self.scrollBrContents)
        self.tabWidget.addTab(self.brTab, "")
        self.tlTab = QtWidgets.QWidget()
        self.tlTab.setObjectName("tlTab")
        self.scrollAreaTl = QtWidgets.QScrollArea(self.tlTab)
        self.scrollAreaTl.setGeometry(QtCore.QRect(-1, -1, 801, 431))
        self.scrollAreaTl.setWidgetResizable(True)
        self.scrollAreaTl.setObjectName("scrollAreaTl")
        self.scrollTlContents = QtWidgets.QWidget()
        self.scrollTlContents.setGeometry(QtCore.QRect(0, 0, 799, 429))
        self.scrollTlContents.setObjectName("scrollTlContents")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.scrollTlContents)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 801, 451))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.scrollTlLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.scrollTlLayout.setContentsMargins(11, 11, 11, 11)
        self.scrollTlLayout.setSpacing(6)
        self.scrollTlLayout.setObjectName("scrollTlLayout")
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.scrollAreaTl.setWidget(self.scrollTlContents)
        self.tabWidget.addTab(self.tlTab, "")
        self.trTab = QtWidgets.QWidget()
        self.trTab.setObjectName("trTab")
        self.scrollAreaTr = QtWidgets.QScrollArea(self.trTab)
        self.scrollAreaTr.setGeometry(QtCore.QRect(-1, -1, 801, 431))
        self.scrollAreaTr.setWidgetResizable(True)
        self.scrollAreaTr.setObjectName("scrollAreaTr")
        self.scrollTrContents = QtWidgets.QWidget()
        self.scrollTrContents.setGeometry(QtCore.QRect(0, 0, 799, 429))
        self.scrollTrContents.setObjectName("scrollTrContents")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.scrollTrContents)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(-1, -1, 801, 451))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.scrollTrLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.scrollTrLayout.setContentsMargins(11, 11, 11, 11)
        self.scrollTrLayout.setSpacing(6)
        self.scrollTrLayout.setObjectName("scrollTrLayout")
        self.scrollAreaTr.setWidget(self.scrollTrContents)
        self.tabWidget.addTab(self.trTab, "")
        self.tabWidget.raise_()
        self.homeButton.raise_()
        ViewEditMenu.setCentralWidget(self.centralWidget)

        self.retranslateUi(ViewEditMenu)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(ViewEditMenu)

    def retranslateUi(self, ViewEditMenu):
        _translate = QtCore.QCoreApplication.translate
        ViewEditMenu.setWindowTitle(_translate("ViewEditMenu", "Laundry Manager and Optimizer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.blTab), _translate("ViewEditMenu", "Bottom-Left Section"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.brTab), _translate("ViewEditMenu", "Bottom-Right Section"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tlTab), _translate("ViewEditMenu", "Top-Left Section"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trTab), _translate("ViewEditMenu", "Top-Right Section"))

