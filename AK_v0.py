from PyQt5.QtWidgets import (QPushButton, QWidget, QTableWidget, QHBoxLayout, QVBoxLayout, QApplication, QDesktopWidget, QTableWidgetItem, QHeaderView)


class table(QWidget):

    def __init__(self):
        super().__init__()
        self.zjhang = QPushButton('增加一行')
        # self.inform = QTextBrowser()
        self.zjhang.clicked.connect(self.addhang)
        self.initUI()

    def initUI(self):
        self.resize(700, 500)
        self.setWindowTitle('我的账号管理')
        self.table = QTableWidget(1, 3)
        self.table.setHorizontalHeaderLabels(['Website or App', 'ID', 'Password'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setStyleSheet( "::section{Background-color:rgb(192,192,192); height:40px; font:Georgia;}")
        self.zjhang.setStyleSheet("font:bold")
        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.zjhang)
        self.setLayout(layout)
        self.center()
        self.show()

    def addhang(self):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    exp = table()
    sys.exit(app.exec_())