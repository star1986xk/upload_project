import os
import sys
import datetime
from UI.ui_check import Ui_Form
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from utils.read_db import ReadDB
from utils.ftp.my_ftp import MyFTP
from utils.functions import Func


class WinCheck(QFrame, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(),self.height())


        self.read_db = ReadDB()
        self.func = Func(self.read_db)
        self.timer = QTimer()
        self.t = 0
        self.timer.timeout.connect(self.timeout_slot)
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_stop.clicked.connect(self.stop)

    def run(self):
        days = self.spinBox.value()
        hours = self.spinBox_2.value()
        minutes = self.spinBox_3.value()
        self.t = self.total = int(datetime.timedelta(days=days, hours=hours, minutes=minutes).total_seconds())

        if self.t > 0:
            self.label_5.setText(str(self.t))

            self.spinBox.setDisabled(True)
            self.spinBox_2.setDisabled(True)
            self.spinBox_3.setDisabled(True)
            self.pushButton_run.setDisabled(True)

            self.timer.start(1000)

    def timeout_slot(self):
        self.label_5.setText(str(self.t))
        self.t -= 1
        if self.t >= 0:
            pass
        else:
            self.check()
            self.t = self.total

    def stop(self):
        self.timer.stop()
        self.spinBox.setDisabled(False)
        self.spinBox_2.setDisabled(False)
        self.spinBox_3.setDisabled(False)
        self.pushButton_run.setDisabled(False)

    def check(self):
        TRANSFER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'transfer')  # 临时文件夹 路径

        # 得到中转站文件
        updatefile = self.read_db.get_updatefile([['is_wait', '=', '1']])
        for file in updatefile:
            uid = file[1]
            # 检测审核状态
            result = self.read_db.get_check([['uid', '=', uid]])
            if not result: continue
            # 通过审核
            if str(result[0][2]) == '1':
                # 删除并重建TRANSFER文件夹
                if os.path.exists(TRANSFER):
                    self.func.del_dir(TRANSFER)
                os.makedirs(TRANSFER)

                # 创建中转ftp
                ftp_obj_1 = self.read_db.get_ftp([['id', '=', '1']])[0]
                my_ftp_1 = MyFTP(*ftp_obj_1[2:6])

                # 创建最终ftp
                ftp_obj_2 = self.read_db.get_ftp([['id', '=', file[4]]])[0]
                my_ftp_2 = MyFTP(*ftp_obj_2[2:6])

                # 下载通过的项目
                my_ftp_1.download_file(os.path.join(ftp_obj_1[-1], file[5], file[1]).replace('\\', '/'),
                                       os.path.join(os.path.dirname(os.path.abspath(__file__)), 'transfer'))

                # 得到TRANSFER所有文件路径
                listname = []
                listname = self.func.listdir(TRANSFER, listname)

                # 上传文件到最终服务器
                for filename in listname:
                    with open(filename, 'rb') as f:
                        my_ftp_2.upload_file(ftp_obj_2[-1], file[5], file[1], os.path.split(filename)[-1], f)
                my_ftp_2.close()
            if str(result[0][2]) == '1' or str(result[0][2]) == '2':
                # 更新待审核状态
                self.read_db.update_updatefile({'is_wait': 0}, {'id': file[0]})

                # 删除中转文件
                my_ftp_1.del_file(os.path.join(ftp_obj_1[-1], file[5], file[1]).replace('\\', '/'))

            # 关闭ftp连接
            if 'my_ftp_1' in locals().keys():
                my_ftp_1.close()
            if 'my_ftp_2' in locals().keys():
                my_ftp_2.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinCheck()
    win.show()
    sys.exit(app.exec_())
