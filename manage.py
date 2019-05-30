from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ManageClassRep(object):
    def setupUi(self, centralwidget):
        
        self.widget = QWidget(centralwidget)
        self.widget.setGeometry(QRect(0, 10, 1101, 621))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(0, 20, 561, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 521, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(2, QFormLayout.FieldRole, spacerItem)
        self.cr_username = QLineEdit(self.verticalLayoutWidget)
        self.cr_username.setObjectName("cr_username")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cr_username)
        self.cr_level = QComboBox(self.verticalLayoutWidget)
        self.cr_level.setObjectName("cr_level")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.cr_level.addItem("")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cr_level)
        self.verticalLayout.addLayout(self.formLayout)
        self.addcrBtn = QPushButton(self.widget)
        self.addcrBtn.setGeometry(QRect(210, 260, 111, 41))
        self.addcrBtn.setObjectName("addcrBtn")
        self.line = QFrame(self.widget)
        self.line.setGeometry(QRect(573, 10, 20, 581))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QLabel(self.widget)
        self.label_11.setGeometry(QRect(660, 10, 341, 41))
        self.label_11.setObjectName("label_11")
        self.cr_list = QListWidget(self.widget)
        self.cr_list.setGeometry(QRect(600, 50, 481, 481))
        self.cr_list.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.cr_list.setObjectName("cr_list")
        item = QListWidgetItem()
        self.cr_list.addItem(item)
        centralwidget.raise_()
        
        self.retranslateUi(centralwidget)
        QMetaObject.connectSlotsByName(centralwidget)

    def retranslateUi(self, centralwidget):
        _translate = QCoreApplication.translate
        self.label.setText(_translate("centralwidget", "Add Class Rep"))
        self.label_5.setText(_translate("centralwidget", "Class Rep Details"))
        self.label_4.setText(_translate("centralwidget", "Class Rep Username:"))
        self.label_2.setText(_translate("centralwidget", "Level:"))
        self.cr_level.setItemText(0, _translate("centralwidget", "Select Level"))
        self.cr_level.setItemText(1, _translate("centralwidget", "100"))
        self.cr_level.setItemText(2, _translate("centralwidget", "200"))
        self.cr_level.setItemText(3, _translate("centralwidget", "300"))
        self.cr_level.setItemText(4, _translate("centralwidget", "400"))
        self.cr_level.setItemText(5, _translate("centralwidget", "500"))
        self.addcrBtn.setText(_translate("centralwidget", "Add Class Rep"))
        self.label_11.setText(_translate("centralwidget", "Class Reps - Usernames"))
        __sortingEnabled = self.cr_list.isSortingEnabled()
        self.cr_list.setSortingEnabled(False)
        item = self.cr_list.item(0)
        item.setText(_translate("centralwidget", "100Level - indresilt234"))
        self.cr_list.setSortingEnabled(__sortingEnabled)


