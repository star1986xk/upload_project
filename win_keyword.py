from UI.ui_keyword import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

from utils.read_db import ReadDB


class WinKeyword(QDialog, Ui_Dialog):
    sing = pyqtSignal()

    def __init__(self, read_db: ReadDB, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.read_db = read_db

        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

        self.load_user()

    def load_user(self):
        users = self.read_db.get_user()
        self.comboBox.addItems([str(u[0]) + '_' + u[1] for u in users])

    def save(self):
        word_list = [word.strip() for word in self.textEdit.toPlainText().split('\n') if word.strip()]
        user_id = self.comboBox.currentText().split('_')[0]
        self.read_db.add_word(word_list, user_id)
        if word_list:
            self.sing.emit()
            self.close()
