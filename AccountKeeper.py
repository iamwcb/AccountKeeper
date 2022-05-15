import configparser
import random
import re
import string

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from base64 import b64decode
from addWindow import Ui_addWindow
from LoginDialog import Ui_LoginDialog
from modify import Ui_modify
from modifyLogin import Ui_modifyLogin
from bs4 import BeautifulSoup
from urllib import request
import resources_rc


Button_style = ''' 
                     QPushButton
                     {color: Black;
                     font-family: Courier;
                     font : 16px;}
                     QPushButton:hover
                     {background-color:rgb(224, 128, 49);}
                     '''
LineEdit_style = """
        QLineEdit{
        font-family:"Courier New";
        font-size:18px;
        }"""

Label_style = """
        QLabel{
        font-family:"Courier New";
        color: white;
        font-weight: bold;
        font-size:16px;
        } """

CheckBox_style = """
        QCheckBox{
        color: white;
        } """

RadioButton_style = """
        QRadioButton{
        color: white;
        } """
button_hover = "QPushButton:hover{background-color:rgb(224, 128, 49);}"


class check_update_thread(QThread):  # 步骤1.创建一个线程实例
    mysignal = pyqtSignal(str, str)  # 创建一个自定义信号，元组参数

    def __init__(self):
        super(check_update_thread, self).__init__()

    def run(self):
        try:
            url = 'http://wuchunbo.online/2020/11/20/Account-Keeper/'
            html = request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')
            find = soup.find_all('a', href=re.compile('pan.baidu.com'))
            self.mysignal.emit(find[0].get('href'), find[0].get_text())
        except IOError:
            self.mysignal.emit('Check failed', 'Check failed')


# 创建数据库连接
def createConnection():
    # 选择数据库类型，这里为sqlite3数据库
    db = QSqlDatabase.addDatabase("QSQLITE")
    # 创建数据库test0.db,如果存在则打开，否则创建该数据库
    db.setDatabaseName("UserAccount.db")
    # 打开数据库
    db.open()


# 创建表
def createTable():
    # 创建QsqlQuery对象，用于执行sql语句
    q = QSqlQuery()
    q.exec_("create table if not exists t1 (Website varchar(20), ID varchar(20), Password varchar(20))")
    q.exec_("commit")


# 若无ini文件，则创建
def createIni():
    config = configparser.ConfigParser()
    file = config.read('user.ini')
    config_dict = config.defaults()
    if config.defaults():
        print('yes')
    else:
        config["DEFAULT"] = {
            "user_name": "admin",
            "password": "admin",
            "remember": "False"
        }
        with open('user.ini', 'w') as configfile:
            config.write(configfile)


class Model(QSqlTableModel):
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        # 设置要载入的表名
        self.setTable("t1")
        # 这一步应该是执行查询的操作，不太理解
        self.select()
        # 数据更新的策略，详细可以查看Qt文档
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)


# 表格，用于展示数据库中的数据
class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1400, 800)  # 窗口大小
        self.view = QTableView()
        self.model = Model(self.view)
        self.view.setModel(self.model)
        self.view.setFont(QFont("Courier New", 10))  # 设置表格字体
        # 表格样式设置
        # self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置单元格不可编辑
        # self.view.setSelectionBehavior(QTableView.SelectRows)  # 选取整行
        self.view.setAlternatingRowColors(True)  # 交替变色
        self.view.setStyleSheet("alternate-background-color: #F5F5F5;")  # 定义交替的色号
        self.view.horizontalHeader().setStyleSheet("::section{Background-color:#292929;color:#fff}")  # rgb末尾表示透明度0-255
        self.view.horizontalHeader().setFont(QFont("Courier New", 11, QFont.Bold))
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.setFrameShape(QFrame.NoFrame)  # 无边框
        # 布局设置
        wwg = QWidget(self)
        wl = QHBoxLayout(wwg)
        wl.addWidget(self.view)
        self.setLayout(wl)

    # def paintEvent(self, event):  # 设置背景图片
    #     self.painter = QPainter()
    #     self.painter.begin(self)
    #     self.painter.drawPixmap(self.rect(), QPixmap(resource_path(r"pic\1.png")))
    #     self.painter.end()


