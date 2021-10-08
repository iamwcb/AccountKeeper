from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
import sqlite3
from PyQt5.QtCore import Qt
from base64 import b64decode
# from PyQt5.QtCore import QCoreApplication

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(b64decode(pic_code))
    image.close()

BM_PNG = "iVBORw0KGgoAAAANSUhEUgAAAdsAAAEcCAYAAACPlx44AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAARHSURBVHhe7dUxAQAgDMAwtOwB/waHin45oiHnvlkAoCNbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWAmGwBICZbAIjJFgBisgWA1OwHrUarHA2/9jEAAAAASUVORK5CYII="
exit_ico = "AAABAAEAMDAAAAEAIACoJQAAFgAAACgAAAAwAAAAYAAAAAEAIAAAAAAAACQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOJ3SCBKQ3TINjdteDIzZeAiN2oUNjtqDDYzadg2N2loZktwyP5vXBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////8AAP///////wAA////////AAD///////8AAP///////wAA///+f///AAD//8AD//8AAP//AAD//wAA//wAAD//AAD/8AAAD/8AAP/gAAAH/wAA/8AAAAP/AAD/gAAAAf8AAP+AAAAB/wAA/wAAAAD/AAD/AAAAAP8AAP4AAAAAfwAA/gAAAAB/AAD8AAAAAD8AAPwAAAAAPwAA/AAAAAA/AAD8AAAAAD8AAPwAAAAAPwAA+AAAAAAfAAD4AAAAAB8AAPwAAAAAPwAA/AAAAAA/AAD8AAAAAD8AAPwAAAAAPwAA/AAAAAA/AAD8AAAAAD8AAPwAAAAAPwAA/AAAAAA/AAD/AAAAAP8AAP+AAAAB/wAA/4AAAAH/AAD/wAAAA/8AAP/gAAAH/wAA//AAAA//AAD/8AAAD/8AAP//AAD//wAA///AA///AAD///5///8AAP///////wAA////////AAD///////8AAP///////wAA////////AAA="

get_pic(BM_PNG, 'BM.png')
get_pic(exit_ico, 'exit.ico')

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


# 表格，用于展示数据库中的数据
class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1400, 800)  # 窗口大小
        self.view = QTableView()
        self.model = Model(self.view)
        self.view.setModel(self.model)
        self.view.setFont(QFont("Courier New", 10))  # 设置表格字体
        # 按键布置
        # self.addbtn = QPushButton('Add')
        # self.delbtn = QPushButton('Delete')
        # self.cz = QPushButton("Modify LoginInfo")
        # # self.Tabclose = QPushButton("Close")
        # self.modify = QPushButton("Modify")
        # 按键样式设置
        # self.addbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        # self.addbtn.setStyleSheet(button_hover)
        # self.delbtn.setFont(QFont("Courier New", 10, QFont.Bold))
        # self.delbtn.setStyleSheet(button_hover)
        # self.cz.setFont(QFont("Courier New", 10, QFont.Bold))
        # self.cz.setStyleSheet(button_hover)
        # self.Tabclose.setFont(QFont("Courier New", 10, QFont.Bold))
        # self.Tabclose.setStyleSheet(button_hover)
        # self.modify.setFont(QFont("Courier New", 10, QFont.Bold))
        # self.modify.setStyleSheet(button_hover)
        # 表格样式设置
        #self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置单元格不可编辑
        #self.view.setSelectionBehavior(QTableView.SelectRows)  # 选取整行
        self.view.setAlternatingRowColors(True)  # 交替变色
        self.view.setStyleSheet("alternate-background-color: #F5F5F5;")  # 定义交替的色号
        self.view.horizontalHeader().setStyleSheet("::section{Background-color:#252521;color:#fff;border:#3F3F3F"
                                                   ";height:35px}")  # rgb末尾表示透明度0-255
        self.view.horizontalHeader().setFont(QFont("Courier New", 13, QFont.Bold))
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.setFrameShape(QFrame.NoFrame)  # 无边框
        # 布局设置
        wwg = QWidget(self)
        wl = QHBoxLayout(wwg)
        # layout = QGridLayout()
        # layout.addWidget(self.addbtn, 0, 0)
        # layout.addWidget(self.delbtn, 1, 0)
        # layout.addWidget(self.cz, 2, 0)
        # layout.addWidget(self.modify, 3, 0)
        # layout.addWidget(self.Tabclose, 4, 0)
        wl.addWidget(self.view)
        # wl.addLayout(layout)
        # wl.setStretchFactor(layout, 1)
        # wl.setStretchFactor(self.view, 7)
        self.setLayout(wl)
        self.setStyleSheet(style)

    # def paintEvent(self, event):  # 设置背景图片
    #     self.painter = QPainter()
    #     self.painter.begin(self)
    #     self.painter.drawPixmap(self.rect(), QPixmap(resource_path(r"pic\1.png")))
    #     self.painter.end()


