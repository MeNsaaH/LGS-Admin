# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Home(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 712)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet("QComboBox, QLineEdit {\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(207, 207, 207);\n"
"font: 12pt \"Consolas\";\n"
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
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_14 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: rgb(0, 170, 0);\n"
"font: 16pt \"Monaco\";\n"
"background: #ffffff;\n"
"padding: 0px\n"
"}\n"
"QPushButton:hover#pushButton{\n"
"color: rgb(0, 170, 0);\n"
"font: 16pt \"Monaco\";\n"
"background: #ffffff;\n"
"padding: 30px;\n"
"border: None\n"
"}")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/logo"), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_38.addWidget(self.pushButton)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(204, 204, 204);\n"
"    border-right: 2px solid rgb(115, 115, 115);\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 20px;\n"
"    height: 40px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.courseGrading = QPushButton(self.frame)
        self.courseGrading.setObjectName("courseGrading")
        self.verticalLayout_11.addWidget(self.courseGrading)
        self.manLecturerBtn = QPushButton(self.frame)
        self.manLecturerBtn.setObjectName("manLecturerBtn")
        self.verticalLayout_11.addWidget(self.manLecturerBtn)
        self.manCoursesBtn = QPushButton(self.frame)
        self.manCoursesBtn.setObjectName("manCoursesBtn")
        self.verticalLayout_11.addWidget(self.manCoursesBtn)
        self.manClassRepsBtn = QPushButton(self.frame)
        self.manClassRepsBtn.setObjectName("manClassRepsBtn")
        self.verticalLayout_11.addWidget(self.manClassRepsBtn)
        self.manLectHallBtn = QPushButton(self.frame)
        self.manLectHallBtn.setObjectName("manLectHallBtn")
        self.verticalLayout_11.addWidget(self.manLectHallBtn)
        self.settingBtn = QPushButton(self.frame)
        self.settingBtn.setObjectName("settingBtn")
        self.verticalLayout_11.addWidget(self.settingBtn)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.horizontalLayout_5.addWidget(self.frame)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.HomePage = QWidget()
        self.HomePage.setObjectName("HomePage")
        self.verticalLayout_32 = QVBoxLayout(self.HomePage)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.frame_2 = QFrame(self.HomePage)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_31 = QVBoxLayout(self.frame_2)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_31.addWidget(self.label)
        self.textBrowser = QTextBrowser(self.frame_2)
        self.textBrowser.setStyleSheet("border-top: 5px solid rgb(0, 85, 0)")
        self.textBrowser.setFrameShape(QFrame.Box)
        self.textBrowser.setFrameShadow(QFrame.Raised)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_31.addWidget(self.textBrowser)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_31.addLayout(self.horizontalLayout_6)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_31.addItem(spacerItem3)
        self.verticalLayout_32.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.HomePage)
        self.gradingPage = QWidget()
        self.gradingPage.setObjectName("gradingPage")
        self.verticalLayout_40 = QVBoxLayout(self.gradingPage)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.widget = QWidget(self.gradingPage)
        self.widget.setStyleSheet("\n"
"QComboBox, QLineEdit {\n"
"border-radius: 5px;\n"
"border: 3px solid rgb(207, 207, 207);\n"
"font: 12pt \"Consolas\";\n"
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
"font-family: Comic Sans Ms;\n"
"padding: 5px;\n"
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
        self.widget.setObjectName("widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.levelCombo = QComboBox(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.levelCombo.sizePolicy().hasHeightForWidth())
        self.levelCombo.setSizePolicy(sizePolicy)
        self.levelCombo.setMinimumSize(QSize(140, 0))
        self.levelCombo.setStyleSheet("")
        self.levelCombo.setObjectName("levelCombo")
        self.levelCombo.addItem("")
        self.levelCombo.addItem("")
        self.levelCombo.addItem("")
        self.levelCombo.addItem("")
        self.levelCombo.addItem("")
        self.levelCombo.addItem("")
        self.verticalLayout_8.addWidget(self.levelCombo)
        spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lecturerCombo = QComboBox(self.widget)
        self.lecturerCombo.setStyleSheet("height: 25px")
        self.lecturerCombo.setObjectName("lecturerCombo")
        self.lecturerCombo.addItem("")
        self.verticalLayout_9.addWidget(self.lecturerCombo)
        self.courseCombo = QComboBox(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.courseCombo.sizePolicy().hasHeightForWidth())
        self.courseCombo.setSizePolicy(sizePolicy)
        self.courseCombo.setMinimumSize(QSize(400, 0))
        self.courseCombo.setStyleSheet("height: 25px")
        self.courseCombo.setObjectName("courseCombo")
        self.courseCombo.addItem("")
        self.verticalLayout_9.addWidget(self.courseCombo)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.chngResource = QPushButton(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chngResource.sizePolicy().hasHeightForWidth())
        self.chngResource.setSizePolicy(sizePolicy)
        self.chngResource.setStyleSheet("padding: 10px;\n"
"height: 30px")
        self.chngResource.setObjectName("chngResource")
        self.horizontalLayout_4.addWidget(self.chngResource)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.getGrading = QPushButton(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getGrading.sizePolicy().hasHeightForWidth())
        self.getGrading.setSizePolicy(sizePolicy)
        self.getGrading.setStyleSheet("height: 30px;\n"
"padding: 10px")
        self.getGrading.setObjectName("getGrading")
        self.horizontalLayout_4.addWidget(self.getGrading)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setStyleSheet("font: 9pt \"Comic Sans MS\";")
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.recentCourseTab = QWidget()
        self.recentCourseTab.setStyleSheet("")
        self.recentCourseTab.setObjectName("recentCourseTab")
        self.verticalLayout_6 = QVBoxLayout(self.recentCourseTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget_2 = QStackedWidget(self.recentCourseTab)
        self.stackedWidget_2.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_33 = QLabel(self.page)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_5.addWidget(self.label_33)
        self.label_34 = QLabel(self.page)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_5.addWidget(self.label_34)
        self.label_35 = QLabel(self.page)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_5.addWidget(self.label_35)
        spacerItem7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.summaryWidget = QWidget(self.page)
        self.summaryWidget.setObjectName("summaryWidget")
        self.gridLayout_8 = QGridLayout(self.summaryWidget)
        self.gridLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_99 = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy)
        self.label_99.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_99.setObjectName("label_99")
        self.gridLayout_8.addWidget(self.label_99, 0, 0, 1, 1)
        self.label_103 = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy)
        self.label_103.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_103.setObjectName("label_103")
        self.gridLayout_8.addWidget(self.label_103, 2, 0, 1, 1)
        self.ave_no_students = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ave_no_students.sizePolicy().hasHeightForWidth())
        self.ave_no_students.setSizePolicy(sizePolicy)
        self.ave_no_students.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.ave_no_students.setObjectName("ave_no_students")
        self.gridLayout_8.addWidget(self.ave_no_students, 4, 1, 1, 1)
        self.no_lectures = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_lectures.sizePolicy().hasHeightForWidth())
        self.no_lectures.setSizePolicy(sizePolicy)
        self.no_lectures.setObjectName("no_lectures")
        self.gridLayout_8.addWidget(self.no_lectures, 3, 1, 1, 1)
        self.label_101 = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy)
        self.label_101.setObjectName("label_101")
        self.gridLayout_8.addWidget(self.label_101, 1, 0, 1, 1)
        self.lect_hall = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lect_hall.sizePolicy().hasHeightForWidth())
        self.lect_hall.setSizePolicy(sizePolicy)
        self.lect_hall.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.lect_hall.setObjectName("lect_hall")
        self.gridLayout_8.addWidget(self.lect_hall, 2, 1, 1, 1)
        self.label_102 = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)
        self.label_102.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_102.setObjectName("label_102")
        self.gridLayout_8.addWidget(self.label_102, 4, 0, 1, 1)
        self.course_name = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_name.sizePolicy().hasHeightForWidth())
        self.course_name.setSizePolicy(sizePolicy)
        self.course_name.setObjectName("course_name")
        self.gridLayout_8.addWidget(self.course_name, 1, 1, 1, 1)
        self.label_100 = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy)
        self.label_100.setObjectName("label_100")
        self.gridLayout_8.addWidget(self.label_100, 3, 0, 1, 1)
        self.lect_fname = QLabel(self.summaryWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lect_fname.sizePolicy().hasHeightForWidth())
        self.lect_fname.setSizePolicy(sizePolicy)
        self.lect_fname.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.lect_fname.setObjectName("lect_fname")
        self.gridLayout_8.addWidget(self.lect_fname, 0, 1, 1, 1)
        self.label_104 = QLabel(self.summaryWidget)
        self.label_104.setObjectName("label_104")
        self.gridLayout_8.addWidget(self.label_104, 5, 0, 1, 1)
        self.lect_time = QLabel(self.summaryWidget)
        self.lect_time.setObjectName("lect_time")
        self.gridLayout_8.addWidget(self.lect_time, 5, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.summaryWidget)
        spacerItem8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.stackedWidget_2.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.page_3.setObjectName("page_3")
        self.verticalLayout_33 = QVBoxLayout(self.page_3)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        spacerItem9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_33.addItem(spacerItem9)
        self.label_2 = QLabel(self.page_3)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 100))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0, 85, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_33.addWidget(self.label_2)
        spacerItem10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_33.addItem(spacerItem10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QLabel(self.page_3)
        self.label_4.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 10pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QLabel(self.page_3)
        self.label_6.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QLabel(self.page_3)
        self.label_7.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_8 = QLabel(self.page_3)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_9 = QLabel(self.page_3)
        self.label_9.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 40)
        self.gridLayout.setRowMinimumHeight(1, 40)
        self.gridLayout.setRowMinimumHeight(2, 40)
        self.gridLayout.setRowMinimumHeight(3, 40)
        self.verticalLayout_33.addLayout(self.gridLayout)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.page_4.setObjectName("page_4")
        self.verticalLayout_34 = QVBoxLayout(self.page_4)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_34.addItem(spacerItem11)
        self.label_11 = QLabel(self.page_4)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0, 85, 0);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_34.addWidget(self.label_11)
        spacerItem12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_34.addItem(spacerItem12)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_20 = QLabel(self.page_4)
        self.label_20.setStyleSheet("")
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_19 = QLabel(self.page_4)
        self.label_19.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_12 = QLabel(self.page_4)
        self.label_12.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_17 = QLabel(self.page_4)
        self.label_17.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 2, 1, 1, 1, Qt.AlignHCenter)
        self.label_16 = QLabel(self.page_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 1, 1, 1, Qt.AlignHCenter)
        self.label_15 = QLabel(self.page_4)
        self.label_15.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 1, 1, 1, Qt.AlignHCenter)
        self.label_14 = QLabel(self.page_4)
        self.label_14.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_18 = QLabel(self.page_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_21 = QLabel(self.page_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 1, 1, 1, Qt.AlignHCenter)
        self.label_22 = QLabel(self.page_4)
        self.label_22.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 6, 0, 1, 1)
        self.label_23 = QLabel(self.page_4)
        self.label_23.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 4, 1, 1, 1, Qt.AlignHCenter)
        self.label_24 = QLabel(self.page_4)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 5, 1, 1, 1, Qt.AlignHCenter)
        self.label_25 = QLabel(self.page_4)
        self.label_25.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 6, 1, 1, 1, Qt.AlignHCenter)
        self.verticalLayout_34.addLayout(self.gridLayout_2)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_35 = QVBoxLayout(self.page_5)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        spacerItem13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_35.addItem(spacerItem13)
        self.label_39 = QLabel(self.page_5)
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0, 85, 0);\n"
"height: 100px")
        self.label_39.setObjectName("label_39")
        self.verticalLayout_35.addWidget(self.label_39)
        spacerItem14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_35.addItem(spacerItem14)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_30 = QLabel(self.page_5)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 1, 1, 1, 1, Qt.AlignHCenter)
        self.label_27 = QLabel(self.page_5)
        self.label_27.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_28 = QLabel(self.page_5)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_32 = QLabel(self.page_5)
        self.label_32.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_31 = QLabel(self.page_5)
        self.label_31.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 0, 1, 1, 1, Qt.AlignHCenter)
        self.label_29 = QLabel(self.page_5)
        self.label_29.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 2, 1, 1, 1, Qt.AlignHCenter)
        self.gridLayout_3.setRowMinimumHeight(0, 50)
        self.gridLayout_3.setRowMinimumHeight(1, 50)
        self.gridLayout_3.setRowMinimumHeight(2, 50)
        self.verticalLayout_35.addLayout(self.gridLayout_3)
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_36 = QVBoxLayout(self.page_6)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.label_42 = QLabel(self.page_6)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0, 85, 0);")
        self.label_42.setObjectName("label_42")
        self.verticalLayout_36.addWidget(self.label_42)
        spacerItem15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_36.addItem(spacerItem15)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_51 = QLabel(self.page_6)
        self.label_51.setObjectName("label_51")
        self.gridLayout_5.addWidget(self.label_51, 3, 1, 1, 1, Qt.AlignHCenter)
        self.label_44 = QLabel(self.page_6)
        self.label_44.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_44.setObjectName("label_44")
        self.gridLayout_5.addWidget(self.label_44, 2, 0, 1, 1)
        self.label_45 = QLabel(self.page_6)
        self.label_45.setObjectName("label_45")
        self.gridLayout_5.addWidget(self.label_45, 1, 0, 1, 1)
        self.label_46 = QLabel(self.page_6)
        self.label_46.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_46.setObjectName("label_46")
        self.gridLayout_5.addWidget(self.label_46, 2, 1, 1, 1, Qt.AlignHCenter)
        self.label_47 = QLabel(self.page_6)
        self.label_47.setObjectName("label_47")
        self.gridLayout_5.addWidget(self.label_47, 1, 1, 1, 1, Qt.AlignHCenter)
        self.label_50 = QLabel(self.page_6)
        self.label_50.setObjectName("label_50")
        self.gridLayout_5.addWidget(self.label_50, 3, 0, 1, 1)
        self.label_48 = QLabel(self.page_6)
        self.label_48.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_48.setObjectName("label_48")
        self.gridLayout_5.addWidget(self.label_48, 0, 1, 1, 1, Qt.AlignHCenter)
        self.label_49 = QLabel(self.page_6)
        self.label_49.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_49.setObjectName("label_49")
        self.gridLayout_5.addWidget(self.label_49, 0, 0, 1, 1)
        self.verticalLayout_36.addLayout(self.gridLayout_5)
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_12 = QWidget()
        self.page_12.setObjectName("page_12")
        self.verticalLayout_37 = QVBoxLayout(self.page_12)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_72 = QLabel(self.page_12)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMinimumSize(QSize(100, 0))
        self.label_72.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0, 85, 0);")
        self.label_72.setObjectName("label_72")
        self.verticalLayout_37.addWidget(self.label_72)
        spacerItem16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_37.addItem(spacerItem16)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_43 = QLabel(self.page_12)
        self.label_43.setStyleSheet("")
        self.label_43.setObjectName("label_43")
        self.gridLayout_7.addWidget(self.label_43, 5, 0, 1, 1)
        self.label_52 = QLabel(self.page_12)
        self.label_52.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_52.setObjectName("label_52")
        self.gridLayout_7.addWidget(self.label_52, 4, 0, 1, 1)
        self.label_53 = QLabel(self.page_12)
        self.label_53.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_53.setObjectName("label_53")
        self.gridLayout_7.addWidget(self.label_53, 2, 0, 1, 1)
        self.label_54 = QLabel(self.page_12)
        self.label_54.setObjectName("label_54")
        self.gridLayout_7.addWidget(self.label_54, 1, 0, 1, 1)
        self.label_55 = QLabel(self.page_12)
        self.label_55.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_55.setObjectName("label_55")
        self.gridLayout_7.addWidget(self.label_55, 2, 1, 1, 1, Qt.AlignHCenter)
        self.label_63 = QLabel(self.page_12)
        self.label_63.setObjectName("label_63")
        self.gridLayout_7.addWidget(self.label_63, 1, 1, 1, 1, Qt.AlignHCenter)
        self.label_64 = QLabel(self.page_12)
        self.label_64.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_64.setObjectName("label_64")
        self.gridLayout_7.addWidget(self.label_64, 0, 1, 1, 1, Qt.AlignHCenter)
        self.label_65 = QLabel(self.page_12)
        self.label_65.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_65.setObjectName("label_65")
        self.gridLayout_7.addWidget(self.label_65, 0, 0, 1, 1)
        self.label_66 = QLabel(self.page_12)
        self.label_66.setObjectName("label_66")
        self.gridLayout_7.addWidget(self.label_66, 3, 0, 1, 1)
        self.label_67 = QLabel(self.page_12)
        self.label_67.setObjectName("label_67")
        self.gridLayout_7.addWidget(self.label_67, 3, 1, 1, 1, Qt.AlignHCenter)
        self.label_68 = QLabel(self.page_12)
        self.label_68.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 10pt \"Comic Sans MS\";")
        self.label_68.setObjectName("label_68")
        self.gridLayout_7.addWidget(self.label_68, 6, 0, 1, 1)
        self.label_69 = QLabel(self.page_12)
        self.label_69.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_69.setObjectName("label_69")
        self.gridLayout_7.addWidget(self.label_69, 4, 1, 1, 1, Qt.AlignHCenter)
        self.label_70 = QLabel(self.page_12)
        self.label_70.setObjectName("label_70")
        self.gridLayout_7.addWidget(self.label_70, 5, 1, 1, 1, Qt.AlignHCenter)
        self.label_71 = QLabel(self.page_12)
        self.label_71.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_71.setObjectName("label_71")
        self.gridLayout_7.addWidget(self.label_71, 6, 1, 1, 1, Qt.AlignHCenter)
        self.gridLayout_7.setRowMinimumHeight(0, 30)
        self.gridLayout_7.setRowMinimumHeight(1, 30)
        self.gridLayout_7.setRowMinimumHeight(2, 30)
        self.gridLayout_7.setRowMinimumHeight(3, 30)
        self.gridLayout_7.setRowMinimumHeight(4, 30)
        self.gridLayout_7.setRowMinimumHeight(5, 30)
        self.verticalLayout_37.addLayout(self.gridLayout_7)
        self.stackedWidget_2.addWidget(self.page_12)
        self.verticalLayout_6.addWidget(self.stackedWidget_2)
        self.tabWidget.addTab(self.recentCourseTab, "")
        self.recommndTab = QWidget()
        self.recommndTab.setObjectName("recommndTab")
        self.verticalLayout_12 = QVBoxLayout(self.recommndTab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_26 = QLabel(self.recommndTab)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_12.addWidget(self.label_26)
        self.commentTable = QTableWidget(self.recommndTab)
        self.commentTable.setMinimumSize(QSize(0, 0))
        self.commentTable.setMaximumSize(QSize(16777215, 16777215))
        self.commentTable.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.commentTable.setDragEnabled(False)
        self.commentTable.setAlternatingRowColors(True)
        self.commentTable.setSelectionMode(QAbstractItemView.MultiSelection)
        self.commentTable.setGridStyle(Qt.SolidLine)
        self.commentTable.setWordWrap(True)
        self.commentTable.setObjectName("commentTable")
        self.commentTable.setColumnCount(2)
        self.commentTable.setRowCount(2)
        item = QTableWidgetItem()
        self.commentTable.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.commentTable.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.commentTable.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.commentTable.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        self.commentTable.setItem(0, 0, item)
        item = QTableWidgetItem()
        self.commentTable.setItem(0, 1, item)
        self.commentTable.horizontalHeader().setDefaultSectionSize(486)
        self.verticalLayout_12.addWidget(self.commentTable)
        self.tabWidget.addTab(self.recommndTab, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevBtn = QPushButton(self.frame_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevBtn.sizePolicy().hasHeightForWidth())
        self.prevBtn.setSizePolicy(sizePolicy)
        self.prevBtn.setStyleSheet("padding: 10px;\n"
"width: 100px")
        self.prevBtn.setObjectName("prevBtn")
        self.horizontalLayout.addWidget(self.prevBtn)
        spacerItem17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.nextBtn = QPushButton(self.frame_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        self.nextBtn.setStyleSheet("padding: 10px;\n"
"width: 100px")
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout.addWidget(self.nextBtn)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addWidget(self.frame_3)
        self.verticalLayout_40.addWidget(self.widget)
        self.stackedWidget.addWidget(self.gradingPage)
        self.lectHallPage = QWidget()
        self.lectHallPage.setObjectName("lectHallPage")
        self.verticalLayout_17 = QVBoxLayout(self.lectHallPage)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.widget_5 = QWidget(self.lectHallPage)
        self.widget_5.setStyleSheet("")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_94 = QLabel(self.widget_5)
        self.label_94.setMinimumSize(QSize(263, 0))
        self.label_94.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label_94.setScaledContents(True)
        self.label_94.setObjectName("label_94")
        self.verticalLayout_13.addWidget(self.label_94)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_95 = QLabel(self.widget_5)
        self.label_95.setObjectName("label_95")
        self.verticalLayout_4.addWidget(self.label_95)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_96 = QLabel(self.widget_5)
        self.label_96.setObjectName("label_96")
        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_96)
        self.lectVenueDesc = QLineEdit(self.widget_5)
        self.lectVenueDesc.setMinimumSize(QSize(400, 0))
        self.lectVenueDesc.setObjectName("lectVenueDesc")
        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lectVenueDesc)
        self.label_97 = QLabel(self.widget_5)
        self.label_97.setObjectName("label_97")
        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_97)
        self.lectSchList = QComboBox(self.widget_5)
        self.lectSchList.setMinimumSize(QSize(163, 0))
        self.lectSchList.setObjectName("lectSchList")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lectSchList)
        self.verticalLayout_4.addLayout(self.formLayout_5)
        spacerItem18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem18)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem19)
        self.addVenue = QPushButton(self.widget_5)
        self.addVenue.setStyleSheet("padding: 10px;\n"
"")
        self.addVenue.setObjectName("addVenue")
        self.horizontalLayout_7.addWidget(self.addVenue)
        spacerItem20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_13.addLayout(self.verticalLayout_4)
        spacerItem21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem21)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        spacerItem22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem22)
        self.line_4 = QFrame(self.widget_5)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_8.addWidget(self.line_4)
        spacerItem23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem23)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_98 = QLabel(self.widget_5)
        self.label_98.setObjectName("label_98")
        self.verticalLayout_15.addWidget(self.label_98)
        self.lectVenueList = QListWidget(self.widget_5)
        self.lectVenueList.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.lectVenueList.setMovement(QListView.Free)
        self.lectVenueList.setResizeMode(QListView.Adjust)
        self.lectVenueList.setObjectName("lectVenueList")
        self.verticalLayout_15.addWidget(self.lectVenueList)
        self.horizontalLayout_8.addLayout(self.verticalLayout_15)
        self.verticalLayout_16.addLayout(self.horizontalLayout_8)
        self.verticalLayout_17.addWidget(self.widget_5)
        self.stackedWidget.addWidget(self.lectHallPage)
        self.coursesPage = QWidget()
        self.coursesPage.setObjectName("coursesPage")
        self.verticalLayout_21 = QVBoxLayout(self.coursesPage)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.widget_4 = QWidget(self.coursesPage)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_20 = QVBoxLayout(self.widget_4)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_89 = QLabel(self.widget_4)
        self.label_89.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label_89.setObjectName("label_89")
        self.verticalLayout_18.addWidget(self.label_89)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_90 = QLabel(self.widget_4)
        self.label_90.setObjectName("label_90")
        self.verticalLayout_3.addWidget(self.label_90)
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_91 = QLabel(self.widget_4)
        self.label_91.setObjectName("label_91")
        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_91)
        self.label_92 = QLabel(self.widget_4)
        self.label_92.setObjectName("label_92")
        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_92)
        spacerItem24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout_4.setItem(2, QFormLayout.FieldRole, spacerItem24)
        self.courseCode = QLineEdit(self.widget_4)
        self.courseCode.setMinimumSize(QSize(400, 0))
        self.courseCode.setObjectName("courseCode")
        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.courseCode)
        self.courseName = QLineEdit(self.widget_4)
        self.courseName.setObjectName("courseName")
        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.courseName)
        self.verticalLayout_3.addLayout(self.formLayout_4)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem25)
        self.addCourseBtn = QPushButton(self.widget_4)
        self.addCourseBtn.setStyleSheet("padding: 10px;")
        self.addCourseBtn.setObjectName("addCourseBtn")
        self.horizontalLayout_9.addWidget(self.addCourseBtn)
        spacerItem26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem26)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_18.addLayout(self.verticalLayout_3)
        spacerItem27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem27)
        self.horizontalLayout_10.addLayout(self.verticalLayout_18)
        spacerItem28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem28)
        self.line_3 = QFrame(self.widget_4)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_10.addWidget(self.line_3)
        spacerItem29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem29)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_93 = QLabel(self.widget_4)
        self.label_93.setObjectName("label_93")
        self.verticalLayout_19.addWidget(self.label_93)
        self.courseList = QListWidget(self.widget_4)
        self.courseList.setMinimumSize(QSize(300, 0))
        self.courseList.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.courseList.setObjectName("courseList")
        self.verticalLayout_19.addWidget(self.courseList)
        self.horizontalLayout_10.addLayout(self.verticalLayout_19)
        self.verticalLayout_20.addLayout(self.horizontalLayout_10)
        self.verticalLayout_21.addWidget(self.widget_4)
        self.stackedWidget.addWidget(self.coursesPage)
        self.lecturersPage = QWidget()
        self.lecturersPage.setObjectName("lecturersPage")
        self.verticalLayout_26 = QVBoxLayout(self.lecturersPage)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.widget_3 = QWidget(self.lecturersPage)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_25 = QVBoxLayout(self.widget_3)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_78 = QLabel(self.widget_3)
        self.label_78.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label_78.setObjectName("label_78")
        self.verticalLayout_23.addWidget(self.label_78)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_79 = QLabel(self.widget_3)
        self.label_79.setObjectName("label_79")
        self.verticalLayout_2.addWidget(self.label_79)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_80 = QLabel(self.widget_3)
        self.label_80.setObjectName("label_80")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_80)
        self.label_81 = QLabel(self.widget_3)
        self.label_81.setObjectName("label_81")
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_81)
        self.lectFname = QLineEdit(self.widget_3)
        self.lectFname.setMinimumSize(QSize(400, 0))
        self.lectFname.setObjectName("lectFname")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lectFname)
        self.lectTitleCombo = QComboBox(self.widget_3)
        self.lectTitleCombo.setObjectName("comboBox")
        self.lectTitleCombo.addItem("")
        self.lectTitleCombo.addItem("")
        self.lectTitleCombo.addItem("")
        self.lectTitleCombo.addItem("")
        self.lectTitleCombo.addItem("")
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lectTitleCombo)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        spacerItem30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem30)
        self.label_82 = QLabel(self.widget_3)
        self.label_82.setObjectName("label_82")
        self.verticalLayout_2.addWidget(self.label_82)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_83 = QLabel(self.widget_3)
        self.label_83.setObjectName("label_83")
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_83)
        self.label_84 = QLabel(self.widget_3)
        self.label_84.setObjectName("label_84")
        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_84)
        self.label_85 = QLabel(self.widget_3)
        self.label_85.setObjectName("label_85")
        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_85)
        self.label_86 = QLabel(self.widget_3)
        self.label_86.setObjectName("label_86")
        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_86)
        self.label_87 = QLabel(self.widget_3)
        self.label_87.setObjectName("label_87")
        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_87)
        spacerItem31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout_3.setItem(5, QFormLayout.LabelRole, spacerItem31)
        self.course1 = QComboBox(self.widget_3)
        self.course1.setObjectName("course1")
        self.course1.addItem("")
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.course1)
        self.course2 = QComboBox(self.widget_3)
        self.course2.setObjectName("course2")
        self.course2.addItem("")
        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.course2)
        self.course3 = QComboBox(self.widget_3)
        self.course3.setObjectName("course3")
        self.course3.addItem("")
        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.course3)
        self.course4 = QComboBox(self.widget_3)
        self.course4.setObjectName("course4")
        self.course4.addItem("")
        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.course4)
        self.course5 = QComboBox(self.widget_3)
        self.course5.setObjectName("course5")
        self.course5.addItem("")
        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.course5)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.verticalLayout_22.addLayout(self.verticalLayout_2)
        spacerItem32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem32)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem33)
        self.addLecturer = QPushButton(self.widget_3)
        self.addLecturer.setMinimumSize(QSize(0, 40))
        self.addLecturer.setStyleSheet("padding:10px")
        self.addLecturer.setObjectName("addLecturer")
        self.horizontalLayout_11.addWidget(self.addLecturer)
        spacerItem34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem34)
        self.verticalLayout_22.addLayout(self.horizontalLayout_11)
        spacerItem35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem35)
        self.verticalLayout_23.addLayout(self.verticalLayout_22)
        self.horizontalLayout_12.addLayout(self.verticalLayout_23)
        spacerItem36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem36)
        self.line_2 = QFrame(self.widget_3)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_12.addWidget(self.line_2)
        spacerItem37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem37)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_88 = QLabel(self.widget_3)
        self.label_88.setObjectName("label_88")
        self.verticalLayout_24.addWidget(self.label_88)
        self.lectList = QListWidget(self.widget_3)
        self.lectList.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.lectList.setObjectName("lectList")
        self.verticalLayout_24.addWidget(self.lectList)
        self.horizontalLayout_12.addLayout(self.verticalLayout_24)
        self.verticalLayout_25.addLayout(self.horizontalLayout_12)
        self.verticalLayout_26.addWidget(self.widget_3)
        self.stackedWidget.addWidget(self.lecturersPage)
        self.ClassRepsPage = QWidget()
        self.ClassRepsPage.setObjectName("ClassRepsPage")
        self.verticalLayout_30 = QVBoxLayout(self.ClassRepsPage)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.widget_2 = QWidget(self.ClassRepsPage)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_29 = QVBoxLayout(self.widget_2)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_73 = QLabel(self.widget_2)
        self.label_73.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label_73.setObjectName("label_73")
        self.verticalLayout_27.addWidget(self.label_73)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_74 = QLabel(self.widget_2)
        self.label_74.setObjectName("label_74")
        self.verticalLayout.addWidget(self.label_74)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_75 = QLabel(self.widget_2)
        self.label_75.setObjectName("label_75")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_75)
        spacerItem38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(4, QFormLayout.FieldRole, spacerItem38)
        self.cr_level = QComboBox(self.widget_2)
        self.cr_level.setObjectName("cr_level")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cr_level)
        self.label_76 = QLabel(self.widget_2)
        self.label_76.setObjectName("label_76")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_76)
        self.cr_username = QComboBox(self.widget_2)
        self.cr_username.setMinimumSize(QSize(400, 0))
        self.cr_username.setObjectName("cr_username")
        self.cr_username.addItem("")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cr_username)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem39)
        self.addcrBtn = QPushButton(self.widget_2)
        self.addcrBtn.setStyleSheet("padding: 10px;")
        self.addcrBtn.setObjectName("addcrBtn")
        self.horizontalLayout_13.addWidget(self.addcrBtn)
        spacerItem40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem40)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        spacerItem41 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem41)
        self.verticalLayout_27.addLayout(self.verticalLayout)
        self.horizontalLayout_14.addLayout(self.verticalLayout_27)
        spacerItem42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem42)
        self.line = QFrame(self.widget_2)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_14.addWidget(self.line)
        spacerItem43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem43)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_77 = QLabel(self.widget_2)
        self.label_77.setObjectName("label_77")
        self.verticalLayout_28.addWidget(self.label_77)
        self.cr_list = QListWidget(self.widget_2)
        self.cr_list.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.cr_list.setObjectName("cr_list")
        self.verticalLayout_28.addWidget(self.cr_list)
        self.horizontalLayout_14.addLayout(self.verticalLayout_28)
        self.verticalLayout_29.addLayout(self.horizontalLayout_14)
        self.verticalLayout_30.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.ClassRepsPage)
        self.settingPage = QWidget()
        self.settingPage.setObjectName("settingPage")
        self.horizontalLayout_16 = QHBoxLayout(self.settingPage)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem44)
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.groupBox = QGroupBox(self.settingPage)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    font: 75 10pt \"Monaco\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 5px;\n"
"    background-color: rgb(25, 93, 39);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(25, 93, 39);\n"
"    background: #ffffff;\n"
"    border: 2px solid rgb(25, 93, 39);\n"
"}")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.logoutBtn = QPushButton(self.groupBox)
        self.logoutBtn.setMinimumSize(QSize(100, 0))
        self.logoutBtn.setStyleSheet("")
        self.logoutBtn.setObjectName("logoutBtn")
        self.verticalLayout_39.addWidget(self.logoutBtn)
        self.changeAccountBtn = QPushButton(self.groupBox)
        self.changeAccountBtn.setObjectName("changeAccountBtn")
        self.verticalLayout_39.addWidget(self.changeAccountBtn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_39)
        spacerItem45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem45)
        self.verticalLayout_43.addWidget(self.groupBox)
        spacerItem46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout_43.addItem(spacerItem46)
        self.groupBox_2 = QGroupBox(self.settingPage)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    font: 75 10pt \"Monaco\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 5px;\n"