# 增加记录的窗口
class addWindow(QDialog, Ui_addWindow):
    def __init__(self, parent=None):
        super(addWindow, self).__init__(parent)
        self.setupUi(self)
        self.yesbtn.setStyleSheet(Button_style)
        self.cancelbtn.setStyleSheet(Button_style)
        self.genPw.setStyleSheet(Button_style)
        self.labelWebsite.setStyleSheet(Label_style)
        self.labelID.setStyleSheet(Label_style)
        self.labelPw.setStyleSheet(Label_style)
        self.lineeditWebsite.setStyleSheet(LineEdit_style)
        self.lineeditID.setStyleSheet(LineEdit_style)
        self.lineeditPw.setStyleSheet(LineEdit_style)
        self.auto_az.setStyleSheet(CheckBox_style)
        self.auto_AZ.setStyleSheet(CheckBox_style)
        self.auto_num.setStyleSheet(CheckBox_style)
        self.auto_char.setStyleSheet(CheckBox_style)
        self.initui()

    def initui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去窗口

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap(':/images/images/bm.png'))
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
class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)

        self.pbLogin.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)
        # 样式设置
        self.keepPwBtn.setStyleSheet(RadioButton_style)
        self.pbLogin.setStyleSheet(Button_style)
        self.pbCancel.setStyleSheet(Button_style)
        self.leName.setStyleSheet(LineEdit_style)
        self.lePassword.setStyleSheet(LineEdit_style)

        self.initui()
        self.load_config()

    # 导入配置信息中的账号密码
    def load_config(self):
        config = configparser.ConfigParser()
        file = config.read('user.ini')
        config_dict = config.defaults()
        self.leName.setText(config_dict['user_name'])
        if config_dict['remember'] == 'True':
            self.lePassword.setText(config_dict['password'])
            self.keepPwBtn.setChecked(True)
        else:
            self.keepPwBtn.setChecked(False)

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap(":/images/images/bm.png"))
        self.painter.end()

    def login(self):
        config = configparser.ConfigParser()
        file = config.read('user.ini')
        config_dict = config.defaults()
        if self.leName.text() == config_dict['user_name'] and self.lePassword.text() == config_dict['password']:
            self.accept()  # 关闭对话框并返回1
            print('login successfully!')
            if self.keepPwBtn.isChecked():
                config["DEFAULT"] = {
                    "user_name": self.leName.text(),
                    "password": self.lePassword.text(),
                    "remember": "True"
                }
                with open('user.ini', 'w') as configfile:
                    config.write(configfile)
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
class modifyLoginInfo(QDialog, Ui_modifyLogin):
    def __init__(self, parent=None):
        super(modifyLoginInfo, self).__init__(parent)
        self.resize(400, 250)
        self.setupUi(self)
        # 设置样式
        self.queren.setStyleSheet(Button_style)
        self.quxiao.setStyleSheet(Button_style)
        self.labelOldPw.setStyleSheet(Label_style)
        self.labelNewAcc.setStyleSheet(Label_style)
        self.labelNewPw.setStyleSheet(Label_style)
        self.oldpw.setStyleSheet(LineEdit_style)
        self.newacc.setStyleSheet(LineEdit_style)
        self.newpw.setStyleSheet(LineEdit_style)
        self.initui()

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap(":/images/images/bm.png"))
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
        self.setWindowTitle("Delete")
        self.resize(300, 100)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        # self.setStyleSheet(style)
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
        self.painter.drawPixmap(self.rect(), QPixmap(":/images/images/bm.png"))
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


