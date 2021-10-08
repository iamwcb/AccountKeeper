from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import sqlite3
from PyQt5.QtCore import Qt
# from PyQt5.QtCore import QCoreApplication

style = """
        .QPushButton{
        border-style:none;
        border:1px solid #C2CCD8; 
        color:#fff;  
        padding:5px;
        min-height:25px;
        #border-radius:5px;
        selection-color:pink;
        font-size:20px;
        font-weight:800;
        #backgrounE:qlineargradient(spreaE:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);#渐变色
        }
        # .QPushButton:hover{background-color:white; color: black;}
        # .QPushButton:pressed{background-color:rgb(46, 104, 170); border-style: inset; }
        .QLineEdit{
        font-family:"Courier New";
        font-size:20px;
        }
    """
button_hover = "QPushButton:hover{background-color:rgb(224, 128, 49);}"

# 创建数据库连接
def createConnection():
    # 选择数据库类型，这里为sqlite3数据库
    db = QSqlDatabase.addDatabase("QSQLITE")
    # 创建数据库test0.db,如果存在则打开，否则创建该数据库
    db.setDatabaseName("wcbAccount.db")
    # 打开数据库
    db.open()

# 创建表
def createTable():
    # 创建QsqlQuery对象，用于执行sql语句
    q = QSqlQuery()
    q.exec_("create table if not exists t1 (Website varchar(20), ID varchar(20), Password varchar(20))")
    # q.exec_("delete from t1")
    # 这里使用 u 将字符串转换成unicode编码，解决中文乱码
    conn = sqlite3.connect('wcbAccount.db')
    c = conn.cursor()
    c.execute("SELECT ID,Password FROM t1 WHERE Website='admin'")
    if not c.fetchone():
        q.exec_(u"insert into t1  values('admin','admin','admin')")
    q.exec_("commit")

class Model(QSqlTableModel):
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        # 设置要载入的表名
        self.setTable("t1")
        # 这一步应该是执行查询的操作，不太理解
        self.select()
        # 数据更新的策略，详细可以查看Qt文档
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#表格，用于展示数据库中的数据
class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1400, 800)  #窗口大小
        self.view = QTableView()
        self.model = Model(self.view)
        self.view.setModel(self.model)
        self.view.setFont(QFont("Courier New", 10)) #设置表格字体
        # 按键布置
        self.addbtn = QPushButton('Add')
        self.delbtn = QPushButton('Delete')
        self.cz = QPushButton("Modify LoginInfo")
        self.Tabclose = QPushButton("Close")
        self.modify = QPushButton("Modify")
        # 按键样式设置
        self.addbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        self.addbtn.setStyleSheet(button_hover)
        self.delbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        self.delbtn.setStyleSheet(button_hover)
        self.cz.setFont(QFont("Courier New", 10, QFont.Bold))
        self.cz.setStyleSheet(button_hover)
        self.Tabclose.setFont(QFont("Courier New", 10, QFont.Bold))
        self.Tabclose.setStyleSheet(button_hover)
        self.modify.setFont(QFont("Courier New", 10, QFont.Bold))
        self.modify.setStyleSheet(button_hover)
        # 表格样式设置
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置单元格不可编辑
        self.view.setSelectionBehavior(QTableView.SelectRows)  # 选取整行
        self.view.setAlternatingRowColors(True)  # 交替变色
        self.view.setStyleSheet("alternate-background-color: #F5F5F5;")  # 定义交替的色号
        self.view.horizontalHeader().setStyleSheet("::section{Background-color:#252521;color:#fff;border:#3F3F3F;height:35px}")  # rgb末尾表示透明度0-255
        self.view.horizontalHeader().setFont(QFont("Courier New", 13, QFont.Bold))
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.setFrameShape(QFrame.NoFrame)  # 无边框
        # 布局设置
        wwg = QWidget(self)
        wl = QHBoxLayout(wwg)
        layout = QGridLayout()
        layout.addWidget(self.addbtn, 0, 0)
        layout.addWidget(self.delbtn, 1, 0)
        layout.addWidget(self.cz, 2, 0)
        layout.addWidget(self.modify, 3, 0)
        layout.addWidget(self.Tabclose, 4, 0)
        wl.addWidget(self.view)
        wl.addLayout(layout)
        wl.setStretchFactor(layout, 1)
        wl.setStretchFactor(self.view, 7)
        self.setLayout(wl)
        self.setStyleSheet(style)
        self.initui_Table()

    def initui_Table(self):
        self.setWindowFlags(Qt.FramelessWindowHint) #去窗口

    def paintEvent(self,event): #设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap(resource_path(r"pic\1.png")))
        self.painter.end()
    def mousePressEvent(self, event): #以下3个函数用来使窗口可以拖动
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

