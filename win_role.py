import json
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDialog, QCheckBox, QWidget, QVBoxLayout, QListWidgetItem
from PyQt5.QtCore import pyqtSignal

from UI.ui_role import Ui_Dialog
from utils.read_db import ReadDB


class WinRole(QDialog, Ui_Dialog):
    sing = pyqtSignal()

    def __init__(self, read_db: ReadDB, role_ojb: dict = None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.read_db = read_db
        self.role_ojb = role_ojb if isinstance(role_ojb, dict) else {}

        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

        self.load_role()
        self.load_ftp()

    def load_role(self):
        if self.role_ojb:
            self.lineEdit_name.setText(self.role_ojb.get('name'))

    def load_ftp(self):
        self.check_list = []
        ftp_list = self.read_db.get_ftp()
        for ftp in ftp_list:
            widget = QWidget()
            Layout = QVBoxLayout()
            check = QCheckBox(ftp[1], self)
            check.setObjectName(str(ftp[0]))
            if str(ftp[1]) in json.loads(self.role_ojb.get('ftp_list','[]')):
                check.setChecked(True)
            self.check_list.append(check)
            Layout.addWidget(check)
            widget.setLayout(Layout)
            item = QListWidgetItem()
            item.setSizeHint(QSize(80, 40))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def get_id(self,role_id):
        id_list = []
        for check in self.check_list:
            if check.isChecked():
                id_list.append({'role_id':str(role_id),'ftp_id':check.objectName()})
        return id_list

    def save(self):
        if not self.lineEdit_name.text().strip(): return
        self.role_ojb['name'] = self.lineEdit_name.text().strip()
        if self.role_ojb.get('id'):
            del self.role_ojb['ftp_list']
            role_id = self.role_ojb.pop('id')
            condition = {'id': role_id}
            self.read_db.update_role(self.role_ojb, condition)
            self.read_db.delete_role_ftp(role_id)
        else:
            role_id = self.read_db.add_role(self.role_ojb)
        id_list = self.get_id(role_id)
        self.read_db.add_role_ftp(id_list)
        self.sing.emit()
        self.close()
