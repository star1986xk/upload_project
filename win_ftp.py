from UI.ui_ftp import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

from utils.read_db import ReadDB


class WinFtp(QDialog, Ui_Dialog):
    sing = pyqtSignal()

    def __init__(self, read_db: ReadDB, ftp_ojb: dict = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.read_db = read_db
        self.ftp_ojb = ftp_ojb if isinstance(ftp_ojb, dict) else {}

        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

        self.load_ftp()

    def load_ftp(self):
        if self.ftp_ojb:
            self.lineEdit_name.setText(self.ftp_ojb.get('name'))
            self.lineEdit_ip.setText(self.ftp_ojb.get('ip'))
            self.lineEdit_port.setText(self.ftp_ojb.get('port'))
            self.lineEdit_username.setText(self.ftp_ojb.get('username'))
            self.lineEdit_password.setText(self.ftp_ojb.get('password'))
            self.lineEdit_path.setText(self.ftp_ojb.get('path'))

    def save(self):
        if not (self.lineEdit_name.text().strip() and self.lineEdit_ip.text().strip() and self.lineEdit_port.text().strip() and self.lineEdit_username.text().strip() and self.lineEdit_password.text().strip() and self.lineEdit_path.text().strip()): return
        self.ftp_ojb['name'] = self.lineEdit_name.text().strip()
        self.ftp_ojb['ip'] = self.lineEdit_ip.text().strip()
        self.ftp_ojb['port'] = self.lineEdit_port.text().strip()
        self.ftp_ojb['username'] = self.lineEdit_username.text().strip()
        self.ftp_ojb['password'] = self.lineEdit_password.text().strip()
        self.ftp_ojb['path'] = self.lineEdit_path.text().strip()
        if self.ftp_ojb.get('id'):
            condition = {'id': self.ftp_ojb.pop('id')}
            self.read_db.update_ftp(self.ftp_ojb, condition)
        else:
            self.read_db.add_ftp(self.ftp_ojb)
        self.sing.emit()
        self.close()