class modifyinfo(QWidget, Ui_modify):
    def __init__(self, parent=None):
        super(modifyinfo, self).__init__(parent)
        self.setupUi(self)
        # 设置样式
        self.yesbtn.setStyleSheet(Button_style)
        self.cancelbtn.setStyleSheet(Button_style)
        self.lineeditWebsite.setStyleSheet(LineEdit_style)
        self.lineeditID.setStyleSheet(LineEdit_style)
        self.lineeditPw.setStyleSheet(LineEdit_style)
        self.lineEdit.setStyleSheet(Label_style)
        self.lineEdit_2.setStyleSheet(Label_style)
        self.lineEdit_3.setStyleSheet(Label_style)
        self.initui()

    def initui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去窗口

    def paintEvent(self, event):  # 设置背景图片
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap(":/images/images/bm.png"))
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
        self.setWindowIcon(QIcon("akico.ico"))
        self.window1 = TestWidget()
        self.window2 = qrshanchu()
        self.window3 = addWindow()
        self.window4 = modifyLoginInfo()
        self.window5 = modifyinfo()
        self.version = "Version 1.4"

        self.statusBar()  # 创建一个空的状态栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        eidtMenu = menubar.addMenu('Edit')
        setMenu = menubar.addMenu('Settings')
        helpMenu = menubar.addMenu('Help')

        # 给menu创建一个Action
        exitAction = QAction(QIcon(':/images/images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)
        # 将这个Action添加到fileMenu上
        fileMenu.addAction(exitAction)

        # 给Edit创建Action
        # 第一个，增加一条记录
        addAction = QAction(QIcon(":/images/images/add.png"), 'Add', self)
        addAction.setShortcut('Ctrl+N')
        addAction.setStatusTip('Add one information')
        addAction.triggered.connect(self.addclick)
        eidtMenu.addAction(addAction)
        # 第二个，删除一条记录
        delAction = QAction(QIcon(":/images/images/delete_fill.png"), 'Delete', self)
        delAction.setShortcut('Delete')
        delAction.setStatusTip('Delete one information')
        delAction.triggered.connect(self.subclick)
        eidtMenu.addAction(delAction)
        # 第三个，修改一条记录
        modifyAction = QAction(QIcon(":/images/images/modify.png"), 'Modify', self)
        modifyAction.setShortcut('Ctrl+M')
        modifyAction.setStatusTip('Modify one information')
        modifyAction.triggered.connect(self.modifyThisRow)
        eidtMenu.addAction(modifyAction)

        # 给Settings创建Action
        modifyLogin = QAction(QIcon(":/images/images/modify_login.png"), 'Modify Login Information', self)
        # modifyLogin.setShortcut('')
        modifyLogin.setStatusTip('Modify Login Information')
        modifyLogin.triggered.connect(self.xg)
        setMenu.addAction(modifyLogin)

        aboutAction = QAction(QIcon(":/images/images/about.png"), 'About', self)
        # aboutAction.setShortcut('Ctrl+M')
        aboutAction.setStatusTip('About this software')
        aboutAction.triggered.connect(self.aboutbtn)
        update_check = QAction(QIcon(":/images/images/update.png"), 'Check for updates', self)
        update_check.setStatusTip('Check for updates')
        update_check.triggered.connect(self.update_check_action)
        helpMenu.addAction(aboutAction)
        helpMenu.addAction(update_check)

        self.setWindowTitle('Account Keeper')

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
        self.window3.genPw.clicked.connect(self.autoGenPw)
        self.window4.queren.clicked.connect(self.cz)
        self.window4.quxiao.clicked.connect(self.qx)
        self.window5.yesbtn.clicked.connect(self.confirmModifyInfo)
        self.window5.cancelbtn.clicked.connect(self.cancelModifyInfo)

        # 更新线程
        self.my_thread = check_update_thread()  # 主线程连接子线
        self.my_thread.mysignal.connect(self.update_result)  # 信号连接

    def update_check_action(self):
        self.my_thread.start()

    def update_result(self, url, version):
        if url == 'Check failed':
            QMessageBox.information(self, "Update", "Check Failed! Please Check Your Internet!")
        elif version == self.version:
            QMessageBox.information(self, "Update", "You already have the latest version!")
        else:
            msg = "<a href='%s'>The New %s is available. Click to download</a>" % (url, version)
            QMessageBox.information(self, "Update", msg)

    def autoGenPw(self):
        total_list = ""
        list_az = string.ascii_lowercase
        list_AZ = string.ascii_uppercase
        list_num = string.digits
        list_char = string.punctuation
        if self.window3.auto_az.isChecked() or self.window3.auto_AZ.isChecked() or self.window3.auto_num.isChecked() or self.window3.auto_char.isChecked():
            if self.window3.auto_az.isChecked():
                total_list = total_list + list_az
            if self.window3.auto_AZ.isChecked():
                total_list = total_list + list_AZ
            if self.window3.auto_num.isChecked():
                total_list = total_list + list_num
            if self.window3.auto_char.isChecked():
                total_list = total_list + list_char
            temp_count = int(self.window3.pwLen.value())
            auto_gen_pw = ''
            while temp_count != 0:
                auto_gen_pw = auto_gen_pw + random.sample(total_list, 1)[0]
                temp_count = temp_count - 1
            self.window3.lineeditPw.setText(auto_gen_pw)
        else:
            QMessageBox.critical(self, u'Warning', u'Check at least one check box!')

    def aboutbtn(self):
        QMessageBox.about(self, u'About',
                          u"Account Manager (%s)\n\nThis software is used to record your account and password. \n\n\n\nLucas Wu All Rights Reserved" % self.version)

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
        conn = sqlite3.connect('UserAccount.db')
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

    def yes(self):
        index = self.window1.view.currentIndex()
        self.window1.model.removeRow(index.row())
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

    def cancelInput(self):
        self.window3.lineeditWebsite.setText('')
        self.window3.lineeditID.setText('')
        self.window3.lineeditPw.setText('')
        self.window3.close()

    def cz(self):
        config = configparser.ConfigParser()
        file = config.read('user.ini')
        config_dict = config.defaults()
        if self.window4.oldpw.text() == config_dict['password']:
            config["DEFAULT"] = {
                "user_name": self.window4.newacc.text(),
                "password": self.window4.newpw.text(),
                "remember": False
            }
            with open('user.ini', 'w') as configfile:
                config.write(configfile)
            QMessageBox.information(self, "Successful!", "Login Information Modified Successfully")
            self.window4.oldpw.setText('')
            self.window4.newacc.setText('')
            self.window4.newpw.setText('')
            self.window4.close()
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
    createIni()
    dlck = LoginDialog()
    if dlck.exec_():
        w = mainw()
        w.resize(1400, 800)
        w.show()
        sys.exit(a.exec_())
