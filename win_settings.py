from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QDialog, QHeaderView, QRadioButton, QTableWidgetItem, QMessageBox

from UI.ui_settings import Ui_Dialog
from win_ftp import WinFtp
from win_role import WinRole
from win_user import WinUser
from win_keyword import WinKeyword
from utils.read_db import ReadDB


class WinSettings(QDialog, Ui_Dialog):

    def __init__(self, read_db: ReadDB, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.read_db = read_db

        self.load()

    def load(self):
        headerView = self.tableWidget_ftp.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)
        headerView = self.tableWidget_user.horizontalHeader()
        headerView.setSectionResizeMode(QHeaderView.Stretch)

        headerView = self.tableWidget_ftp.verticalHeader()
        headerView.setHidden(True)
        headerView = self.tableWidget_role.verticalHeader()
        headerView.setHidden(True)
        headerView = self.tableWidget_user.verticalHeader()
        headerView.setHidden(True)
        headerView = self.tableWidget_word.verticalHeader()
        headerView.setHidden(True)

        self.tableWidget_ftp.clicked.connect(self.check)
        self.tableWidget_role.clicked.connect(self.check)
        self.tableWidget_user.clicked.connect(self.check)
        self.tableWidget_word.clicked.connect(self.check)

        self.pushButton_info.clicked.connect(self.update_info)

        self.pushButton_role_add.clicked.connect(self.open_role)
        self.pushButton_role_update.clicked.connect(self.update_role)
        self.pushButton_role_delete.clicked.connect(self.delete_role)

        self.pushButton_user_add.clicked.connect(self.open_user)
        self.pushButton_user_update.clicked.connect(self.update_user)
        self.pushButton_user_delete.clicked.connect(self.delete_user)

        self.pushButton_ftp_add.clicked.connect(self.open_ftp)
        self.pushButton_ftp_update.clicked.connect(self.update_ftp)
        self.pushButton_ftp_detele.clicked.connect(self.delete_ftp)

        self.pushButton_word_search.clicked.connect(self.search_word)
        self.pushButton_word_add.clicked.connect(self.open_word)
        self.pushButton_word_del.clicked.connect(self.delete_word)

        self.pushButton_key.clicked.connect(self.update_key)

        self.load_info()
        self.load_user()
        self.load_ftp()
        self.load_role()
        self.load_word()
        self.load_baidu()

    def getCheckedRow(self, table):
        row = None
        rowCount = table.rowCount()
        for r in range(rowCount):
            if table.cellWidget(r, 0).isChecked():
                row = r
                break
        return row

    def check(self, n: QModelIndex):
        if self.sender().cellWidget(n.row(), 0).isChecked():
            self.sender().cellWidget(n.row(), 0).setChecked(False)
        else:
            self.sender().cellWidget(n.row(), 0).setChecked(True)

    def load_info(self):
        info = self.read_db.get_info()
        self.lineEdit_title.setText(info[0][1])
        self.textEdit_describe1.setText(info[0][2])
        self.textEdit_tips1.setText(info[0][3])
        self.textEdit_tips2.setText(info[0][4])

    def update_info(self):
        if self.lineEdit_title.text().strip() and self.textEdit_describe1.toPlainText().strip():
            info_obj = {
                'title': self.lineEdit_title.text().strip(),
                'describe': self.textEdit_describe1.toPlainText().strip(),
                'tips1': self.textEdit_tips1.toPlainText().strip(),
                'tips2': self.textEdit_tips2.toPlainText().strip()
            }
            self.read_db.update_info(info_obj, {'id': 1})
            QMessageBox.information(self, '提示', '保存成功')

    def load_role(self):
        role = self.read_db.get_role()
        self.load_table(self.tableWidget_role, role)

    def open_role(self, checked, role_ojb=None):
        self.win_role = WinRole(self.read_db, role_ojb, self)
        self.win_role.sing.connect(self.load_role)
        self.win_role.show()

    def update_role(self):
        row = self.getCheckedRow(self.tableWidget_role)
        if row is None: return
        role_obj = {
            'id': self.tableWidget_role.item(row, 1).text(),
            'name': self.tableWidget_role.item(row, 2).text(),
            'ftp_list': self.tableWidget_role.item(row, 3).text(),
        }
        self.open_role(None, role_obj)

    def delete_role(self):
        row = self.getCheckedRow(self.tableWidget_role)
        if row is None: return
        self.read_db.delete_role(self.tableWidget_role.item(row, 1).text())
        self.read_db.delete_role_ftp(self.tableWidget_role.item(row, 1).text())
        self.load_role()

    def load_ftp(self):
        ftp = self.read_db.get_ftp()
        self.load_table(self.tableWidget_ftp, ftp)

    def open_ftp(self, checked, ftp_ojb=None):
        self.win_ftp = WinFtp(self.read_db, ftp_ojb, self)
        self.win_ftp.sing.connect(self.load_ftp)
        self.win_ftp.show()

    def update_ftp(self):
        row = self.getCheckedRow(self.tableWidget_ftp)
        if row is None: return
        ftp_obj = {
            'id': self.tableWidget_ftp.item(row, 1).text(),
            'name': self.tableWidget_ftp.item(row, 2).text(),
            'ip': self.tableWidget_ftp.item(row, 3).text(),
            'port': self.tableWidget_ftp.item(row, 4).text(),
            'username': self.tableWidget_ftp.item(row, 5).text(),
            'password': self.tableWidget_ftp.item(row, 6).text(),
            'path': self.tableWidget_ftp.item(row, 7).text()
        }
        self.open_ftp(None, ftp_obj)

    def delete_ftp(self):
        row = self.getCheckedRow(self.tableWidget_ftp)
        if row is None: return
        self.read_db.delete_ftp(self.tableWidget_ftp.item(row, 1).text())
        self.load_ftp()

    def load_user(self):
        user = self.read_db.get_user()
        self.load_table(self.tableWidget_user, user)

    def open_user(self, checked, user_ojb=None):
        self.win_user = WinUser(self.read_db, user_ojb, self)
        self.win_user.sing.connect(self.load_user)
        self.win_user.show()

    def update_user(self):
        row = self.getCheckedRow(self.tableWidget_user)
        if row is None: return
        user_obj = {
            'id': self.tableWidget_user.item(row, 1).text(),
            'name': self.tableWidget_user.item(row, 2).text(),
            'username': self.tableWidget_user.item(row, 3).text(),
            'password': self.tableWidget_user.item(row, 4).text(),
            'role_id': self.tableWidget_user.item(row, 5).text()
        }
        self.open_user(None, user_obj)

    def delete_user(self):
        row = self.getCheckedRow(self.tableWidget_user)
        if row is None: return
        self.read_db.delete_user(self.tableWidget_user.item(row, 1).text())
        self.load_user()

    def load_word(self):
        word = self.read_db.get_word_view()
        self.load_table(self.tableWidget_word, word)

    def search_word(self):
        k = self.lineEdit_word_search.text().strip()
        word = self.read_db.get_word_view([['word', 'like', '%{}%'.format(k)]])
        self.load_table(self.tableWidget_word, word)

    def open_word(self):
        self.win_keyword = WinKeyword(self.read_db, self)
        self.win_keyword.sing.connect(self.load_word)
        self.win_keyword.show()

    def delete_word(self):
        row = self.getCheckedRow(self.tableWidget_word)
        if row is None: return
        self.read_db.delete_word(self.tableWidget_word.item(row, 1).text())
        self.load_word()

    def load_baidu(self):
        _, API_Key, Secret_Key = self.read_db.get_baidu()
        self.lineEdit_API_Key.setText(API_Key)
        self.lineEdit_Secret_Key.setText(Secret_Key)

    def update_key(self):
        if self.lineEdit_API_Key.text().strip() and self.lineEdit_Secret_Key.text().strip():
            baidu_obj = {
                'api_key': self.lineEdit_API_Key.text().strip(),
                'secret_key': self.lineEdit_Secret_Key.text().strip()
            }
            self.read_db.update_baidu(baidu_obj)
            QMessageBox.information(self, '提示', '保存成功')

    def load_table(self, table, items):
        table.setRowCount(0)
        if items:
            for n, item in enumerate(items):
                table.setRowCount(n + 1)
                radio = QRadioButton()
                table.setCellWidget(n, 0, radio)
                for m, li in enumerate(item):
                    table.setItem(n, m + 1, QTableWidgetItem(str(li)))
