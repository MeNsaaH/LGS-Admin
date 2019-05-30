from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from string import ascii_uppercase, ascii_lowercase, digits
from database import Database
from exceptions import ConnectionError
import sys


class Auth(QObject):
    """
    Authenticates an email
    """
    DB_NAME = "../LectureGS.db"
    lect_added = False
    course_added = False
    lectHall_added = False
    cr_added = False
    
    def __init__(self, obj = None, parent  = None):
        super(Auth, self).__init__(parent)
        try:
            self.db = Database(self.DB_NAME)
            if obj is not None:
                self.parent = parent
                self.grade_indices = [i for i in ascii_lowercase][:-1]
                self.obj = obj
                self.createData()
        except ConnectionError as e:
            settings = QSettings()
            settings.clear()
            QMessageBox.critical(parent, "Connection Error", "Could not Connect to server to start app, Check your connection and try again later")
            sys.exit()

    def initializeApp(self, school, department):
        try:
            x = self.db.initializeApp(school, department)
            if x:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
        
    def createData(self):
        self.lect, self.halls, self.courses = self.getFullDetails()
        self.lecturers = []
        for i in self.lect:
            self.lecturers.append([i[0], i[1] + '. ' + i[2]])
        self.course_list = []
        lect_courses = []
        for i in self.courses:
            self.course_list.append([i[2], i[0] + ' - ' + i[1]])
    
    def isClassRep(self, s_id):
        return self.db.userExists([s_id], ["student_id"], "ClassReps")

    
    def getPreviousGrades(self, id):
        previousGrades = self.db.getRow("Gradings", ["student_id"], [id])
        return previousGrades

    def loadPreviousGrades(self, this):
        stat, self.previousGrades = self.getPreviousGrades(self.user["id"])
        
        if stat:
            this.tableWidget.setColumnCount(2)
            if len(self.previousGrades) >=  1:
                this.tableWidget.setRowCount(len(list(self.previousGrades.values())[0]))
            this.tableWidget.setHorizontalHeaderLabels(["Course", "Time"])
            this.tableWidget.setAlternatingRowColors(True)
            this.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
            this.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
            this.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
            item = col = None
            
            for i in self.previousGrades:
                row = len(list(self.previousGrades.values())[0]) - 1
                for x in self.previousGrades[i]:
                    item = QTableWidgetItem('%s' % x)
                    avail = False
                    if i == "course_code":
                        col = 0
                        avail = True
                        
                    if i == 'time':
                        col = 1
                        avail = True
                    if avail:
                        this.tableWidget.setItem(row, col, item)
                        row -= 1

    
    def getFullDetails(self, level = False):
        try:
            i = True
            j = True
            k = True
            lect_details = None
            lecture_env = None
            courses = None

            if level:
                k, courses = self.db.getRows("Courses", ['course_code', 'description'], ['level'], [level], withWhere = True)
            else:
                i, lect_details = self.db.getRows("Lecturers")
                j, lecture_env = self.db.getRows("LectureEnv", ['id', "description", 'school'])
                k, courses = self.db.getRows("Courses", ['course_code', 'description', 'level'])
            
               
            if i and j and k:
                return lect_details, lecture_env, courses
            return False, None, None
        except Exception as e:
            raise e

    def getGrades(self, t = 'c'):
        error = None
        if self.obj.levelCombo.currentIndex() == 0:
            error = "Select Level"
        
        if self.obj.courseCombo.currentIndex() == 0:
            error = "Select Course"

        if self.obj.lecturerCombo.currentIndex() == 0:
            error = "Select Lecturer"
        if error is not None:
            QMessageBox.warning(self.parent, "Error", error)
            return
        self.obj.stackedWidget_2.setCurrentIndex(0)
        lect_id = self.l_index[self.obj.lecturerCombo.currentIndex()]
        for i in self.lect:
            if lect_id == i[0]:
                db_name = i[5]
        
        course = self.obj.courseCombo.currentText()[:6]
        
        try:
            if t == 'r':
                course += '_r'
            fields = self.grade_indices + ["time", "no_graded", "lecture_env_id", "no_lectures", 'rating_id']
            x, grades = self.db.getRows(db_name, fields, ['course'], [course], withWhere = True)
            
            details = grades[0][25:]
            grades = grades[0][:25]
            
            venue = ''
            for x in self.halls:
                if x[0] == details[2]:
                    venue = x[1]
            self.obj.course_name.setText(self.obj.courseCombo.currentText())
            self.obj.no_lectures.setText(str(details[3]))
            self.obj.lect_hall.setText(venue)
            self.obj.lect_fname.setText(self.obj.lecturerCombo.currentText())
            self.obj.ave_no_students.setText(str(details[1]))
            self.obj.lect_time.setText(details[0])
            grades = [i + 2 for i in grades]
            
            self.layoutItems(self.obj.gridLayout, grades[:4])
            self.layoutItems(self.obj.gridLayout_2, grades[4:11])
            self.layoutItems(self.obj.gridLayout_3, grades[11:14])
            self.layoutItems(self.obj.gridLayout_5, grades[14:18])
            self.layoutItems(self.obj.gridLayout_7, grades[18:])
            if t == 'r':
                x, data = self.db.getRows("Gradings", ['lectComment', 'recommendations'], ['lecturer_id', 'course_code', 'rating_id'], [lect_id, course[:6], details[4]], withWhere = True)
                self.obj.getGrading.setStyleSheet("background-color: rgba(255, 0, 0, 0.1);\n"
                "color: #000000;\n border: 2px solid  #ffffff; \n padding: 2px;")
                self.obj.chngResource.setStyleSheet("")
            else:
                x, data = self.db.getRows("Gradings", ['lectComment', 'recommendations'], ['lecturer_id', 'course_code'], [lect_id, course[:6]], withWhere = True)
                self.obj.chngResource.setStyleSheet("background-color: rgba(255, 0, 0, 0.1);\n"
                "color: #000000;\n border: 2px solid  #ffffff;")
                self.obj.getGrading.setStyleSheet("")
            
            self.obj.commentTable.setRowCount(len(data))
            for i in range(len(data)):
                
                self.obj.commentTable.setItem(i, 0, QTableWidgetItem(data[i][0]))
                self.obj.commentTable.setItem(i, 1, QTableWidgetItem(data[i][1]))
            
            
        except Exception as e:
            QMessageBox.warning(self.parent, "Error", "Could not retrieve Lecturer Grading, Try again later")
            raise(e)


    def loadCourseList(self):
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
            
            self.obj.courseCombo.clear()
            self.obj.courseCombo.addItem("Select Course")
            self.obj.courseCombo.addItems(lect_courses)
        except Exception as e:
            print(e)

    def loadLecturers(self):
        try:
            level = (self.obj.levelCombo.currentIndex()) * 100
            _, _, self.level_courses = self.getFullDetails(level)
            
            level_lecturers = []
            self.l_index = [0]
            self.lect_levels = [i[4].split(',') for i in self.lect]
            
            for i, x in enumerate(self.lect_levels):
                if str(level) in x:
                    level_lecturers.append(self.lecturers[i])
                    self.l_index.append(self.lect[i][0])
            self.obj.lecturerCombo.clear()
            self.obj.lecturerCombo.addItem("Select Lecturer")
            self.obj.lecturerCombo.addItems([x[1] for x in level_lecturers])
            self.obj.courseCombo.clear()
            self.obj.courseCombo.addItem("Select Course")
            self.obj.courseCombo.addItems([x[0] + ' - ' + x[1] for x in sorted(self.level_courses)])
            
        except Exception as e:
            raise(e)

    def layoutItems(self, layout, values):
        grade = ["Strongly Disagree", "Disagree", "Don't Know", "Agree", "Strongly Agree"]
        
        wid_obj_name, widgets = self.layouts(layout, QLabel, "grade_")
        
        for i in range(len(wid_obj_name)):
            widgets[wid_obj_name[i][1]].setText(grade[values[i]])

    def layouts(self, layout, q_wid, search=""):
        widgets = []
        wid_obj_name = []
        j = 0
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, q_wid):
                if widget.objectName().startswith(search):
                    wid_obj_name.append([widget.objectName(), j])
                    widgets.append(widget)
                    j += 1
        return sorted(wid_obj_name), widgets

    def getChildren(self, parent, childWidget):
        return parent.findChildren(childWidget)

    def manLecturers(self, f='add'):
       

        if f == 'init':
            if not self.lect_added:
                self.obj.lectList.addItems([x[1] for x in self.lecturers])
                self.lect_added = True
            _, field = self.layouts(self.obj.formLayout_3, QComboBox, 'course')
            for i in field:
                i.addItems([i[1] for i in sorted(self.course_list)])
            return
        error = None

        fname = self.obj.lectFname.text()
        title = self.obj.lectTitleCombo.currentText()

        if not " " in fname:
            error = "Fullname must be atleast two names {Surname Firstname othernames[optional]}"

        if self.obj.lectTitleCombo.currentIndex() == 0:
            error = "Select Title from dropdown list"

        
        if error is not None:
            QMessageBox.warning(self.parent, "Error", error)
            return
        
        _, inputs = self.layouts(self.obj.formLayout_3, QComboBox, 'course')
        
        a = []
        levels = []
        for i in range(len(inputs)):
            index = inputs[i].currentIndex()
            course_code = sorted(self.course_list)[index-1][1][:6]
            if index != 0:
                if index in a:
                    QMessageBox.warning(self.parent, 'Selection Duplicate', 'Course {0}'\
                        ' already exist in previous course inputs'.format(course_code))
                    return
                a.append([inputs[i].currentIndex(), sorted(self.course_list)[index-1][1][:6]])
                level = str(int(course_code[3]) * 100)
                if level not in levels:
                    levels.append(level)
        dont_proceed = True
        if len(a) < 1:
            QMessageBox.question(self.parent, "Warning", 
                "No course has being assigned to {0}, \nDo You want to Proceed?".format(title + '. ' + fname))
            if not QMessageBox.Yes:
                return
            else:
                dont_proceed = False
        
        courses = ','.join([i[1] for i in a])
        levels = ','.join(levels)
        if len(self.lect)<1:
            new_db_index = 0
        else:
            new_db_index = int(self.lect[len(self.lect)-1][5][13:]) + 1
        db_name = 'CPE_Lecturer_' + str(new_db_index)
        params = "`id` INTEGER PRIMARY KEY AUTOINCREMENT, `course` TEXT UNIQUE, `a` INTEGER DEFAULT 0,"\
                " `b` INTEGER DEFAULT 0, `c` INTEGER DEFAULT 0, `d` INTEGER DEFAULT 0, `e` INTEGER DEFAULT 0,"\
                " `f` INTEGER DEFAULT 0, `g` INTEGER DEFAULT 0, `h` INTEGER DEFAULT 0, `i` INTEGER DEFAULT 0,"\
                " `j` INTEGER DEFAULT 0, `k` INTEGER DEFAULT 0, `l` INTEGER DEFAULT 0, `m` INTEGER DEFAULT 0, "\
                "`n` INTEGER DEFAULT 0, `o` INTEGER DEFAULT 0, `p` INTEGER DEFAULT 0, `q` INTEGER DEFAULT 0,"\
                " `r` INTEGER DEFAULT 0, `s` INTEGER DEFAULT 0, `t` INTEGER DEFAULT 0, `u` INTEGER DEFAULT 0,"\
                " `v` INTEGER DEFAULT 0, `w` INTEGER DEFAULT 0, `x` INTEGER DEFAULT 0, `y` INTEGER DEFAULT 0,"\
                " `rating_id` TEXT, `time` TEXT, `no_graded` INTEGER DEFAULT 0, `lecture_env_id` INTEGER,"\
                " `no_lectures` INTEGER DEFAULT 0, `validate` INTEGER DEFAULT 0 "
        try:
            x, error = self.db.createTable(db_name, params)
            y, err = self.db.addRow('Lecturers', ['title', 'fname', 'courses', 'levels', 'db_name'], 
                                                    [title, fname, courses, levels, db_name])
            for i in a:
                s1, err1 = self.db.addRow(db_name, ['course'], [i[1]])
                s2, err2 = self.db.addRow(db_name, ['course'], [i[1] + '_r'])
            if not dont_proceed:
                s1 = s2 = True

            if x and y and ((s1 and s2) or proceed):
                QMessageBox.information(self.parent, 'Success', "A New Lecturer has being successfully added")
                self.refresh()
                fname = self.obj.lectFname.setText("")
                title = self.obj.lectTitleCombo.setCurrentIndex(0)
                self.manLecturers(f='init')
                return
        except Exception as e:
            raise(e)

    def refresh(self):
        self.lect, self.halls, self.courses = self.getFullDetails()
        self.lect_added = False
        self.course_added = False
        self.lectHall_added = False
        self.cr_added = False
        self.obj.cr_username.clear()
        self.obj.lectList.clear()
        self.obj.courseList.clear()
        self.obj.cr_list.clear()
        _, inputs = self.layouts(self.obj.formLayout_3, QComboBox, 'course')
        for i in inputs:
            i.clear()
            i.addItem("Select Course")
        self.createData()
        
    def loadCourse(self):
        if not self.course_added:
            self.obj.courseList.addItems([i[1] for i in sorted(self.course_list)])
            self.course_added = True

    def loadLectHall(self):
        if not self.lectHall_added:
            self.obj.lectVenueList.clear()
            self.obj.lectVenueList.addItems([i[1] + ' - ' + i[2] for i in sorted(self.halls)])
            self.lectHall_added = True

    def addCourse(self):
        course_name = self.obj.courseName.text()
        course_code = self.obj.courseCode.text()
        error = None 
        if len(course_code) < 1 or len(course_name) < 1:
            error = "All Fields must be filled"
        if len(course_code) != 6:
            error = "Course code must be six character length e.g CPE111"
        if int(course_code[3]) > 5:
            error = "Course code first digit must represent the level, Invalid level {0}".format(course_code[3])
        if error is not None:
            QMessageBox.warning(self.parent, header, error)
            return
            
        level = int(course_code[3]) * 100
        try:
            x, err = self.db.addRow('Courses', ['course_code', 'description', 'level'], [course_code, course_name, level]) 
            QMessageBox.information(self.parent, 'Success', "{0} has being successfully added as a new course".format(course_code))
            self.refresh()
            self.loadCourse()
            return
        except Exception as e:
            raise e

    def addcr(self):
        addCr = True
        error = None
        if self.obj.cr_level.currentIndex() == 0:
            error = "Select Class Rep username"
        if error is not None:
            QMessageBox.warning(self.parent, "Error", error)
        level = self.obj.cr_level.currentIndex() * 100
        student_id = self.current_users[self.obj.cr_username.currentIndex()-1][0]
        if len(self.cr)<1:
            self.cr.append([0, 0, 0])
        for i in self.cr:
            if student_id == i[0]:
                QMessageBox.information(self.parent, "Info", "user {0} already exist as class Rep".format(i[1]))
                return
        for i in range(len(self.cr)):
            if level == self.cr[i][2]:
                QMessageBox.question(self.parent, "Confirm", "{0} Level already has a class rep\nDo you want to replace?".format(level))
                if QMessageBox.Yes:
                    self.add_cr(student_id, level)
                return
                
            if i+1 == len(self.cr):
                addCr = True
                QMessageBox.question(self.parent, "Confirm", "Do you want to a new class rep for {0}Level".format(level))
                if QMessageBox.Yes:
                    self.add_cr(student_id, level)
                return

    def loadcr(self, l = None):
        if l == 'input':
            self.current_users = []
            level = self.obj.cr_level.currentIndex() * 100
            for i in self.students:
                if i[2] == level:

                    self.current_users.append([i[0], i[1]])
            self.obj.cr_username.clear()
            self.obj.cr_username.addItem("Select Class Rep")
            self.obj.cr_username.addItems([x[1] for x in self.current_users])
            return
        try:
            self.cr = list()
            x, cr =self.db.getRows("ClassReps", ['student_id', 'level'])
            y, self.students = self.db.getRows("Students", ["id", "username", "level"])
            for i in cr:
                if i[0] != "" and i[0] is not None: 
                    self.cr.append(self.students[i[0]-1])
            self.obj.cr_list.clear()
            self.obj.cr_list.addItems([x[1] + ' - ' + str(x[2]) +'Level' for x in self.cr])
            self.obj.cr_username.addItem("Select Class Rep")
            
        except Exception as e:
            raise(e)

    def add_cr(self, id, level):
        x, err = self.db.updateField(["student_id"], [id], "ClassReps", level, 'level')
        if x:
            QMessageBox.information(self.parent, "Success", "Class Rep status for {0}Level has being updated".format(level))
            self.refresh()
            self.loadcr()
            self.obj.cr_level.setCurrentIndex(0)
        else:
            QMessageBox.warning(self.parent, "Error", "Error updating class Rep for {0}Level".format(level))

    def addLectHall(self):
        desc = self.obj.lectVenueDesc.text()
        loc = self.obj.lectSchList.currentText()
        try:
            x, err = self.db.addRow('LectureEnv', ['description', 'school'], [desc, loc])
            if x:
                QMessageBox.information(self.parent, "Success", "A new lecture hall has being added")
            else:
                QMessageBox.warning(self.parent, "Error", "Could not add lecture venue, try again later")
            self.refresh()
            self.loadLectHall()
            return
        except Exception as e:
            raise(e)

    def update_cr(self):
        index = self.obj.cr_list.currentRow()
        QMessageBox.question(self.parent, "Confirm", "Do you want to remove {0} Level class Rep?".format(self.cr[index][2]))
        if QMessageBox.Yes:
            try:
                x, err = self.db.updateField(["student_id"], [None], "ClassReps", self.cr[index][2], 'level')
                if x:
                    QMessageBox.information(self.parent, "Success", "{0} Level class rep removed".format(self.cr[index][2]))
                    self.refresh()
                    self.loadcr()
                    self.obj.cr_level.setCurrentIndex(0)
                else:
                    QMessageBox.warning(self.parent, "Error", "Could not remove {0} Level class rep, try again later".format(self.cr[index][2]))
            except Exception as e:
                print(e)

    def update_lect(self):
        index = self.obj.lectList.currentRow()
        self.parent.close()