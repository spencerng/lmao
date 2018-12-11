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
        self.detectedSymbolFrame.setGeometry(QtCore.QRect(70, 60, 641, 80))
        self.detectedSymbolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detectedSymbolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detectedSymbolFrame.setObjectName("detectedSymbolFrame")
        self.symbolsDetectedLabel = QtWidgets.QLabel(self.confirmMenuWidget)
        self.symbolsDetectedLabel.setGeometry(QtCore.QRect(320, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.symbolsDetectedLabel.setFont(font)
        self.symbolsDetectedLabel.setObjectName("symbolsDetectedLabel")
        self.locationDropLabel = QtWidgets.QLabel(self.confirmMenuWidget)
        self.locationDropLabel.setGeometry(QtCore.QRect(170, 170, 431, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.locationDropLabel.setFont(font)
        self.locationDropLabel.setObjectName("locationDropLabel")
        self.hamperSectionsView = QtWidgets.QGraphicsView(self.confirmMenuWidget)
        self.hamperSectionsView.setGeometry(QtCore.QRect(200, 210, 371, 181))
        self.hamperSectionsView.setObjectName("hamperSectionsView")
        self.confirmScanBtn = QtWidgets.QPushButton(self.confirmMenuWidget)
        self.confirmScanBtn.setGeometry(QtCore.QRect(270, 430, 75, 23))
        self.confirmScanBtn.setObjectName("confirmScanBtn")
        self.retryScanBtn = QtWidgets.QPushButton(self.confirmMenuWidget)
        self.retryScanBtn.setGeometry(QtCore.QRect(400, 430, 75, 23))
        self.retryScanBtn.setObjectName("retryScanBtn")
        ConfirmMenu.setCentralWidget(self.confirmMenuWidget)
        self.mainToolBar = QtWidgets.QToolBar(ConfirmMenu)
        self.mainToolBar.setObjectName("mainToolBar")
        ConfirmMenu.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(ConfirmMenu)
        self.statusBar.setObjectName("statusBar")
        ConfirmMenu.setStatusBar(self.statusBar)

        self.retranslateUi(ConfirmMenu)
        QtCore.QMetaObject.connectSlotsByName(ConfirmMenu)

    def retranslateUi(self, ConfirmMenu):
        _translate = QtCore.QCoreApplication.translate
        ConfirmMenu.setWindowTitle(_translate("ConfirmMenu", "Laundry Manager and Optimizer"))
        self.symbolsDetectedLabel.setText(_translate("ConfirmMenu", "Symbols Detected"))
        self.locationDropLabel.setText(_translate("ConfirmMenu", "Place clothing item in the <location> section of the hamper"))
        self.confirmScanBtn.setText(_translate("ConfirmMenu", "Confirm"))
        self.retryScanBtn.setText(_translate("ConfirmMenu", "Retry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfirmMenu = QtWidgets.QMainWindow()
    ui = Ui_ConfirmMenu()
    ui.setupUi(ConfirmMenu)
    ConfirmMenu.show()
    sys.exit(app.exec_())

