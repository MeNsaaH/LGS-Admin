# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class About(QDialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 583)
        Form.setStyleSheet("QComboBox, QLineEdit {\n"
                        "border-radius: 5px;\n"
                        "border: 3px solid rgb(207, 207, 207);\n"
                        "font: 15pt \"Consolas\";\n"
                        "padding: 10%;\n"
                        "}\n"
                        "\n"
                        "\n"
                        "QLineEdit:focus, QComboBox:focus, QComboBox:hover {\n"
                        "outline: 1px solid rgb(60, 185, 112);\n"
                        "background: rgb(223, 255, 208);\n"
                        "border: 2px solid rgb(67, 148, 103);\n"
                        "height: 10px;\n"
                        "}\n"
                        "\n"
                        "QLabel {\n"
                        "font-size: 16px;\n"
                        "font-family: Comic Sans Ms\n"
                        "}\n"
                        "\n"
                        "QPushButton {\n"
                        "background-color: #4CAF50;\n"
                        "selection-color: rgb(255, 255, 255);\n"
                        "border-radius: 3px;\n"
                        "border: none;\n"
                        "color: white;\n"
                        "padding: 15px 32px;\n"
                        "text-align: center;\n"
                        "text-decoration: none;\n"
                        "font: 10pt \"Comic Sans MS\";\n"
                        "padding: 0px;\n"
                        "}\n"
                        "QPushButton:hover {\n"
                        "background-color: #ffffff;\n"
                        "color: #000000;\n"
                        "border: 2px solid  #4CAF50;\n"
                        "}\n"
                        "\n"
                        "QPushButton#closeBtn {\n"
                        "image: url(:/close);\n"
                        "background: #ffffff;\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover#closeBtn {\n"
                        "border: 2px solid rgb(248, 0, 0);\n"
                        "}\n"
                        "\n"
                        "QLabel#closeBtn {\n"
                        "padding: 0px;\n"
                        "}\n"
                        "QLabel#LoginLabel, QLabel#register_label {\n"
                        "font-size: 30px;\n"
                        "color:rgb(0, 255, 59);\n"
                        "}\n"
                        "\n"
                        "QCheckBox {\n"
                        "font: 75 12pt \"Comic Sans MS\";\n"
                        "}\n"
                        "QLabel#errorLabel{\n"
                        "background: rgba(254, 0, 0, 100);\n"
                        "padding: 5px;\n"
                        "height: 10px;\n"
                        "}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QLabel(Form)
        self.label_9.setText("")
        self.label_9.setPixmap(QPixmap(":/futminna"))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QLabel(Form)
        self.label_10.setStyleSheet("font: 16pt \"Comic Sans MS\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "About Application"))
        self.label_10.setText(_translate("Form", "iLecture Grading System"))
        self.label.setText(_translate("Form", "Software Development Team "))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:14pt;\">1. Abdullahi Zekeri </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:14pt;\">2. Owuri Hanifat</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:14pt;\">3. Emiola Tobi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:14pt;\">4. Manasseh Mmadu</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:14pt;\">5. Ivever Timothy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:14pt;\">6. Bekaiye Martins</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Developed using Python PyQt5 on Windows "))