#增加记录的窗口
class addWindow(QWidget):
    def __init__(self,parent=None):
        super(addWindow, self).__init__(parent)
        self.resize(400, 100)
        self.setStyleSheet(style)
        # self.setWindowOpacity(0.8)  # 窗口透明度
        #设置增加记录的标签和文本框
        self.labelWebsite = QLabel("Website")
        self.labelWebsite.setFont(QFont("Courier New",10,QFont.Bold))
        self.labelID = QLabel("ID")
        self.labelID.setFont(QFont("Courier New", 10, QFont.Bold))
        self.labelPw = QLabel("Password")
        self.labelPw.setFont(QFont("Courier New", 10, QFont.Bold))
        self.lineeditWebsite = QLineEdit()
        self.lineeditID = QLineEdit()
        self.lineeditPw = QLineEdit()
        self.yesbtn = QPushButton('Yes')
        self.cancelbtn = QPushButton('Cancel')

        self.yesbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        self.yesbtn.setStyleSheet(button_hover)
        self.cancelbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        self.cancelbtn.setStyleSheet(button_hover)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.yesbtn)
        buttonLayout.addWidget(self.cancelbtn)
        layout = QVBoxLayout()
        layout.addWidget(self.labelWebsite)
        layout.addWidget(self.lineeditWebsite)
        layout.addWidget(self.labelID)
        layout.addWidget(self.lineeditID)
        layout.addWidget(self.labelPw)
        layout.addWidget(self.lineeditPw)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        self.initui()

    def initui(self):
        self.setWindowFlags(Qt.FramelessWindowHint) #去窗口

    def paintEvent(self,event): #设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("E:/File/file_python/pycharm_file/pic/2.PNG"))
        self.painter.end()

    def mousePressEvent(self, event): #以下3个函数用来使窗口可以拖动
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

#登录窗口
class LoginDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        # self.setWindowOpacity(0.9) #窗口透明度
        self.resize(400, 200)
        self.setStyleSheet(style)
        self.leName = QLineEdit(self)
        self.leName.setFixedHeight(30)
        self.leName.setPlaceholderText(u'Account')
        self.leName.setFont(QFont("Courier New", 10, QFont.Bold))
        self.lePassword = QLineEdit(self)
        self.lePassword.setFixedHeight(30)
        self.lePassword.setEchoMode(QLineEdit.Password)
        #.setEchoMode(EchoMode),设置输入框显示格式,0--Normal,1--NoEcho,2--Password,3--PasswordEchoOnEdit
        self.lePassword.setPlaceholderText(u'Password')
        self.lePassword.setFont(QFont("Courier New", 10, QFont.Bold))

        self.pbLogin = QPushButton(u'Login', self)
        self.pbCancel = QPushButton(u'Cancel', self)

        self.pbLogin.setFont(QFont("Courier New", 10, QFont.Bold))
        self.pbLogin.setStyleSheet(button_hover)
        self.pbCancel.setFont(QFont("Courier New", 10, QFont.Bold))
        self.pbCancel.setStyleSheet(button_hover)
        self.pbLogin.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.leName)
        layout.addWidget(self.lePassword)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.pbLogin)
        buttonLayout.addWidget(self.pbCancel)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        conn = sqlite3.connect('wcbAccount.db')
        c = conn.cursor()
        c.execute("SELECT ID,Password FROM t1 WHERE Website='admin'")
        self.myacc, self.mypw = c.fetchone()
        self.initui()

    def paintEvent(self,event): #设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap(resource_path(r"pic\1.png")))
        self.painter.end()

    def login(self):
        print('login successfully!')
        if self.leName.text() == self.myacc and self.lePassword.text() == self.mypw:
            self.accept()  # 关闭对话框并返回1
        else:
            QMessageBox.critical(self, u'ERROR', u'User name password mismatch')
    def initui(self):
        self.setWindowFlags(Qt.FramelessWindowHint) #去窗口

    def mousePressEvent(self, event): #以下3个函数用来使窗口可以拖动
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