# 增加记录的窗口
class addWindow(QWidget):
    def __init__(self, parent=None):
        super(addWindow, self).__init__(parent)
        self.resize(400, 100)
        self.setStyleSheet(style)
        # self.setWindowOpacity(0.8)  # 窗口透明度
        # 设置增加记录的标签和文本框
        self.labelWebsite = QLabel("Website")
        self.labelID = QLabel("ID")
        self.labelPw = QLabel("Password")

        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.white)
        self.labelWebsite.setPalette(pe)
        self.labelID.setPalette(pe)
        self.labelPw.setPalette(pe)

        self.labelWebsite.setFont(QFont("Courier New", 10, QFont.Bold))
        self.labelID.setFont(QFont("Courier New", 10, QFont.Bold))
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
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去窗口

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap('BM.png'))
        self.painter.end()

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


# 登录窗口
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
        # .setEchoMode(EchoMode),设置输入框显示格式,0--Normal,1--NoEcho,2--Password,3--PasswordEchoOnEdit
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

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("BM.png"))
        self.painter.end()

    def login(self):
        print('login successfully!')
        if self.leName.text() == self.myacc and self.lePassword.text() == self.mypw:
            self.accept()  # 关闭对话框并返回1
        else:
            QMessageBox.critical(self, u'ERROR', u'User name password mismatch')

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


# 修改登录信息
class xgdl(QDialog):
    def __init__(self, parent=None):
        super(xgdl, self).__init__(parent)
        self.resize(400, 250)
        # self.setWindowOpacity(0.8)  # 窗口透明度
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
        self.painter.drawPixmap(self.rect(), QPixmap("BM.png"))
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


# 确认删除的窗口
class qrshanchu(QDialog):
    def __init__(self, parent=None):
        super(qrshanchu, self).__init__(parent)
        self.resize(300, 100)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setStyleSheet(style)
        # self.setWindowOpacity(0.8)  # 窗口透明度
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

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("BM.png"))
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


class modifyinfo(QWidget):
    def __init__(self, parent=None):
        super(modifyinfo, self).__init__(parent)
        self.resize(400, 100)
        self.setStyleSheet(style)
        # self.setWindowOpacity(0.8)  # 窗口透明度
        # 设置增加记录的标签和文本框
        self.labelWebsite = QLabel("New Website")
        self.labelID = QLabel("New ID")
        self.labelPw = QLabel("New Password")

        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.white)
        self.labelWebsite.setPalette(pe)
        self.labelID.setPalette(pe)
        self.labelPw.setPalette(pe)

        self.labelWebsite.setFont(QFont("Courier New", 10, QFont.Bold))
        self.labelID.setFont(QFont("Courier New", 10, QFont.Bold))
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
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去窗口

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("BM.png"))
        self.painter.end()

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


