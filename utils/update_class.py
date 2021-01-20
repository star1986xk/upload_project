import os
import shutil
from PyQt5.QtCore import pyqtSignal, QThread

from utils.ftp.my_ftp import MyFTP


class UpdateClass(QThread):
    sig_one = pyqtSignal(int)
    sig_end = pyqtSignal(str, bool)

    def __init__(self, TEMP, update_obj, filenames, log, func, read_db):
        super().__init__()
        self.TEMP = TEMP
        self.update_obj = update_obj
        self.filenames = filenames
        self.log = log
        self.func = func
        self.read_db = read_db

        self.flag = True  # 审批标识，True:默认无需审批 False:识别出别人的关键词,需审批并且上传到中转服务器

    def run(self):
        try:
            self.log.logger.info('删除并重建temp文件夹')
            # 删除并重建temp文件夹
            if os.path.exists(self.TEMP):
                self.func.del_dir(self.TEMP)
            os.makedirs(self.TEMP)

            self.log.logger.info('上传文件copy到temp文件夹')
            # 上传文件copy到temp文件夹
            for filename in self.filenames:
                dirname, file = os.path.split(filename)
                shutil.copy(filename, os.path.join(self.TEMP, file))

            self.log.logger.info('得到temp所有文件路径')
            # 得到temp所有文件路径
            listname = []
            listname = self.func.listdir(self.TEMP, listname)

            self.log.logger.info('把压缩包全部解压缩')
            # 把压缩包全部解压缩
            for filename in listname:
                self.func.un_zip(filename, self.TEMP)

            self.log.logger.info('得到temp所有文件路径')
            # 得到temp所有文件路径
            listname = []
            listname = self.func.listdir(self.TEMP, listname)

            text_list = []
            keys = []

            self.log.logger.info('读取文件内文本')
            # 读取文件内文本
            for filename in listname:
                text = self.func.read(filename)
                if text:
                    text_list.append(text)

            self.log.logger.info('判断关键字')
            # 判断关键字
            if text_list:
                text_str = ' '.join(text_list)
                words = self.read_db.get_word()
                for word in words:
                    if word[1] in text_str:
                        keys.append(word[1])
                        if str(word[2]) != str(self.update_obj.get('user_id')):
                            self.flag = False
                keyword = '/'.join(keys) if keys else '无关键词'
            else:
                keyword = '未识别'
            self.update_obj['keyword'] = keyword

            self.log.logger.info('上传服务器')
            if self.flag:  # 无需审批
                ftp_obj = self.read_db.get_ftp([['id', '=', self.update_obj.get('ftp_id')]])[0]
                self.update_obj['is_wait'] = '0'
            else:  # 需审批
                ftp_obj = self.read_db.get_ftp([['id', '=', '1']])[0]
            my_ftp = MyFTP(*ftp_obj[2:6])
            for n, filename in enumerate(self.filenames):
                with open(filename, 'rb') as f:
                    my_ftp.upload_file(ftp_obj[-1], self.update_obj.get('project_name'), self.update_obj.get('uid'),
                                       os.path.split(filename)[-1], f)
                    self.sig_one.emit(int((n + 1) / len(self.filenames) * 100))
            my_ftp.close()
            self.read_db.add_update(self.update_obj)
            self.log.logger.info('上传服务器完成')
            self.sig_end.emit('上传成功', self.flag)
        except Exception as e:
            self.log.logger.warning('上传失败：' + str(e))
            self.sig_end.emit('上传失败：' + str(e), self.flag)
