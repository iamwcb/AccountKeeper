from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3
from PyQt5.QtCore import Qt

style = """
        .QPushButton{
        border-style:none;
        border:1px solid #C2CCD8; 
        color:#fff;  
        padding:5px;
        min-height:25px;
        border-radius:5px;
        font-size:20px;
        font-weight:800;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);
        }
        .QLineEdit{
        font-family:"Courier New";
        font-size:20px;
        }
    """
# 创建数据库连接
# def createConnection():
#     # 选择数据库类型，这里为sqlite3数据库
#     db = QSqlDatabase.addDatabase("QSQLITE")
#     # 创建数据库wcbAccount.db,如果存在则打开，否则创建该数据库
#     db.setDatabaseName("wcbAccount.db")
#     # 打开数据库
#     db.open()
# 创建表
# def createTable():
#     # 创建QsqlQuery对象，用于执行sql语句
#     q = QSqlQuery()
#     q.exec_("create table if not exists t1 (Website varchar(20), ID varchar(20), Password varchar(20))")
#     conn = sqlite3.connect('wcbAccount.db')
#     c = conn.cursor()
#     c.execute("SELECT ID,Password FROM t1 WHERE Website='admin'")
#     if not c.fetchone():
#         q.exec_(u"insert into t1  values('admin','admin','admin')")
#     q.exec_("commit") #提交数据库

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("wcbAccount.db")
db.open()
q = QSqlQuery()
q.exec_("create table if not exists t1 (Website varchar(20), ID varchar(20), Password varchar(20))")
conn = sqlite3.connect('wcbAccount.db')
c = conn.cursor()
c.execute("SELECT ID,Password FROM t1 WHERE Website='admin'")
if not c.fetchone():
    q.exec_(u"insert into t1  values('admin','admin','admin')")
q.exec_("commit")  # 提交数据库

class Model(QSqlTableModel):
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        # 设置要载入的表名
        self.setTable("t1")
        self.select()
        # 数据更新的策略，详细可以查看Qt文档
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)

class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1000, 700)
        self.setWindowIcon(QIcon('D:/File/file_python/pycharm_file/mysql_96.ico'))
        self.setWindowTitle('账号管理')
        self.view = QTableView()
        self.view.setFont(QFont("Courier New", 10))
        self.addbtn = QPushButton('增加记录')
        self.delbtn = QPushButton('删除记录')
        self.cz = QPushButton("修改登录信息")

        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置单元格不可编辑
        self.view.setSelectionBehavior(QTableView.SelectRows) #选取整行
        self.view.setAlternatingRowColors(True) #交替变色
        self.view.setStyleSheet("alternate-background-color: #F5F5F5;") #定义交替的色号

        self.view.horizontalHeader().setStyleSheet("::section{Background-color:#3F3F3F;color:#fff;border:1px solid #3F3F3F;height:35px}")#rgb末尾表示透明度0-255
        self.view.horizontalHeader().setFont(QFont("Courier New", 13, QFont.Bold))
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = Model(self.view) #将数据库绑定到QTableView
        self.view.setModel(self.model)
        wwg = QWidget(self)
        wl = QHBoxLayout(wwg)
        layout = QGridLayout()
        layout.addWidget(self.addbtn,0,0)
        layout.addWidget(self.delbtn,1,0)
        layout.addWidget(self.cz,2,0)
        wl.addWidget(self.view)
        wl.addLayout(layout)
        wl.setStretchFactor(layout, 1)
        wl.setStretchFactor(self.view, 7)
        self.setLayout(wl)
        self.setStyleSheet(style)
        self.newxx = xgdl()