class ManageCourse(object):
    def setupUi(self, centralwidget):
       
        self.widget = QWidget(centralwidget)
        self.widget.setGeometry(QRect(0, 10, 1101, 621))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(0, 20, 561, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 521, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(2, QFormLayout.FieldRole, spacerItem)
        self.courseCode = QLineEdit(self.verticalLayoutWidget)
        self.courseCode.setObjectName("courseCode")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.courseCode)
        self.courseName = QLineEdit(self.verticalLayoutWidget)
        self.courseName.setObjectName("courseName")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.courseName)
        self.verticalLayout.addLayout(self.formLayout)
        self.addCourseBtn = QPushButton(self.widget)
        self.addCourseBtn.setGeometry(QRect(210, 260, 111, 41))
        self.addCourseBtn.setObjectName("addCourseBtn")
        self.line = QFrame(self.widget)
        self.line.setGeometry(QRect(573, 10, 20, 581))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QLabel(self.widget)
        self.label_11.setGeometry(QRect(660, 10, 341, 41))
        self.label_11.setObjectName("label_11")
        self.courseList = QListWidget(self.widget)
        self.courseList.setGeometry(QRect(600, 50, 481, 481))
        self.courseList.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.courseList.setObjectName("courseList")
        item = QListWidgetItem()
        self.courseList.addItem(item)
        

        self.retranslateUi(centralwidget)
        QMetaObject.connectSlotsByName(centralwidget)

    def retranslateUi(self, centralwidget):
        _translate = QCoreApplication.translate
        centralwidget.setWindowTitle(_translate("centralwidget", "centralwidget"))
        self.label.setText(_translate("centralwidget", "Add Course"))
        self.label_5.setText(_translate("centralwidget", "Course Details"))
        self.label_4.setText(_translate("centralwidget", "Course Code:"))
        self.label_2.setText(_translate("centralwidget", "Course Name:"))
        self.addCourseBtn.setText(_translate("centralwidget", "Add Course"))
        self.label_11.setText(_translate("centralwidget", "Course List"))
        __sortingEnabled = self.courseList.isSortingEnabled()
        self.courseList.setSortingEnabled(False)
        item = self.courseList.item(0)
        item.setText(_translate("centralwidget", "100Level - indresilt234"))
        self.courseList.setSortingEnabled(__sortingEnabled)



class ManageLecturer(object):
    def setupUi(self, centralwidget):
        
        self.widget = QWidget(centralwidget)
        self.widget.setGeometry(QRect(0, 0, 1101, 621))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(0, 20, 561, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 521, 369))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)
        self.lectFname = QLineEdit(self.verticalLayoutWidget)
        self.lectFname.setObjectName("lectFname")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lectFname)
        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)
        self.course1 = QLineEdit(self.verticalLayoutWidget)
        self.course1.setObjectName("course1")
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.course1)
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)
        self.course2 = QLineEdit(self.verticalLayoutWidget)
        self.course2.setObjectName("course2")
        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.course2)
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_8)
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_9)
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_10)
        self.course3 = QLineEdit(self.verticalLayoutWidget)
        self.course3.setObjectName("course3")
        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.course3)
        self.course4 = QLineEdit(self.verticalLayoutWidget)
        self.course4.setObjectName("course4")
        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.course4)
        self.course5 = QLineEdit(self.verticalLayoutWidget)
        self.course5.setObjectName("course5")
        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.course5)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.addLecturer = QPushButton(self.widget)
        self.addLecturer.setGeometry(QRect(190, 460, 111, 41))
        self.addLecturer.setObjectName("addLecturer")
        self.line = QFrame(self.widget)
        self.line.setGeometry(QRect(573, 10, 20, 581))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QLabel(self.widget)
        self.label_11.setGeometry(QRect(660, 10, 341, 41))
        self.label_11.setObjectName("label_11")
        self.lecturerList = QListWidget(self.widget)
        self.lecturerList.setGeometry(QRect(600, 50, 481, 481))
        self.lecturerList.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.lecturerList.setObjectName("lecturerList")
        item = QListWidgetItem()
        self.lecturerList.addItem(item)
        

        self.retranslateUi(centralwidget)
        QMetaObject.connectSlotsByName(centralwidget)

    def retranslateUi(self, centralwidget):
        _translate = QCoreApplication.translate
        self.label.setText(_translate("centralwidget", "Add Lecturer"))
        self.label_5.setText(_translate("centralwidget", "Personal Details"))
        self.label_4.setText(_translate("centralwidget", "Title:"))
        self.label_2.setText(_translate("centralwidget", "Fullname:"))
        self.comboBox.setItemText(0, _translate("centralwidget", "Select Title"))
        self.comboBox.setItemText(1, _translate("centralwidget", "Prof"))
        self.comboBox.setItemText(2, _translate("centralwidget", "Dr"))
        self.comboBox.setItemText(3, _translate("centralwidget", "Engr"))
        self.comboBox.setItemText(4, _translate("centralwidget", "Mr"))
        self.label_3.setText(_translate("centralwidget", "Course Details"))
        self.label_6.setText(_translate("centralwidget", "Course 1:"))
        self.label_7.setText(_translate("centralwidget", "Course 2:"))
        self.label_8.setText(_translate("centralwidget", "Course 3"))
        self.label_9.setText(_translate("centralwidget", "Course 4"))
        self.label_10.setText(_translate("centralwidget", "Course 5"))
        self.addLecturer.setText(_translate("centralwidget", "Add Lecturer"))
        self.label_11.setText(_translate("centralwidget", "Lecturers List"))
        __sortingEnabled = self.lecturerList.isSortingEnabled()
        self.lecturerList.setSortingEnabled(False)
        item = self.lecturerList.item(0)
        item.setText(_translate("centralwidget", "100Level - indresilt234"))
        self.lecturerList.setSortingEnabled(__sortingEnabled)