"    background-color: rgb(25, 93, 39);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(25, 93, 39);\n"
"    background: #ffffff;\n"
"    border: 2px solid rgb(25, 93, 39);\n"
"}")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.helpBtn = QPushButton(self.groupBox_2)
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_41.addWidget(self.helpBtn)
        self.aboutButton = QPushButton(self.groupBox_2)
        self.aboutButton.setObjectName("aboutButton")
        self.verticalLayout_41.addWidget(self.aboutButton)
        self.updateBtn = QPushButton(self.groupBox_2)
        self.updateBtn.setObjectName("updateBtn")
        self.verticalLayout_41.addWidget(self.updateBtn)
        self.reportBtn = QPushButton(self.groupBox_2)
        self.reportBtn.setObjectName("reportBtn")
        self.verticalLayout_41.addWidget(self.reportBtn)
        self.horizontalLayout_15.addLayout(self.verticalLayout_41)
        spacerItem47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem47)
        self.verticalLayout_43.addWidget(self.groupBox_2)
        spacerItem48 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_43.addItem(spacerItem48)
        self.horizontalLayout_16.addLayout(self.verticalLayout_43)
        spacerItem49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem49)
        spacerItem50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem50)
        spacerItem51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem51)
        spacerItem52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem52)
        spacerItem53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem53)
        spacerItem54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem54)
        spacerItem55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem55)
        self.stackedWidget.addWidget(self.settingPage)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.verticalLayout_38.addLayout(self.horizontalLayout_5)
        self.verticalLayout_14.addLayout(self.verticalLayout_38)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "     iLecture Grading System"))
        self.courseGrading.setText(_translate("MainWindow", "View Course Gradings"))
        self.manLecturerBtn.setText(_translate("MainWindow", "Manage Lecturer"))
        self.manCoursesBtn.setText(_translate("MainWindow", "Manage Courses"))
        self.manClassRepsBtn.setText(_translate("MainWindow", "Manage Class Reps"))
        self.manLectHallBtn.setText(_translate("MainWindow", "Manage Lecture Venues"))
        self.settingBtn.setText(_translate("MainWindow", "Settings and Help"))
        self.label.setText(_translate("MainWindow", "Welcome to the iLecture Grading System"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":futminna_logo\" /><span style=\" font-family:\'Monaco\'; font-size:13pt;\">An application that connects you to your students feelings about the efficiency of their lectures and how to improve them</span></p></body></html>"))
        self.levelCombo.setItemText(0, _translate("MainWindow", "Select Level"))
        self.levelCombo.setItemText(1, _translate("MainWindow", "100"))
        self.levelCombo.setItemText(2, _translate("MainWindow", "200"))
        self.levelCombo.setItemText(3, _translate("MainWindow", "300"))
        self.levelCombo.setItemText(4, _translate("MainWindow", "400"))
        self.levelCombo.setItemText(5, _translate("MainWindow", "500"))
        self.lecturerCombo.setItemText(0, _translate("MainWindow", "Select Lecturer"))
        self.courseCombo.setItemText(0, _translate("MainWindow", "Select Course"))
        self.chngResource.setText(_translate("MainWindow", "Show Cumulated Grading"))
        self.getGrading.setText(_translate("MainWindow", "Get Gradings"))
        self.label_33.setText(_translate("MainWindow", "Course Grading presents an average grading for a lecturer presented by the student."))
        self.label_34.setText(_translate("MainWindow", "To get recent grading for last lecture, click <i><b>Get Grading</b></i>. "))
        self.label_35.setText(_translate("MainWindow", "To get the accumulated grading over all lectures, click <b><i>Show Cumulated Grading</i></b>"))
        self.label_99.setText(_translate("MainWindow", "Lecturer\'s Fullname:"))
        self.label_103.setText(_translate("MainWindow", "Lecture Hall Used"))
        self.ave_no_students.setText(_translate("MainWindow", "N/A"))
        self.no_lectures.setText(_translate("MainWindow", "N/A"))
        self.label_101.setText(_translate("MainWindow", "Course"))
        self.lect_hall.setText(_translate("MainWindow", "N/A"))
        self.label_102.setText(_translate("MainWindow", "Average No of Students"))
        self.course_name.setText(_translate("MainWindow", "N/A"))
        self.label_100.setText(_translate("MainWindow", "Number of Lectures"))
        self.lect_fname.setText(_translate("MainWindow", "N/A"))
        self.label_104.setText(_translate("MainWindow", "Last Lecture Time"))
        self.lect_time.setText(_translate("MainWindow", "N/A"))
        self.label_2.setText(_translate("MainWindow", "To what extend students agree with the following statements about what this lecturer does regarding this course"))
        self.label_3.setText(_translate("MainWindow", "Informs students about the course grading system at the beginning of each semester"))
        self.label_4.setText(_translate("MainWindow", "Informs students what he/she expects from them on this course at the beginning of the semester"))
        self.label_5.setText(_translate("MainWindow", "Provides or directs students to additional reading sources"))
        self.label_6.setText(_translate("MainWindow", "Provides students with course outlines at the beginning of each semester"))
        self.label_7.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_8.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_9.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_10.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_11.setText(_translate("MainWindow", "This Lecturer"))
        self.label_20.setText(_translate("MainWindow", "Treatss students equally regardless of gender"))
        self.label_19.setText(_translate("MainWindow", "is Fair with his/her grading system (marks)"))
        self.label_12.setText(_translate("MainWindow", "Makes the course challenging but interesting"))
        self.label_13.setText(_translate("MainWindow", "is tolerant of students"))
        self.label_17.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_16.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_15.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_14.setText(_translate("MainWindow", "is considerate to students"))
        self.label_18.setText(_translate("MainWindow", "Encourages students to understand all phases of the course                "))
        self.label_21.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_22.setText(_translate("MainWindow", "Has high expectation for students"))
        self.label_23.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_24.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_25.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_39.setText(_translate("MainWindow", "This lecturer is accessible to students for academic Discussion"))
        self.label_30.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_27.setText(_translate("MainWindow", "Not available at all"))
        self.label_28.setText(_translate("MainWindow", "Outside the classroom"))
        self.label_32.setText(_translate("MainWindow", "inside the classroom                                                                                                        "))
        self.label_31.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_29.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_42.setText(_translate("MainWindow", "How would you rate lecturer\'s class Attendance"))
        self.label_51.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_44.setText(_translate("MainWindow", "Sometimes late to class"))
        self.label_45.setText(_translate("MainWindow", "Always late to class                                                                                         "))
        self.label_46.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_47.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_50.setText(_translate("MainWindow", "Does not come to class often"))
        self.label_48.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_49.setText(_translate("MainWindow", "Always puntual to class"))
        self.label_72.setText(_translate("MainWindow", "Lecturer\'s Overall Effort for this course"))
        self.label_43.setText(_translate("MainWindow", "The lecturer demands gifts from students in order to give BETTER GRADES"))
        self.label_52.setText(_translate("MainWindow", "Shows good concerns for all students"))
        self.label_53.setText(_translate("MainWindow", "Uses variety of examples to illustrate a point"))
        self.label_54.setText(_translate("MainWindow", "Very knowledgeable of the subject matter"))
        self.label_55.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_63.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_64.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_65.setText(_translate("MainWindow", "Uses lecture time to tell glorifying stories"))
        self.label_66.setText(_translate("MainWindow", "Returns test grades back to students on time"))
        self.label_67.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_68.setText(_translate("MainWindow", "uses some modern technologies in teaching (projectors, power points and other audio Visual)"))
        self.label_69.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_70.setText(_translate("MainWindow", "Strongly Disagree"))
        self.label_71.setText(_translate("MainWindow", "Strongly Disagree"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recentCourseTab), _translate("MainWindow", "Course Grading"))
        self.label_26.setText(_translate("MainWindow", "Click a comment/recommendation to view Complete details"))
        item = self.commentTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.commentTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Comment"))
        item = self.commentTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Recommendation"))
        __sortingEnabled = self.commentTable.isSortingEnabled()
        self.commentTable.setSortingEnabled(False)
        item = self.commentTable.item(0, 0)
        item.setText(_translate("MainWindow", "the lecturer should always come to class early because in that does he get it right \\n"))
        item = self.commentTable.item(0, 1)
        item.setText(_translate("MainWindow", "the lecturer should always come to class early because in that does he get it right \\n"))
        self.commentTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recommndTab), _translate("MainWindow", "Recommendations and Comments"))
        self.prevBtn.setText(_translate("MainWindow", "Previous"))
        self.nextBtn.setText(_translate("MainWindow", "next"))
        self.label_94.setText(_translate("MainWindow", "Add Lecture Venue"))
        self.label_95.setText(_translate("MainWindow", "Lecture Venue Details"))
        self.label_96.setText(_translate("MainWindow", "Description:"))
        self.lectVenueDesc.setPlaceholderText(_translate("MainWindow", "Venue Description e.g NLR Room II"))
        self.label_97.setText(_translate("MainWindow", "School:"))
        self.lectSchList.setItemText(0, _translate("MainWindow", "Select School"))
        self.lectSchList.setItemText(1, _translate("MainWindow", "SET"))
        self.lectSchList.setItemText(2, _translate("MainWindow", "SEET"))
        self.lectSchList.setItemText(3, _translate("MainWindow", "SIPET"))
        self.lectSchList.setItemText(4, _translate("MainWindow", "SEMT"))
        self.lectSchList.setItemText(5, _translate("MainWindow", "SAAT"))
        self.lectSchList.setItemText(6, _translate("MainWindow", "SICT"))
        self.addVenue.setText(_translate("MainWindow", "Add Venue"))
        self.label_98.setText(_translate("MainWindow", "Lecture Venues"))
        self.label_89.setText(_translate("MainWindow", "Add Course"))
        self.label_90.setText(_translate("MainWindow", "Course Details"))
        self.label_91.setText(_translate("MainWindow", "Course Code:"))
        self.label_92.setText(_translate("MainWindow", "Course Name:"))
        self.courseCode.setPlaceholderText(_translate("MainWindow", "e.g MAT111"))
        self.courseName.setPlaceholderText(_translate("MainWindow", "e.g General Mathematics "))
        self.addCourseBtn.setText(_translate("MainWindow", "Add Course"))
        self.label_93.setText(_translate("MainWindow", "Course List"))
        self.label_78.setText(_translate("MainWindow", "Add Lecturer"))
        self.label_79.setText(_translate("MainWindow", "Personal Details"))
        self.label_80.setText(_translate("MainWindow", "Title:"))
        self.label_81.setText(_translate("MainWindow", "Fullname:"))
        self.lectFname.setPlaceholderText(_translate("MainWindow", "e.g Ibrahim M. Abdullahi"))
        self.lectTitleCombo.setItemText(0, _translate("MainWindow", "Select Title"))
        self.lectTitleCombo.setItemText(1, _translate("MainWindow", "Prof"))
        self.lectTitleCombo.setItemText(2, _translate("MainWindow", "Dr"))
        self.lectTitleCombo.setItemText(3, _translate("MainWindow", "Engr"))
        self.lectTitleCombo.setItemText(4, _translate("MainWindow", "Mr"))
        self.lectTitleCombo.addItems(["Mrs", "Miss"])
        self.label_82.setText(_translate("MainWindow", "Course Details"))
        self.label_83.setText(_translate("MainWindow", "Course 1:"))
        self.label_84.setText(_translate("MainWindow", "Course 2:"))
        self.label_85.setText(_translate("MainWindow", "Course 3"))
        self.label_86.setText(_translate("MainWindow", "Course 4"))
        self.label_87.setText(_translate("MainWindow", "Course 5"))
        self.course1.setItemText(0, _translate("MainWindow", "Select Course"))
        self.course2.setItemText(0, _translate("MainWindow", "Select Course"))
        self.course3.setItemText(0, _translate("MainWindow", "Select Course"))
        self.course4.setItemText(0, _translate("MainWindow", "Select Course"))
        self.course5.setItemText(0, _translate("MainWindow", "Select Course"))
        self.addLecturer.setText(_translate("MainWindow", "Add Lecturer"))
        self.label_88.setText(_translate("MainWindow", "Lecturers List"))
        self.label_73.setText(_translate("MainWindow", "Add Class Rep"))
        self.label_74.setText(_translate("MainWindow", "Class Rep Details"))
        self.label_75.setText(_translate("MainWindow", "Class Rep Username:"))
        self.cr_level.setItemText(0, _translate("MainWindow", "Select Level"))
        self.cr_level.setItemText(1, _translate("MainWindow", "100"))
        self.cr_level.setItemText(2, _translate("MainWindow", "200"))
        self.cr_level.setItemText(3, _translate("MainWindow", "300"))
        self.cr_level.setItemText(4, _translate("MainWindow", "400"))
        self.cr_level.setItemText(5, _translate("MainWindow", "500"))
        self.label_76.setText(_translate("MainWindow", "Level:"))
        self.cr_username.setItemText(0, _translate("MainWindow", "Select Class Rep"))
        self.addcrBtn.setText(_translate("MainWindow", "Add Class Rep"))
        self.label_77.setText(_translate("MainWindow", "Class Reps - Usernames"))
        self.groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))
        self.changeAccountBtn.setText(_translate("MainWindow", "Change Account"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Help"))
        self.helpBtn.setText(_translate("MainWindow", "iLecture Grading System Help"))
        self.aboutButton.setText(_translate("MainWindow", "About iLGS"))
        self.updateBtn.setText(_translate("MainWindow", "Check for Updates"))
        self.reportBtn.setText(_translate("MainWindow", "Report an Issue"))
        self.cr_list.setSortingEnabled(False)
        self.cr_list.setSortingEnabled(__sortingEnabled)
        self.nextBtn.clicked.connect(self.gotoNextIndex)
        self.prevBtn.clicked.connect(self.gotoPreviousIndex)

    def gotoNextIndex(self):
        x = self.stackedWidget_2.currentIndex()
        if x < 6:
            self.stackedWidget_2.setCurrentIndex(int(x + 1))

    def gotoPreviousIndex(self):
        x = self.stackedWidget_2.currentIndex()
        if x > 0:
            self.stackedWidget_2.setCurrentIndex(int(x - 1))

    def setActiveButton(self, btn):
        self.courseGrading.setStyleSheet("")
        self.manLecturerBtn.setStyleSheet("")
        self.manCoursesBtn.setStyleSheet("")
        self.manClassRepsBtn.setStyleSheet("")
        self.manLectHallBtn.setStyleSheet("")
        self.settingBtn.setStyleSheet("")
        btn.setStyleSheet("background-color: rgba(255, 0, 0, 0.1);\n"
            "color: #000000;\n"
            "border: 2px solid  #ffffff;")


class Mod_lectHall(QWidget):
    def __init__(self,  parent=None):
        super(Mod_lectHall, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 274)
        Dialog.setStyleSheet("\n"
            "QComboBox, QLineEdit {\n"
            "border-radius: 5px;\n"
            "border: 3px solid rgb(207, 207, 207);\n"
            "font: 12pt \"Consolas\";\n"
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
            "font-family: Comic Sans Ms;\n"
            "padding: 5px;\n"
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
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QRect(40, 40, 581, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)
        self.mod_desc = QLineEdit(self.gridLayoutWidget)
        self.mod_desc.setText("")
        self.mod_desc.setObjectName("mod_desc")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.mod_desc)
        self.mod_school = QComboBox(self.gridLayoutWidget)
        self.mod_school.setObjectName("mod_school")
        self.mod_school.addItem("")
        self.mod_school.addItem("")
        self.mod_school.addItem("")
        self.mod_school.addItem("")
        self.mod_school.addItem("")
        self.mod_school.addItem("")
        self.mod_school.addItem("")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mod_school)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(50, 10, 171, 31))
        self.label.setObjectName("label")
        self.rem_venue = QPushButton(Dialog)
        self.rem_venue.setGeometry(QRect(260, 200, 131, 41))
        self.rem_venue.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.rem_venue.setObjectName("rem_venue")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Description:"))
        self.label_3.setText(_translate("Dialog", "School:"))
        self.mod_school.setItemText(0, _translate("Dialog", "Select School"))
        self.mod_school.setItemText(1, _translate("Dialog", "SEET"))
        self.mod_school.setItemText(2, _translate("Dialog", "SICT"))
        self.mod_school.setItemText(3, _translate("Dialog", "SET"))
        self.mod_school.setItemText(4, _translate("Dialog", "SIPET"))
        self.mod_school.setItemText(5, _translate("Dialog", "SEMT"))
        self.mod_school.setItemText(6, _translate("Dialog", "SAAT"))
        self.label.setText(_translate("Dialog", "Modify Venue Details"))
        self.rem_venue.setText(_translate("Dialog", "Delete Venue"))


