from UI.ui_user import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

from utils.read_db import ReadDB


class WinUser(QDialog, Ui_Dialog):
    sing = pyqtSignal()

    def __init__(self, read_db: ReadDB, user_ojb: dict = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.read_db = read_db
        self.user_ojb = user_ojb if isinstance(user_ojb, dict) else {}

        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

        self.load_role()
        self.load_user()

    def load_user(self):
        if self.user_ojb:
            self.lineEdit_name.setText(self.user_ojb.get('name'))
            self.lineEdit_username.setText(self.user_ojb.get('username'))
            self.lineEdit_password.setText(self.user_ojb.get('password'))
            self.comboBox.setCurrentText(self.user_ojb.get('role_id'))

    def load_role(self):
        self.role_dict = {}
        for role in self.read_db.get_role():
            self.role_dict[role[1]] = role[0]
            self.comboBox.addItem(role[1])

    def save(self):
        if not (self.lineEdit_name.text().strip() and self.lineEdit_username.text().strip() and self.lineEdit_password.text().strip()): return
        self.user_ojb['name'] = self.lineEdit_name.text().strip()
        self.user_ojb['username'] = self.lineEdit_username.text().strip()
        self.user_ojb['password'] = self.lineEdit_password.text().strip()
        self.user_ojb['role_id'] = self.role_dict.get(self.comboBox.currentText())
        if self.user_ojb.get('id'):
            condition = {'id': self.user_ojb.pop('id')}
            self.read_db.update_user(self.user_ojb, condition)
        else:
            self.read_db.add_user(self.user_ojb)
        self.sing.emit()
        self.close()
