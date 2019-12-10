# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Options_Menu(object):
    def setupUi(self, Options_Menu):
        Options_Menu.setObjectName("Options_Menu")
        Options_Menu.resize(490, 400)
        self.label = QtWidgets.QLabel(Options_Menu)
        self.label.setGeometry(QtCore.QRect(150, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Options_Menu)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 241, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 201, 101))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 111, 19))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 70, 111, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 221, 151))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 30, 81, 111))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 30, 61, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 60, 51, 19))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(100, 30, 111, 111))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 30, 61, 19))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.pushButton = QtWidgets.QPushButton(Options_Menu)
        self.pushButton.setGeometry(QtCore.QRect(260, 300, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Options_Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 350, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.board_preview = QtWidgets.QLabel(Options_Menu)
        self.board_preview.setGeometry(QtCore.QRect(260, 70, 221, 221))
        self.board_preview.setText("")
        self.board_preview.setPixmap(QtGui.QPixmap("../resources/external-content.duckduckgo.png"))
        self.board_preview.setScaledContents(True)
        self.board_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.board_preview.setObjectName("board_preview")

        self.retranslateUi(Options_Menu)
        QtCore.QMetaObject.connectSlotsByName(Options_Menu)

    def retranslateUi(self, Options_Menu):
        _translate = QtCore.QCoreApplication.translate
        Options_Menu.setWindowTitle(_translate("Options_Menu", "Form"))
        self.label.setText(_translate("Options_Menu", "Options Menu"))
        self.groupBox_2.setTitle(_translate("Options_Menu", "Appearance"))
        self.groupBox.setTitle(_translate("Options_Menu", "Piece Graphics"))
        self.radioButton.setText(_translate("Options_Menu", "Chess Style"))
        self.radioButton_2.setText(_translate("Options_Menu", "Shogi Style"))
        self.groupBox_3.setTitle(_translate("Options_Menu", "Coordinates"))
        self.groupBox_4.setTitle(_translate("Options_Menu", "Horizontal"))
        self.radioButton_3.setText(_translate("Options_Menu", "1 - 9"))
        self.radioButton_4.setText(_translate("Options_Menu", "a - i"))
        self.groupBox_5.setTitle(_translate("Options_Menu", "Vertical"))
        self.radioButton_6.setText(_translate("Options_Menu", "一  -   九"))
        self.radioButton_5.setText(_translate("Options_Menu", "1 - 9"))
        self.pushButton.setText(_translate("Options_Menu", "Gameplay Presets..."))
        self.pushButton_2.setText(_translate("Options_Menu", "Go Back"))