#修改登录信息
class xgdl(QDialog):
    def __init__(self, parent=None):
        super(xgdl, self).__init__(parent)
        self.resize(400,250)
        self.setWindowOpacity(0.8)  # 窗口透明度
        self.oldpw = QLineEdit(self)
        self.oldpw.setPlaceholderText(u'original password')
        self.oldpw.setFont(QFont("Courier New", 9, QFont.Bold))
        self.newacc = QLineEdit(self)
        self.newacc.setPlaceholderText(u'new username')
        self.newacc.setFont(QFont("Courier New", 9, QFont.Bold))
        self.newpw = QLineEdit(self)
        self.newpw.setPlaceholderText(u'new password')
        self.newpw.setFont(QFont("Courier New", 9, QFont.Bold))
        self.queren = QPushButton(u'Modify')
        self.quxiao = QPushButton(u'Cancel')

        self.queren.setFont(QFont("Courier New", 10, QFont.Bold))
        self.queren.setStyleSheet(button_hover)
        self.quxiao.setFont(QFont("Courier New", 10, QFont.Bold))
        self.quxiao.setStyleSheet(button_hover)

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
        self.initui()

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("E:/File/file_python/pycharm_file/pic/2.PNG"))
        self.painter.end()

    def initui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去窗口

    def mousePressEvent(self, event):  # 以下3个函数用来使窗口可以拖动
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

#确认删除的窗口
class qrshanchu(QDialog):
    def __init__(self,parent=None):
        super(qrshanchu,self).__init__(parent)
        self.resize(300,100)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setStyleSheet(style)
        self.setWindowOpacity(0.8)  # 窗口透明度
        self.btn1 = QPushButton("Yes")
        self.btn2 = QPushButton("Cancel")

        self.btn1.setFont(QFont("Courier New", 10, QFont.Bold))
        self.btn1.setStyleSheet(button_hover)
        self.btn2.setFont(QFont("Courier New", 10, QFont.Bold))
        self.btn2.setStyleSheet(button_hover)

        layout = QHBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.initui()

    def paintEvent(self,event): #设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("E:/File/file_python/pycharm_file/pic/1.PNG"))
        self.painter.end()
    def initui(self):
        self.setWindowFlags(Qt.FramelessWindowHint) #去窗口

    def mousePressEvent(self, event): #以下3个函数用来使窗口可以拖动
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

class modifyinfo(QWidget):
    def __init__(self,parent=None):
        super(modifyinfo, self).__init__(parent)
        self.resize(400, 100)
        self.setStyleSheet(style)
        # self.setWindowOpacity(0.8)  # 窗口透明度
        #设置增加记录的标签和文本框
        self.labelWebsite = QLabel("New Website")
        self.labelWebsite.setFont(QFont("Courier New",10,QFont.Bold))
        self.labelID = QLabel("New ID")
        self.labelID.setFont(QFont("Courier New", 10, QFont.Bold))
        self.labelPw = QLabel("New Password")
        self.labelPw.setFont(QFont("Courier New", 10, QFont.Bold))
        self.lineeditWebsite = QLineEdit()
        self.lineeditID = QLineEdit()
        self.lineeditPw = QLineEdit()
        self.yesbtn = QPushButton('Yes')
        self.cancelbtn = QPushButton('Cancel')

        self.yesbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        self.yesbtn.setStyleSheet(button_hover)
        self.cancelbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        self.cancelbtn.setStyleSheet(button_hover)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.yesbtn)
        buttonLayout.addWidget(self.cancelbtn)
        layout = QVBoxLayout()
        layout.addWidget(self.labelWebsite)
        layout.addWidget(self.lineeditWebsite)
        layout.addWidget(self.labelID)
        layout.addWidget(self.lineeditID)
        layout.addWidget(self.labelPw)
        layout.addWidget(self.lineeditPw)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        self.initui()

    def initui(self):
        self.setWindowFlags(Qt.FramelessWindowHint) #去窗口

    def paintEvent(self,event): #设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("E:/File/file_python/pycharm_file/pic/2.PNG"))
        self.painter.end()

    def mousePressEvent(self, event): #以下3个函数用来使窗口可以拖动
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

