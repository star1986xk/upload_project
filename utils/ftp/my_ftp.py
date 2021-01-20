import os
import re
from utils.ftp.ftplib import FTP

from _io import _IOBase


class MyFTP():

    def __init__(self, host: str, port: str, username: str, password: str):
        try:
            self.host = host
            self.ftp = FTP()
            self.ftp.encoding = 'gbk'
            self.ftp.set_pasv(False)
            self.ftp.connect(host, int(port))
            self.ftp.login(username, password)
            self.ftp.cwd('/')
        except Exception as e:
            raise ValueError('MyFTP:' + str(e))

    def upload_file(self, basedir: str, projectdir: str, subdir: str, filename: str, fp: _IOBase):
        '''
        上传文件
        :param remotepath: 上传路径
        :param fp: 文件
        :return:
        '''
        try:
            self.ftp.cwd(basedir)
        except Exception:
            self.ftp.mkd(basedir)
            self.ftp.cwd(basedir)
        try:
            self.ftp.cwd(projectdir)
        except Exception:
            self.ftp.mkd(projectdir)
            self.ftp.cwd(projectdir)
        try:
            self.ftp.cwd(subdir)
        except Exception:
            self.ftp.mkd(subdir)
            self.ftp.cwd(subdir)

        bufsize = 1024
        self.ftp.storbinary('STOR ' + filename, fp, bufsize, ip=self.host)
        self.ftp.set_debuglevel(0)

    def download_file(self, remotepath: str, localpath: str):
        '''
        下载文件夹
        :param remotepath: 服务器文件夹路径
        :param localpath: 保存文件夹路径
        :return:
        '''
        self.ftp.cwd(remotepath)  # 设置FTP远程目录(路径)

        with self.ftp.transfercmd('LIST') as conn, conn.makefile('r', encoding='gbk') as fp:
            f_list = fp.readlines()
            for f in f_list:
                filename = re.search('\d\d:\d\d (.*?)\n', f)[1]
                local_path = os.path.join(localpath, filename)
                with open(local_path, "wb") as f:
                    self.ftp.retrbinary('RETR ' + filename, f.write)  # 保存FTP上的文件

        self.ftp.set_debuglevel(0)  # 关闭调试

    def del_file(self, filename):
        '''
        删除文件夹及文件夹下全部文件
        :param filename: 文件夹路径
        :return:
        '''
        self.ftp.cwd(filename)  # 设置FTP远程目录(路径)
        with self.ftp.transfercmd('LIST') as conn, conn.makefile('r', encoding='gbk') as fp:
            f_list = fp.readlines()
            for f in f_list:
                name = re.search('\d\d:\d\d (.*?)\n', f)[1]
                self.ftp.sendcmd('DELE ' + name)
        self.ftp.sendcmd('DELE ' + filename)
        filename = filename.rsplit('/', 1)[0]
        self.ftp.cwd(filename)
        # 判断项目目录是否为空
        with self.ftp.transfercmd('LIST') as conn, conn.makefile('r', encoding='gbk') as fp:
            f_list = fp.readlines()
            if f_list:
                return
        # 为空,删除目录
        self.ftp.sendcmd('DELE ' + filename)

    def close(self):
        self.ftp.quit()


if __name__ == '__main__':
    FTP_CONNECT = {
        'host': 'yun.fjhczsgc.com',
        'port': 21,
        'username': 'test',
        'password': 'Hh@121212'
    }
    my_ftp = MyFTP(**FTP_CONNECT)
    # my_ftp.download_file('/test/中转站/项目/子项目',
    #                      os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    #                                   'transfer'))
    my_ftp.del_file('/test/中转站/项目/子项目')
    my_ftp.close()