class addWindow(QWidget):
    def __init__(self,parent=None):
        super(addWindow, self).__init__(parent)
        self.resize(400, 100)
        self.setStyleSheet(style)
        self.setWindowIcon(QIcon('D:/File/file_python/pycharm_file/mysql_96.ico'))
        self.setWindowTitle('增加账号')
        # self.table = QTableWidget(1, 3)
        self.labelWebsite = QLabel("Website")
        self.labelWebsite.setFont(QFont("Courier New",10,QFont.Bold))
        self.labelID = QLabel("ID")
        self.labelID.setFont(QFont("Courier New", 10, QFont.Bold))
        self.labelPw = QLabel("Password")
        self.labelPw.setFont(QFont("Courier New", 10, QFont.Bold))
        self.lineeditWebsite = QLineEdit()
        self.lineeditID = QLineEdit()
        self.lineeditPw = QLineEdit()
        self.yesbtn = QPushButton('确认增加')
        layout = QVBoxLayout()
        layout.addWidget(self.labelWebsite)
        layout.addWidget(self.lineeditWebsite)
        layout.addWidget(self.labelID)
        layout.addWidget(self.lineeditID)
        layout.addWidget(self.labelPw)
        layout.addWidget(self.lineeditPw)
        layout.addWidget(self.yesbtn)
        self.setLayout(layout)

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle(u'登录')
        self.setWindowIcon(QIcon('D:/File/file_python/pycharm_file/mysql_96.ico'))
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # self.setWindowOpacity(0.5) 窗口透明度
        self.resize(300, 150)
        self.setStyleSheet(style)
        self.leName = QLineEdit(self)
        self.leName.setPlaceholderText(u'用户名')
        self.leName.setFont(QFont("Courier New", 9, QFont.Bold))
        self.lePassword = QLineEdit(self)
        self.lePassword.setEchoMode(QLineEdit.Password)
        #.setEchoMode(EchoMode),设置输入框显示格式,0--Normal,1--NoEcho,2--Password,3--PasswordEchoOnEdit
        self.lePassword.setPlaceholderText(u'密码')
        self.lePassword.setFont(QFont("Courier New", 9, QFont.Bold))

        self.pbLogin = QPushButton(u'登录', self)
        self.pbCancel = QPushButton(u'取消', self)

        self.pbLogin.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)

        spacerItem = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout = QVBoxLayout()
        layout.addWidget(self.leName)
        layout.addItem(spacerItem)
        layout.addWidget(self.lePassword)
        # 放一个间隔对象美化布局

        layout.addItem(spacerItem)
        # 按钮布局
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.pbLogin)
        buttonLayout.addWidget(self.pbCancel)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        conn = sqlite3.connect('wcbAccount.db')
        c = conn.cursor()
        c.execute("SELECT ID,Password FROM t1 WHERE Website='admin'")
        self.myacc, self.mypw = c.fetchone()

    def login(self):
        print('login')
        if self.leName.text() == self.myacc and self.lePassword.text() == self.mypw:
            self.accept()  # 关闭对话框并返回1
        else:
            QMessageBox.critical(self, u'错误', u'用户名密码不匹配')

class xgdl(QDialog):
    def __init__(self, parent=None):
        super(xgdl, self).__init__(parent)
        self.setWindowIcon(QIcon('D:/File/file_python/pycharm_file/mysql_96.ico'))
        self.resize(400,250)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle(u'修改登录信息')
        self.oldpw = QLineEdit(self)
        self.oldpw.setPlaceholderText(u'输入原密码')
        self.newacc = QLineEdit(self)
        self.newacc.setPlaceholderText(u'输入新的用户名')
        self.newpw = QLineEdit(self)
        self.newpw.setPlaceholderText(u'输入新的密码')
        self.queren = QPushButton(u'确认修改')
        self.quxiao = QPushButton(u'取消')
        layout = QVBoxLayout()
        layout.addWidget(self.oldpw)
        layout.addWidget(self.newacc)
        layout.addWidget(self.newpw)
        layout1 = QHBoxLayout()
        layout1.addWidget(self.queren)
        layout1.addWidget(self.quxiao)
        layout.addLayout(layout1)
        self.setLayout(layout)
        self.setStyleSheet(style)
        self.queren.clicked.connect(self.cz)
        self.quxiao.clicked.connect(self.qx)
        self.tanchu = czcg()
    def cz(self):
        oldpw = self.oldpw.text()
        nacc = self.newacc.text()
        npw = self.newpw.text()
        conn = sqlite3.connect('wcbAccount.db')
        c = conn.cursor()
        c.execute("SELECT Password FROM t1 WHERE Website='admin'")
        if oldpw == c.fetchone()[0]:
            if nacc and npw:
                conn = sqlite3.connect('wcbAccount.db')
                c = conn.cursor()
                c.execute("UPDATE t1 SET ID='%s' WHERE Website = 'admin'" % nacc)
                c.execute("UPDATE t1 SET Password='%s' WHERE Website = 'admin'" % npw)
                conn.commit()
                self.newacc.setText('')
                self.newpw.setText('')
                self.close()
                self.tanchu.show()
            else:
                QMessageBox.critical(self, u'警告', u'用户名密码不能为空')
        else:
            QMessageBox.critical(self, u'警告', u'原密码错误')
    def qx(self):
        self.close()