#把所有窗口串联起来
class mainw(QMainWindow):
    def __init__(self,parent = None):
        super(mainw, self).__init__(parent)
        self.window1 = TestWidget()
        self.window2 = qrshanchu()
        self.window3 = addWindow()
        self.window4 = xgdl()
        self.window5 = modifyinfo()
        self.window1.addbtn.clicked.connect(self.addclick)
        self.window1.delbtn.clicked.connect(self.subclick)
        self.window1.cz.clicked.connect(self.xg)
        self.window1.modify.clicked.connect(self.modifyThisRow)
        self.window1.Tabclose.clicked.connect(self.closeWindow)
        self.window2.btn1.clicked.connect(self.yes)
        self.window2.btn2.clicked.connect(self.no)
        self.window3.yesbtn.clicked.connect(self.myinput)
        self.window3.cancelbtn.clicked.connect(self.cancelInput)
        self.window4.queren.clicked.connect(self.cz)
        self.window4.quxiao.clicked.connect(self.qx)
        self.window5.yesbtn.clicked.connect(self.confirmModifyInfo)
        self.window5.cancelbtn.clicked.connect(self.cancelModifyInfo)

    def cancelModifyInfo(self):
        self.window5.close()
        self.window5.lineeditWebsite.setText('')
        self.window5.lineeditID.setText('')
        self.window5.lineeditPw.setText('')

    def confirmModifyInfo(self):
        index = self.window1.view.currentIndex()
        web = self.window1.model.index(index.row(), 0).data()
        acc = self.window1.model.index(index.row(), 1).data()
        pw = self.window1.model.index(index.row(), 2).data()
        inputWs = self.window5.lineeditWebsite.text()
        inputAcc = self.window5.lineeditID.text()
        inputPw = self.window5.lineeditPw.text()
        conn = sqlite3.connect('wcbAccount.db')
        c = conn.cursor()
        print(web,acc,pw)
        # c.execute("SELECT Website,ID,Password FROM t1 WHERE Website='%s'" % web)
        # info = c.fetchone()
        c.execute("UPDATE t1 SET Website='%s',ID='%s', Password='%s' WHERE Website == '%s' AND ID == '%s' AND Password == '%s' " % (inputWs,inputAcc,inputPw, web, acc, pw))
        conn.commit()
        self.window5.lineeditWebsite.setText('')
        self.window5.lineeditID.setText('')
        self.window5.lineeditPw.setText('')
        self.window1.model.submitAll()
        self.window5.close()

    def modifyThisRow(self):
        self.window5.show()

    def addclick(self):
        self.window3.show()

    def subclick(self):
        self.window2.show()

    def xg(self):
        self.window4.show()

    def closeWindow(self):
        self.window1.close()
        self.window2.close()
        self.window3.close()

    def yes(self):
        index = self.window1.view.currentIndex()
        if not self.window1.model.index(index.row(), 0).data() == 'admin':
            self.window1.model.removeRow(index.row())
        else:
            QMessageBox.warning(self, u'Warning', u'Cannot delete this message!')
        self.window1.model.submitAll()
        self.window2.close()

    def no(self):
        self.window2.close()

    def myinput(self):
        q = QSqlQuery()
        inputWs = self.window3.lineeditWebsite.text()
        inputAcc = self.window3.lineeditID.text()
        inputPw = self.window3.lineeditPw.text()
        if not inputWs == 'admin':
            q.exec_(u"insert into t1 values('%s','%s','%s')" % (inputWs, inputAcc, inputPw))
            q.exec_("commit")
            self.window3.lineeditWebsite.setText('')
            self.window3.lineeditID.setText('')
            self.window3.lineeditPw.setText('')
            self.window1.model.submitAll()
            self.window3.close()
        else:
            QMessageBox.warning(self, u'Warning', r"Website cannot be 'admin!'")
            self.window3.close()


    def cancelInput(self):
        self.window3.close()

    def cz(self):
        oldpw = self.window4.oldpw.text()
        nacc = self.window4.newacc.text()
        npw = self.window4.newpw.text()
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
                self.window4.oldpw.setText('')
                self.window4.newacc.setText('')
                self.window4.newpw.setText('')
                self.window4.close()
                self.window1.model.submitAll()
            else:
                QMessageBox.critical(self, u'Warning', u'Cannot be empty!')
        else:
            QMessageBox.critical(self, u'Warning', u'Wrong Password')

    def qx(self):
        self.window4.close()
        self.window4.oldpw.setText('')
        self.window4.newacc.setText('')
        self.window4.newpw.setText('')

if __name__ == "__main__":
    a = QApplication(sys.argv)
    # QCoreApplication.addLibraryPath("./")
    createConnection()
    createTable()
    dlck = LoginDialog()
    if dlck.exec_():
        w = mainw()
        w.window1.show()
        sys.exit(a.exec_())
