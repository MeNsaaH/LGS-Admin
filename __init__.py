from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from auth import Auth
from views import Home, Mod_Lecturer, Mod_Course, Mod_lectHall
from about import About
import qrc_resource


success_config = pyqtSignal()


class Loading(QMainWindow):
    def __init__(self, parent=None, width = 0, height = 0):
        super(Loading, self).__init__(parent)
        self.width = width
        self.height = height
        self.auth = Auth()
        self.settings = QSettings()
        # self.settings.clear()
        if self.settings.value("Dept") is not None and self.settings.value("School"):
            print(self.settings.value("Dept"))
            startApp(width, height)
        else:
            self.setupUi(self)
            self.contBtn.clicked.connect(self.proceed)
            self.backBtn.clicked.connect(self.receed)
            self.schoolList.currentIndexChanged.connect(self.loadDepts)
            self.proceedBtn.clicked.connect(self.configureApp)
            self.show()
        
        self.setWindowTitle("iLecture Grading System")
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 576)
        MainWindow.setStyleSheet("QComboBox, QLineEdit {\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QLabel(self.page)
        self.label_7.setText("")
        self.label_7.setPixmap(QPixmap(":/futminna"))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QLabel(self.page)
        # self.label_8.setPixmap(QPixmap(":/futminna"))
        self.label_8.setStyleSheet("font: 16pt \"Comic Sans MS\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.textBrowser = QTextBrowser(self.page)
        self.textBrowser.setStyleSheet("font: 12pt \"Menlo\";")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_6)
        self.schoolList = QComboBox(self.page)
        self.schoolList.setObjectName("schoolList")
        self.schoolList.addItem("")
        self.schoolList.addItem("")
        self.schoolList.addItem("")
        self.schoolList.addItem("")
        self.schoolList.addItem("")
        self.schoolList.addItem("")
        self.schoolList.addItem("")
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.schoolList)
        self.deptList = QComboBox(self.page)
        self.deptList.setObjectName("deptList")
        self.deptList.addItem("")
        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.deptList)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.contBtn = QPushButton(self.page)
        self.contBtn.setStyleSheet("padding: 20%;")
        self.contBtn.setObjectName("contBtn")
        self.horizontalLayout_4.addWidget(self.contBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setText("")
        self.label_9.setPixmap(QPixmap(":/futminna"))
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setStyleSheet("font: 16pt \"Comic Sans MS\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.schoolLabel = QLabel(self.page_2)
        self.schoolLabel.setStyleSheet("font: 12pt \"Goudy Stout\";")
        self.schoolLabel.setAlignment(Qt.AlignCenter)
        self.schoolLabel.setObjectName("schoolLabel")
        self.verticalLayout_6.addWidget(self.schoolLabel)
        spacerItem10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.deptLabel = QLabel(self.page_2)
        self.deptLabel.setStyleSheet("font: 12pt \"Goudy Stout\";")
        self.deptLabel.setAlignment(Qt.AlignCenter)
        self.deptLabel.setObjectName("deptLabel")
        self.verticalLayout_6.addWidget(self.deptLabel)
        spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem11)
        spacerItem12 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.backBtn = QPushButton(self.page_2)
        self.backBtn.setStyleSheet("padding: 20%;")
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout_6.addWidget(self.backBtn)
        spacerItem13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.proceedBtn = QPushButton(self.page_2)
        self.proceedBtn.setStyleSheet("padding: 20%;")
        self.proceedBtn.setObjectName("proceedBtn")
        self.horizontalLayout_6.addWidget(self.proceedBtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 897, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "iLecture Grading System"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Menlo\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The iLecture Grading System (LGS) is a software that allows students to communicate their feelings and gradings about their lecturers in order to procure optimum understanding of field of study.</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "School"))
        self.label_6.setText(_translate("MainWindow", "Department"))
        self.schoolList.setItemText(0, _translate("MainWindow", "Select School"))
        self.schoolList.setItemText(1, _translate("MainWindow", "School of Agriculture and Agricultural Technology (SAAT)"))
        self.schoolList.setItemText(2, _translate("MainWindow", "School of Electrical Engineering Technology (SEET)"))
        self.schoolList.setItemText(3, _translate("MainWindow", "School of Entrepreneurship and Management Technology (SEMT)"))
        self.schoolList.setItemText(4, _translate("MainWindow", "School of Environmental Technology (SET)"))
        self.schoolList.setItemText(5, _translate("MainWindow", "School of Industrial and Processing Engineering Technology (SIPET)"))
        self.schoolList.setItemText(6, _translate("MainWindow", "School of Information and Communications Technology (SICT)"))
        self.deptList.setItemText(0, _translate("MainWindow", "Select Department"))
        self.contBtn.setText(_translate("MainWindow", "Continue"))
        self.label_10.setText(_translate("MainWindow", "iLecture Grading System"))
        self.schoolLabel.setText(_translate("MainWindow", "School of Electrical Engineering Technology"))
        self.deptLabel.setText(_translate("MainWindow", "Computer Engineering Department"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.proceedBtn.setText(_translate("MainWindow", "Proceed and Start"))

    def proceed(self):
        if self.schoolList.currentIndex() == 0:
            QMessageBox.warning(self, 'Select School', "Select a school to proceed")
            return
        if self.deptList.currentIndex() == 0:
            QMessageBox.warning(self, "Select Dept", 'Select a Department to proceed')
            return
        self.school = self.schoolList.currentText()
        self.dept = self.deptList.currentText()
        self.schoolLabel.setText(self.school)
        self.deptLabel.setText('Department of ' + self.dept)
        self.stackedWidget.setCurrentIndex(1)

    def receed(self):
        self.stackedWidget.setCurrentIndex(0)

    def loadDepts(self):
        depts = {'1': ['Soil Science', 'Crop Production'],
                '2': ['Computer Engineering', 'Electrical Engineering', 'Mechatronics Engineering', 'Telecommunications Engineering'],
                '3': ['EBS', 'Transport Management', 'Project Management'],
                '4': ['Architecture', 'Building', 'Estate Management', 'Quantity Survey'],
                '5': ['Chemical Engineering', 'Civil Engineering', 'Mechanical Engineering',  'Agric and Bio-Resources', 'Metallurgical'],
                '6': ['Computer Science', 'Cyber Security', 'Info and Media Tech']}
        index = self.schoolList.currentIndex()
        dept = ['Select Dept'] + sorted(depts[str(index)])
        self.deptList.clear()
        self.deptList.addItems(dept)

    def configureApp(self):
        if self.auth.initializeApp(self.school, self.dept):
            self.settings.setValue("Dept", self.dept)
            self.settings.setValue("School", self.school)
            self.close()
            startApp(self.width, self.height)
        else:
            QMessageBox.critical(self, "Error", "Could not Setup up app for usage, Please Try again later."
                                " If problem persists consult the administrator")
            self.close()


class App(QMainWindow):
    def __init__(self, parent=None, width = 0, height = 0):
        super(App, self).__init__(parent)
        self.home = Home()
        self.resize(width, height)
        # self.showMaximized()
        self.home.setupUi(self)
        try:
            self.auth = Auth(self.home, self)
        except TypeError:
            settings = QSettings()
            settings.clear()
            QMessageBox.warning(parent, "Error", "Your Application Data is Corrupted, Restart the application")
            sys.exit()
        self.home.manLecturerBtn.clicked.connect(self.manLecturePage)
        self.home.manCoursesBtn.clicked.connect(self.manCoursePage)
        self.home.manLectHallBtn.clicked.connect(self.manLectHallPage)
        self.home.manClassRepsBtn.clicked.connect(self.manClassRepPage)
        self.home.courseGrading.clicked.connect(self.viewGradingPage)
        self.home.getGrading.clicked.connect(self.getRecentGrades)
        self.home.chngResource.clicked.connect(self.getCumulatedGrades)
        self.home.levelCombo.currentIndexChanged.connect(self.loadLecturers)
        self.home.lecturerCombo.currentIndexChanged.connect(self.loadCourseList)
        self.home.cr_level.currentIndexChanged.connect(self.loadcr)
        self.home.cr_list.itemDoubleClicked.connect(self.update_cr)
        self.home.lectList.itemDoubleClicked.connect(self.update_lect)
        self.home.aboutButton.clicked.connect(self.dispAbout)
        self.home.settingBtn.clicked.connect(self.settingsPage)
        
    def manLecturePage(self):
        self.home.setActiveButton(self.home.manLecturerBtn)
        self.home.stackedWidget.setCurrentIndex(4)
        self.auth.manLecturers(f='init')
        self.home.addLecturer.clicked.connect(self.auth.manLecturers)

    def manLectHallPage(self):
        self.home.setActiveButton(self.home.manLectHallBtn)
        self.home.stackedWidget.setCurrentIndex(2)
        self.auth.loadLectHall()
        self.home.addVenue.clicked.connect(self.auth.addLectHall)

    def manCoursePage(self):
        self.home.setActiveButton(self.home.manCoursesBtn)
        self.home.stackedWidget.setCurrentIndex(3)
        self.auth.loadCourse()
        self.home.addCourseBtn.clicked.connect(self.auth.addCourse)

    def manClassRepPage(self):
        self.home.setActiveButton(self.home.manClassRepsBtn)
        self.home.stackedWidget.setCurrentIndex(5)
        self.auth.loadcr()
        self.home.addcrBtn.clicked.connect(self.auth.addcr)

    def viewGradingPage(self):
        self.home.setActiveButton(self.home.courseGrading)
        self.home.stackedWidget.setCurrentIndex(1)

    def settingsPage(self):
        self.home.setActiveButton(self.home.settingBtn)
        self.home.stackedWidget.setCurrentIndex(6)

    def loadCourseList(self):
        self.auth.loadCourseList()

    def loadLecturers(self):
        self.auth.loadLecturers()

    def loadcr(self):
        self.auth.loadcr(l='input')

    def getRecentGrades(self):
        self.auth.getGrades(t = "r")

    def getCumulatedGrades(self):
        self.auth.getGrades(t = "c")
    
    def addLecturers(self):
        self.auth.addLecturers()

    def update_cr(self):
        self.auth.update_cr()

    def update_lect(self):
        index = self.home.lectList.currentRow()
        modLect = Mod_Lecturer(self.auth.lect[index], self.auth.courses, self)
        # mod_cr = modClassRep.Mod_cr()
        modLect.exec_()
        self.close()
        self.auth.update_lect()

    def update_course(self):
        modCourse = modCourse.Mod_Course()

    def dispAbout(self):
        x = About()
        x.exec_()
        
def startApp(width, height):
    a = App(width = width, height = height)
    a.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("iLecture Grading System")
    app.setOrganizationName("Computer Engineering Department FUT Minna")
    width = app.desktop().availableGeometry().width()
    height = app.desktop().availableGeometry().height()
    width -= width * 5/100
    height -= height * 5/100
    icon = QIcon()
    icon.addPixmap(QPixmap(":/futminna"), QIcon.Normal, QIcon.Off)
    app.setWindowIcon(icon)
    x = Loading(width = width, height =  height - 10)
    app.exec_()


    # app.exec_()