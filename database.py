'''
Database implementation using sqlite3
'''
import sqlite3
import mysql.connector
import sshtunnel
from exceptions import *


class Database(object):
    """docstring for Database"""
    tname = "Students"

    def __init__(self, dbname):
        '''
        Establishes secured connection to the database with given name dbname
        '''
        self.dbname = dbname
        self.connect()
       
    def connect(self):
        try:
            # sshtunnel.SSH_TIMEOUT = 5.0
            # sshtunnel.TUNNEL_TIMEOUT = 5.0
            # with sshtunnel.SSHTunnelForwarder(
            #     ('ssh.pythonanywhere.com'),
            #     ssh_username='Elbravo014', ssh_password='bravo1998',
            #     remote_bind_address=('Elbravo014.mysql.pythonanywhere-services.com', 3306)
            # ) as tunnel:
            #     self.conn = mysql.connector.connect(
            #         user='Elbravo014', password='bravo1998',
            #         host='127.0.0.1', port=tunnel.local_bind_port,
            #         database='Elbravo014$CPE',
            #     )
            print("Establishing Database Connections")
            self.conn = sqlite3.connect(self.dbname)
            self.cur = self.conn.cursor()
        except Exception as e:
            raise ConnectionError(e)

    def runQuery(self, q, params=None, dict_type =False, commit=True):
        '''
        Executes a query q and binds parameter params to it
        '''
        # print(q, params)
        self.connect()
        check = False
        if sqlite3.complete_statement(q):
            data = {}
            try:
                q = q.strip()
                if params is not None:
                    self.cur.execute(q, params)
                else:
                    self.cur.execute(q)
                if q.lstrip().upper().startswith("SELECT"):
                    values = self.cur.fetchall()
                    if not dict_type:
                        key = []
                        for i in range(len(self.cur.description)):
                            key.append(self.cur.description[i][0])

                        if len(values) == 1:
                            for i, j in zip(values[0], key):
                                data[j] = i

                        if len(values) > 1:
                            x = [list() for i in range(len(values[0]))]
                            for i in values:
                                for p in range(len(i)):
                                    x[p].append(i[p])

                            for i, j in zip(key, x):
                                data[i] = j
                    else: 
                        data = values

                check = True
            except sqlite3.Error as e:
                print("an Error occured: {0}".format(e.args[0]))
                return False, e.args[0]

            else:
                if commit and check:
                    self.save()
                return True, data
            finally:
                self.conn.close()
        return False, "Invalid Query"

    def save(self):
        '''
        Closes the database connection
        '''
        self.conn.commit()
        self.conn.close()

    def createTable(self, table_name, params):
        '''
        Creates a table in the database with given name table_name and columns params
        '''

        return self.runQuery("CREATE TABLE IF NOT EXISTS {0}({1});".format(table_name, params))

    def initializeApp(self, school, dept):
        try:
            queries = '`id`    INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    '`title` TEXT,' \
                        '`fname` TEXT,'\
                        '`courses`   TEXT,'\
                        '`levels`    TEXT,'\
                        '`db_name`   TEXT UNIQUE'
            x, y =  self.createTable("Lecturers", queries)
            queries = '`id`    INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        '`description`   TEXT, `school`    TEXT'
            a, b = self.createTable("lectureEnv", queries)

            queries = '`id`    INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        '`course_code`   TEXT UNIQUE, `description`   TEXT,'\
                        '`level` INTEGER, `dept`  TEXT, `school`    TEXT'
            c, d = self.createTable("Courses", queries)

            queries = '`id`    INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        '`student_id`    INTEGER, `level` INTEGER UNIQUE,'\
                        '`session_start` INTEGER DEFAULT 0,'\
                        '`course_code`   TEXT, `desc`  TEXT,'\
                        '`lecturer_id`   INTEGER, `lecture_env_id`    INTEGER,'\
                        '`time`  TEXT, `rating_id` TEXT, `review`  INTEGER DEFAULT 0'
            e, f = self.createTable("ClassReps", queries)

            queries = '`id`    INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        '`username`  VARCHAR ( 100 ) UNIQUE,'\
                        '`email` VARCHAR ( 50 ) UNIQUE,'\
                        '`password`  VARCHAR ( 255 ),'\
                        '`status`    INTEGER NOT NULL DEFAULT 0,'\
                        '`level` INTEGER, `rating_id` INTEGER, `grade_check`  INTEGER DEFAULT 0'
            g, h = self.createTable("Students", queries)

            queries = '`id`    INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        '`username`  TEXT UNIQUE,  `token` TEXT, `password`  INTEGER'
            i, j = self.createTable("Token", queries)

            queries = '`id`    INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        '`rating_id` INTEGER, `student_id`    INTEGER,'\
                        '`course_code`   TEXT, `time`  TEXT, `lecturer_id`   INTEGER,'\
                        '`lecture_env_id`    INTEGER, `a` INTEGER DEFAULT 0, `b` INTEGER DEFAULT 0,'\
                        '`c` INTEGER DEFAULT 0, `d` INTEGER DEFAULT 0, `e` INTEGER DEFAULT 0,'\
                        '`f` INTEGER DEFAULT 0, `g` INTEGER DEFAULT 0, `h` INTEGER DEFAULT 0,'\
                        '`i` INTEGER DEFAULT 0, `j` INTEGER DEFAULT 0, `k` INTEGER DEFAULT 0,'\
                        '`l` INTEGER DEFAULT 0, `m` INTEGER DEFAULT 0, `n` INTEGER DEFAULT 0,'\
                        '`o` INTEGER DEFAULT 0, `p` INTEGER DEFAULT 0, `q` INTEGER DEFAULT 0,'\
                        '`r` INTEGER DEFAULT 0, `s` INTEGER DEFAULT 0, `t` INTEGER DEFAULT 0,'\
                        '`u` INTEGER DEFAULT 0, `v` INTEGER DEFAULT 0, `w` INTEGER DEFAULT 0,'\
                        '`x` INTEGER DEFAULT 0, `y` INTEGER DEFAULT 0, `lectComment`   TEXT,'\
                        '`recommendations`   TEXT'
            try:
                k, l = self.createTable("Gradings", queries)
                m, n = self.addRow("ClassReps", ['level'], [100])
                o, p = self.addRow("ClassReps", ['level'], [200])
                q, r = self.addRow("ClassReps", ['level'], [300])
                s, t = self.addRow("ClassReps", ['level'], [400])
                u, v = self.addRow("ClassReps", ['level'], [500])
                w, ap = self.addRow("ClassReps", ['level'], [600])
                rows = True
            except Exception as e:
                print("already Added")
                rows = true

            if x and a and c and e and g and i and rows:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def userExists(self, param, col, table_name):
        '''
        Checks if a user with username or email specified exists on the table_name

        '''
        buf = Database.stringify(col, end = ' = ?', sep = ' OR ')
        try:
            for i in param:
                if len(i) < 1:
                    return False, "Input field cannot be empty"
        except:
            pass
        x = self.runQuery("SELECT * FROM {0} WHERE {1};".format(table_name, buf), param)
        try:
            if x[0]:
                if len(x[1]) > 0:
                    return True, x[1]
                return False, "Invalid User"
        except Exception as e:
            raise(e)
            return False, e

    def addRow(self, table_name, fields, values):
        '''
        Adds a new row into the table table_name with parameters user
        '''
        s = Database.stringify(fields, end='')
        binds = Database.stringify(fields, end='? ', inc=False)
        return self.runQuery("INSERT INTO {0}({1}) VALUES({2});".format(table_name, s, binds), values)

    def getRow(self, table_name, fields, params, sep = ' AND ', col = '*'):
        '''
        Retrieves a row from a table in the database
        '''
        buf = Database.stringify(fields, end = ' = ?', sep = sep)
        return self.runQuery("SELECT {2} FROM {0} WHERE {1};".format(table_name, buf, col), params)

    def getRows(self, table_name, cur = '*', fields = None, params = None, sep = ' AND ', withWhere = False):
        '''
        Retrieves rows from a table in the database
        '''
        if fields is not None:
            x = Database.stringify(fields, end = ' = ?', sep = sep)
            if withWhere:
                table_name += ' WHERE {0}'.format(x)

        buf = Database.stringify(cur, sep = ', ')
        
        return self.runQuery("SELECT {1} FROM {0};".format(table_name, buf), params = params, dict_type = True)

    def deleteRow(self, table_name, fields, params):
        '''
        Deletes a particular row from the table
        '''
        buf = Database.stringify(fields, end = ' = ?', sep = 'AND')
        return self.runQuery("DELETE FROM {0} WHERE {1};".format(table_name, buf), params)

    def getUser(self, u_email, password, table_name):
        '''
        retrieves a user from the database with specified email/username and password
        '''
        try:
            x, data = self.runQuery("SELECT * FROM {0} WHERE (email = ? OR username = ?) and password = ?;".format(table_name), [u_email, u_email, password])
            if not x:
                return x, data
            if len(data)<1:
                return False, "Invalid User"
            return x, data
            
        except Exception as e:
            raise e

    def updateField(self, field, value, table_name, col, i = "username"):
        '''
        updates a field in a given row with username on table table_name
        '''
        buf = Database.stringify(field, end=" = ?")
        value.append(col)
        try:
            return self.runQuery("UPDATE {0} SET {1} WHERE {2} = ?;".format(table_name, buf, i), value)
        except Exception as e:
            raise e

    @staticmethod
    def stringify(l, end='', sep=',', inc = True):
        buf = ""
        for x in l:
            if inc:
                buf += x
            if l[-1] != x:
                buf += end + sep
            else:
                buf += end
        return buf



        