# 主窗口
class mainw(QMainWindow):
    def __init__(self, parent=None):
        super(mainw, self).__init__(parent)
        self.setWindowIcon(QIcon("exit.ico"))
        self.window1 = TestWidget()
        self.window2 = qrshanchu()
        self.window3 = addWindow()
        self.window4 = xgdl()
        self.window5 = modifyinfo()

        self.statusBar()  # 创建一个空的状态栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        eidtMenu = menubar.addMenu('Edit')
        setMenu = menubar.addMenu('Settings')
        helpMenu = menubar.addMenu('Help')

        # 给menu创建一个Action
        exitAction = QAction(QIcon('exit.ico'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)
        # 将这个Action添加到fileMenu上
        fileMenu.addAction(exitAction)

        # 给Edit创建Action
        # 第一个，增加一条记录
        addAction = QAction(QIcon("exit.ico"), 'Add', self)
        addAction.setShortcut('Ctrl+N')
        addAction.setStatusTip('Add one information')
        addAction.triggered.connect(self.addclick)
        eidtMenu.addAction(addAction)
        # 第二个，删除一条记录
        delAction = QAction(QIcon("exit.ico"), 'Delete', self)
        delAction.setShortcut('Delete')
        delAction.setStatusTip('Delete one information')
        delAction.triggered.connect(self.subclick)
        eidtMenu.addAction(delAction)
        # 第三个，修改一条记录
        modifyAction = QAction(QIcon("exit.ico"), 'Modify', self)
        modifyAction.setShortcut('Ctrl+M')
        modifyAction.setStatusTip('Modify one information')
        modifyAction.triggered.connect(self.modifyThisRow)
        eidtMenu.addAction(modifyAction)

        # 给Settings创建Action
        modifyLogin = QAction(QIcon("exit.ico"), 'Modify Login Information', self)
        # modifyLogin.setShortcut('')
        modifyLogin.setStatusTip('Modify Login Information')
        modifyLogin.triggered.connect(self.xg)
        setMenu.addAction(modifyLogin)

        aboutAction = QAction(QIcon("exit.ico"), 'About', self)
        # aboutAction.setShortcut('Ctrl+M')
        aboutAction.setStatusTip('About this software')
        aboutAction.triggered.connect(self.aboutbtn)
        helpMenu.addAction(aboutAction)

        self.setWindowTitle('Account Manager')
        self.setGeometry(300, 300, 450, 450)

        self.mainFormLayout = QVBoxLayout(self.window1)
        self.window1.setLayout(self.mainFormLayout)
        self.setCentralWidget(self.window1)
        # self.window1.addbtn.clicked.connect(self.addclick)
        # self.window1.delbtn.clicked.connect(self.subclick)
        # self.window1.cz.clicked.connect(self.xg)
        # self.window1.modify.clicked.connect(self.modifyThisRow)
        # self.window1.Tabclose.clicked.connect(self.closeWindow)
        self.window2.btn1.clicked.connect(self.yes)
        self.window2.btn2.clicked.connect(self.no)
        self.window3.yesbtn.clicked.connect(self.myinput)
        self.window3.cancelbtn.clicked.connect(self.cancelInput)
        self.window4.queren.clicked.connect(self.cz)
        self.window4.quxiao.clicked.connect(self.qx)
        self.window5.yesbtn.clicked.connect(self.confirmModifyInfo)
        self.window5.cancelbtn.clicked.connect(self.cancelModifyInfo)

    def aboutbtn(self):
        QMessageBox.about(self, u'About',
                          u'Account Manager (Version 1.0)\n\nThis software is used to record your account and password. The \'admin\' row represents login information, it cannot be delete!\n\n\n\nwcb All Rights Reserved')

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
        print(web, acc, pw)
        # c.execute("SELECT Website,ID,Password FROM t1 WHERE Website='%s'" % web)
        # info = c.fetchone()
        c.execute(
            "UPDATE t1 SET Website='%s',ID='%s', Password='%s' WHERE Website == '%s' AND ID == '%s' AND Password == '%s' " % (
            inputWs, inputAcc, inputPw, web, acc, pw))
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

    # def closeWindow(self):
    #     self.window1.close()
    #     self.window2.close()
    #     self.window3.close()

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
    createConnection()
    createTable()
    dlck = LoginDialog()
    if dlck.exec_():
        w = mainw()
        w.resize(1400, 800)
        w.show()
        sys.exit(a.exec_())