class ManageLectHall(object):
    def setupUi(self, centralwidget):
        
        self.widget = QWidget(centralwidget)
        self.widget.setGeometry(QRect(0, 10, 1101, 621))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QLabel(self.widget)
        self.label.setGeometry(QRect(0, 20, 561, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-bottom: 2px solid rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 521, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(2, QFormLayout.FieldRole, spacerItem)
        self.lectVenueDesc = QLineEdit(self.verticalLayoutWidget)
        self.lectVenueDesc.setObjectName("lectVenueDesc")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lectVenueDesc)
        self.lectSchList = QComboBox(self.verticalLayoutWidget)
        self.lectSchList.setObjectName("lectSchList")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.lectSchList.addItem("")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lectSchList)
        self.verticalLayout.addLayout(self.formLayout)
        self.addcrBtn = QPushButton(self.widget)
        self.addcrBtn.setGeometry(QRect(210, 260, 111, 41))
        self.addcrBtn.setObjectName("addcrBtn")
        self.line = QFrame(self.widget)
        self.line.setGeometry(QRect(573, 10, 20, 581))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QLabel(self.widget)
        self.label_11.setGeometry(QRect(660, 10, 341, 41))
        self.label_11.setObjectName("label_11")
        self.cr_list = QListWidget(self.widget)
        self.cr_list.setGeometry(QRect(600, 50, 481, 481))
        self.cr_list.setStyleSheet("font: 11pt \"Consolas\";\n"
"border-left: 3px solid rgb(0, 85, 0)")
        self.cr_list.setObjectName("cr_list")
        item = QListWidgetItem()

        self.retranslateUi(centralwidget)
        QMetaObject.connectSlotsByName(centralwidget)

    def retranslateUi(self, centralwidget):
        _translate = QCoreApplication.translate
        self.label.setText(_translate("centralwidget", "Add Lecture Venue"))
        self.label_5.setText(_translate("centralwidget", "Lecture Venue Details"))
        self.label_4.setText(_translate("centralwidget", "Description:"))
        self.label_2.setText(_translate("centralwidget", "School:"))
        self.lectSchList.setItemText(0, _translate("centralwidget", "Select School"))
        self.lectSchList.setItemText(1, _translate("centralwidget", "SET"))
        self.lectSchList.setItemText(2, _translate("centralwidget", "SEET"))
        self.lectSchList.setItemText(3, _translate("centralwidget", "SIPET"))
        self.lectSchList.setItemText(4, _translate("centralwidget", "SEMT"))
        self.lectSchList.setItemText(5, _translate("centralwidget", "SAAT"))
        self.lectSchList.setItemText(6, _translate("centralwidget", "SICT"))
        self.addcrBtn.setText(_translate("centralwidget", "Add Class Rep"))
        self.label_11.setText(_translate("centralwidget", "Lecture Venues"))
        __sortingEnabled = self.cr_list.isSortingEnabled()
        self.cr_list.setSortingEnabled(False)
        item = self.cr_list.item(0)
        # item.setText(_translate("centralwidget", "NLR1 - SAAT"))
        self.cr_list.setSortingEnabled(__sortingEnabled)
