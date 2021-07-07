import os
import sys
import time

from UI.ui_main import Ui_Form
from PyQt5.QtWidgets import QApplication, QFrame, QFileDialog, QMessageBox

from win_login import WinLogin
from win_settings import WinSettings
from utils.read_db import ReadDB
from utils.functions import Func
from utils.my_log import MyLog
from utils.update_class import UpdateClass


class MainWindow(QFrame, Ui_Form):

    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)
            self.retranslateUi(self)

            self.label_up.setHidden(True)  # 上传编号 上传成功时 显示
            self.lineEdit_uid.setHidden(True)  # 上传编号 上传成功时 显示

            self.pushButton_settings.clicked.connect(self.open_settings)  # 配置按钮
            self.pushButton_file.clicked.connect(self.open_file)  # 选取文件按钮
            self.pushButton_upload.clicked.connect(self.upload)  # 上传按钮
            self.pushButton_logout.clicked.connect(self.logout)  # 登出按钮

            self.log = MyLog()

            self.log.logger.info('初始化开始')
            self.var()
            self.load_info()
            self.load_project()
            self.login()
            self.log.logger.info('初始化完成')
        except Exception as e:
            self.log.logger.warning('__init__:' + str(e))

    # 登出按钮
    def logout(self):
        self.hide()
        self.win_login.show()

    # 初始化变量
    def var(self):
        self.filenames = None
        self.read_db = ReadDB()
        self.func = Func(self.read_db)

    # 载入软件标题及说明
    def load_info(self):
        self.info = self.read_db.get_info()
        self.setWindowTitle(self.info[0][1])
        self.textEdit_describe.setText(self.info[0][2])

    # 载入全部项目
    def load_project(self):
        project = self.read_db.get_project()
        self.comboBox_project.addItems([str(p[0]) + '_' + str(p[1]) + '_' + p[2] for p in project])

    # 载入ftp服务器
    def load_ftp(self, role_id):
        ftp = self.read_db.get_role_ftp(role_id)
        self.comboBox_ftp.addItems(ftp)

    # 打开登陆界面
    def login(self):
        self.win_login = WinLogin(self.info[0][1], self.read_db, self)
        self.win_login.sing.connect(self.auth)
        if not self.win_login.remember_auto_password():
            self.win_login.show()

    # 登陆成功
    def auth(self, user_id, role_id):
        self.win_login.hide()
        self.user_id = user_id
        self.role_id = role_id
        if role_id != 1:
            self.pushButton_settings.setHidden(True)
        self.load_ftp(role_id)
        self.show()

    # 打开配置页面
    def open_settings(self):
        self.win_settings = WinSettings(self.read_db, self)
        self.win_settings.show()

    # 选取文件
    def open_file(self):
        try:
            self.filenames, _ = QFileDialog.getOpenFileNames(self,
                                                             "选取文件",
                                                             ".",
                                                             "ALL 文件 (*)")
            self.lineEdit_filename.setText(str(self.filenames))
        except Exception as e:
            print(e)

    # 上传文件
    def upload(self):
        if not self.filenames: return

        # 初始化
        self.label_up.setHidden(True)
        self.lineEdit_uid.setHidden(True)
        self.pushButton_upload.setDisabled(True)
        self.textEdit_tips.setText('')
        self.progressBar.setValue(0)

        TEMP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp')  # 临时文件夹 路径
        update_obj = {
            'uid': str(time.time()).replace('.', ''),
            'user_id': str(self.user_id),
            'project_id': self.comboBox_project.currentText().split('_')[0],
            'ftp_id': self.comboBox_ftp.currentText().split('_')[0],
            'project_name': self.comboBox_project.currentText().split('_', 1)[-1].replace(':', ''),
            'keyword': None,
            'is_wait': '1'
        }
        self.lineEdit_uid.setText(update_obj.get('uid'))

        self.update_class = UpdateClass(self.role_id, TEMP, update_obj, self.filenames, self.log, self.func,
                                        self.read_db)
        self.update_class.sig_one.connect(self.up_progress)
        self.update_class.sig_end.connect(self.up_end)
        self.update_class.start()

    # 更新进度条
    def up_progress(self, number):
        self.progressBar.setValue(number)

    # 上传结束
    def up_end(self, msg: str, flag: bool):
        QMessageBox.information(self, '提示', msg)
        if '成功' in msg:
            self.label_up.setHidden(False)
            self.lineEdit_uid.setHidden(False)
        self.pushButton_upload.setDisabled(False)
        self.update_class.deleteLater()
        if flag:
            self.textEdit_tips.setText(self.info[0][3])
        else:
            self.textEdit_tips.setText(self.info[0][4])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
