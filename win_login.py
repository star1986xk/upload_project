import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSettings

from UI.ui_login import Ui_Dialog
from utils.read_db import ReadDB


class WinLogin(QDialog, Ui_Dialog):
    sing = pyqtSignal(int, int)

    def __init__(self, title, read_db: ReadDB, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)

        self.setWindowTitle(title)
        self.read_db = read_db

        self.settings = QSettings("config.ini", QSettings.IniFormat)

        self.pushButton_login.clicked.connect(self.login_click)
        self.pushButton_cancel.clicked.connect(self.quit)
        self.checkBox_remember.stateChanged.connect(self.remb_check_change)
        self.checkBox_auto.stateChanged.connect(self.auto_check_change)

    def remb_check_change(self, state):
        if state == 0:
            self.checkBox_auto.setChecked(state)

    def auto_check_change(self, state):
        if state == 2:
            self.checkBox_remember.setChecked(True)

    def login_click(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        if not (username and password): return
        self.settings.setValue('l_u', username)
        self.settings.setValue('l_p', password)
        self.settings.setValue('remember_password', 1 if self.checkBox_remember.isChecked() else 0)
        self.settings.setValue('auto_login', 1 if self.checkBox_auto.isChecked() else 0)
        self.is_login(username, password)

    def is_login(self, username, password):
        result = self.read_db.get_login(username, password)
        if result:
            self.sing.emit(result[0][0], result[0][4])  # user_id,role_id
            return True
        else:
            QMessageBox.information(self, '提示', '账号或密码错误!')

    # 记得密码或自动登录
    def remember_auto_password(self):
        try:
            l_u = self.settings.value('l_u')
            l_p = self.settings.value('l_p')
            remember_password = int(self.settings.value('remember_password'))
            auto_login = int(self.settings.value('auto_login'))
            if not l_u or not l_p: return
            if remember_password:
                self.lineEdit_username.setText(l_u)
                self.lineEdit_password.setText(l_p)
                self.checkBox_remember.setChecked(True)
                if auto_login:
                    self.checkBox_auto.setChecked(True)
            if auto_login:
                return self.is_login(l_u, l_p)
        except Exception as e:
            print(e)

    def quit(self):
        sys.exit(0)
