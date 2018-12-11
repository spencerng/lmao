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
        self.scanItemBtn.setGeometry(QtCore.QRect(570, 50, 201, 61))
        self.scanItemBtn.setObjectName("scanItemBtn")
        self.otherItemLightBtn = QtWidgets.QPushButton(self.centralWidget)
        self.otherItemLightBtn.setGeometry(QtCore.QRect(570, 140, 201, 51))
        self.otherItemLightBtn.setObjectName("otherItemLightBtn")
        self.otherItemDarkBtn = QtWidgets.QPushButton(self.centralWidget)
        self.otherItemDarkBtn.setGeometry(QtCore.QRect(570, 220, 201, 51))
        self.otherItemDarkBtn.setObjectName("otherItemDarkBtn")
        self.homeBtn = QtWidgets.QGraphicsView(self.centralWidget)
        self.homeBtn.setGeometry(QtCore.QRect(610, 310, 121, 111))
        self.homeBtn.setObjectName("homeBtn")
        ScanMenu.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(ScanMenu)
        self.mainToolBar.setObjectName("mainToolBar")
        ScanMenu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(ScanMenu)
        self.statusBar.setObjectName("statusBar")
        ScanMenu.setStatusBar(self.statusBar)

        self.retranslateUi(ScanMenu)
        QtCore.QMetaObject.connectSlotsByName(ScanMenu)

    def retranslateUi(self, ScanMenu):
        _translate = QtCore.QCoreApplication.translate
        ScanMenu.setWindowTitle(_translate("ScanMenu", "Laundry Manager and Optimizer"))
        self.scanItemBtn.setText(_translate("ScanMenu", "Scan Item"))
        self.otherItemLightBtn.setText(_translate("ScanMenu", "Other Item - Light"))
        self.otherItemDarkBtn.setText(_translate("ScanMenu", "Other Item - Dark"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScanMenu = QtWidgets.QMainWindow()
    ui = Ui_ScanMenu()
    ui.setupUi(ScanMenu)
    ScanMenu.show()
    sys.exit(app.exec_())