class czcg(QDialog):
    def __init__(self,parent = None):
        super(czcg, self).__init__(parent)
        self.resize(300,100)
        self.setStyleSheet(style)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon('D:/File/file_python/pycharm_file/mysql_96.ico'))
        self.setWindowTitle('重置成功')
        self.label = QLabel('下次登录生效')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Song", 10, QFont.Bold))
        self.btn = QPushButton("OK")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)
        self.btn.clicked.connect(self.close)

class qrshanchu(QDialog):
    def __init__(self,parent=None):
        super(qrshanchu,self).__init__(parent)
        self.resize(300,100)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setStyleSheet(style)
        self.setWindowIcon(QIcon('D:/File/file_python/pycharm_file/mysql_96.ico'))
        self.setWindowTitle('警告')
        self.label = QLabel('确定要删除吗')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Song", 10, QFont.Bold))
        self.btn1 = QPushButton("确定")
        self.btn2 = QPushButton("取消")
        layout = QHBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.label)
        layout1.addLayout(layout)
        self.setLayout(layout1)
        self.btn1.clicked.connect(self.yes)
        self.btn2.clicked.connect(self.no)
    def yes(self):
        # return True
        self.close()
    def no(self):
        self.close()

class mainw(QWidget):
    def __init__(self,parent = None):
        super(mainw, self).__init__(parent)
        self.window1 = TestWidget()
        self.window2 = qrshanchu()
        self.window3 = addWindow()
        self.window1.addbtn.clicked.connect(self.addclick)
        self.window1.delbtn.clicked.connect(self.subclick)
        self.window1.cz.clicked.connect(self.xg)
        self.window2.btn1.clicked.connect(self.yes)
        self.window2.btn2.clicked.connect(self.no)
        self.window3.yesbtn.clicked.connect(self.myinput)
    def addclick(self):
        self.window3.show()
    def subclick(self):
        self.window2.show()
    def xg(self):
        self.window1.newxx.show()
    def yes(self):
        index = self.window1.view.currentIndex()
        if not self.window1.model.index(index.row(), 0).data() == 'admin':
            self.window1.model.removeRow(index.row())
        else:
            QMessageBox.warning(self, u'警告', u'此条记录无法删除')
        self.window1.model.submitAll()
        self.window2.close()
    def no(self):
        self.window2.close()
    def myinput(self):
        q = QSqlQuery()
        inputWs = self.window3.lineeditWebsite.text()
        inputAcc = self.window3.lineeditID.text()
        inputPw = self.window3.lineeditPw.text()
        q.exec_(u"insert into t1 values('%s','%s','%s')" % (inputWs, inputAcc, inputPw))
        q.exec_("commit")
        self.window3.lineeditWebsite.setText('')
        self.window3.lineeditID.setText('')
        self.window3.lineeditPw.setText('')
        self.window1.model.submitAll()
        self.window3.close()
if __name__ == "__main__":
    a = QApplication(sys.argv)
    dlck = LoginDialog()
    if dlck.exec_():
        # w = TestWidget()
        w = mainw()
        w.window1.show()
        sys.exit(a.exec_())