class Mod_Lecturer(QDialog):
    def __init__(self,  lect, courses, parent=None):
        titles = ["Prof", "Dr", "Engr", "Mr", "Mrs", "Miss"]
        super(Mod_Lecturer, self).__init__(parent)
        self.lect = lect
        self.courses = courses
        self.setupUi(self)
        self.setWindowTitle('{0}. {1} Modify Details'.format(self.lect[1], self.lect[2]))
        self.mod_fname.setText(self.lect[2])
        self.lect_courses = lect[3].split(",")
        lect_title_index = None
        for i in range(len(titles)):
            if self.lect[1] == titles[i]:
                lect_title_index = i + 1
        if lect_title_index is not None:
            self.mod_title.setCurrentIndex(lect_title_index)

        self.course_list = []
        for i in self.courses:
            self.course_list.append([i[2], i[0] + ' - ' + i[1]])
        self.mod_course1.addItems([x[1] for x in sorted(self.course_list)])
        self.mod_course2.addItems([x[1] for x in sorted(self.course_list)])
        self.mod_course3.addItems([x[1] for x in sorted(self.course_list)])
        self.mod_course4.addItems([x[1] for x in sorted(self.course_list)])
        self.mod_course5.addItems([x[1] for x in sorted(self.course_list)])
        
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 510)
        Dialog.setStyleSheet("\n"
            "QComboBox, QLineEdit {\n"
            "border-radius: 5px;\n"
            "border: 3px solid rgb(207, 207, 207);\n"
            "font: 12pt \"Consolas\";\n"
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
            "font-family: Comic Sans Ms;\n"
            "padding: 5px;\n"
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
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QRect(40, 40, 581, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)
        self.mod_title = QComboBox(self.gridLayoutWidget)
        self.mod_title.setObjectName("mod_title")
        self.mod_title.addItem("")
        self.mod_title.addItem("")
        self.mod_title.addItem("")
        self.mod_title.addItem("")
        self.mod_title.addItem("")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.mod_title)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)
        self.mod_fname = QLineEdit(self.gridLayoutWidget)
        self.mod_fname.setObjectName("mod_fname")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mod_fname)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)
        self.mod_course1 = QComboBox(self.gridLayoutWidget)
        self.mod_course1.setObjectName("mod_course1")
        self.mod_course1.addItem("")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mod_course1)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)
        self.mod_course2 = QComboBox(self.gridLayoutWidget)
        self.mod_course2.setObjectName("mod_course2")
        self.mod_course2.addItem("")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.mod_course2)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)
        self.mod_course3 = QComboBox(self.gridLayoutWidget)
        self.mod_course3.setObjectName("mod_course3")
        self.mod_course3.addItem("")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.mod_course3)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)
        self.mod_course4 = QComboBox(self.gridLayoutWidget)
        self.mod_course4.setObjectName("mod_course4")
        self.mod_course4.addItem("")
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.mod_course4)
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)
        self.mod_course5 = QComboBox(self.gridLayoutWidget)
        self.mod_course5.setObjectName("mod_course5")
        self.mod_course5.addItem("")
        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.mod_course5)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(50, 10, 171, 31))
        self.label.setObjectName("label")
        self.rem_lecturer = QPushButton(Dialog)
        self.rem_lecturer.setGeometry(QRect(280, 450, 131, 41))
        self.rem_lecturer.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.rem_lecturer.setObjectName("rem_lecturer")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        self.label_2.setText(_translate("Dialog", "Title"))
        self.mod_title.setItemText(0, _translate("Dialog", "Select Title"))
        self.mod_title.setItemText(1, _translate("Dialog", "Prof"))
        self.mod_title.setItemText(2, _translate("Dialog", "Dr"))
        self.mod_title.setItemText(3, _translate("Dialog", "Engr"))
        self.mod_title.setItemText(4, _translate("Dialog", "Mr"))
        self.mod_title.addItems(["Mrs", "Miss"])
        self.label_3.setText(_translate("Dialog", "Fname"))
        self.label_4.setText(_translate("Dialog", "Course Details"))
        self.label_5.setText(_translate("Dialog", "Course 1"))
        self.mod_course1.setItemText(0, _translate("Dialog", "Select Course"))
        self.label_6.setText(_translate("Dialog", "Course 2"))
        self.mod_course2.setItemText(0, _translate("Dialog", "Selet Course"))
        self.label_7.setText(_translate("Dialog", "Course 3"))
        self.mod_course3.setItemText(0, _translate("Dialog", "Select Course"))
        self.label_8.setText(_translate("Dialog", "Course 4"))
        self.mod_course4.setItemText(0, _translate("Dialog", "Select Course"))
        self.label_9.setText(_translate("Dialog", "Course 5"))
        self.mod_course5.setItemText(0, _translate("Dialog", "Select Course"))
        self.label.setText(_translate("Dialog", "Modify Lecturer"))
        self.rem_lecturer.setText(_translate("Dialog", "Remove Lecturer"))

    def loadCourseList(self, i, combo):
        try:
            lect_courses = []
            i = self.l_index[self.obj.lecturerCombo.currentIndex()]
            courses = ""
            for x in self.lect:
                if i == x[0]:
                    courses = x[3].split(",")
            
            for i in self.level_courses:
                if i[0] in courses:
                    lect_courses.append(i[0] + ' - ' + i[1])
            
            self.mod_c.clear()
            self.obj.courseCombo.addItem("Select Course")
            self.obj.courseCombo.addItems(lect_courses)
        except Exception as e:
            print(e)
            

class Mod_Course(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 274)
        Dialog.setStyleSheet("\n"
            "QComboBox, QLineEdit {\n"
            "border-radius: 5px;\n"
            "border: 3px solid rgb(207, 207, 207);\n"
            "font: 12pt \"Consolas\";\n"
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
            "font-family: Comic Sans Ms;\n"
            "padding: 5px;\n"
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
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QRect(40, 40, 581, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)
        self.mod_coursename = QLineEdit(self.gridLayoutWidget)
        self.mod_coursename.setObjectName("mod_coursename")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mod_coursename)
        self.mod_coursecode = QLineEdit(self.gridLayoutWidget)
        self.mod_coursecode.setObjectName("mod_coursecode")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.mod_coursecode)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(50, 10, 171, 31))
        self.label.setObjectName("label")
        self.removeCourse = QPushButton(Dialog)
        self.removeCourse.setGeometry(QRect(260, 200, 131, 41))
        self.removeCourse.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(255, 0, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.removeCourse.setObjectName("removeCourse")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Course Code:"))
        self.label_3.setText(_translate("Dialog", "Course Name:"))
        self.label.setText(_translate("Dialog", "Modify Course"))
        self.removeCourse.setText(_translate("Dialog", "Remove Course"))

