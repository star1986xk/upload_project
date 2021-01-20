from ftplib import FTP
import os


class MyFTP():

    def __init__(self, ip, port, username, password, ):

        self.ftp = FTP()
        self.ftp.encoding = 'gbk'
        self.ftp.connect(ip, int(port))
        self.ftp.login(username, password)
        self.ftp.set_pasv(False)

    def cwd(self, basedir, projectdir, subdir):
        self.ftp.cwd('/')
        self.ftp.cwd(basedir)
        try:
            self.ftp.cwd(projectdir)
        except Exception as e:
            self.ftp.mkd(projectdir)
            self.ftp.cwd(projectdir)
        try:
            self.ftp.cwd(subdir)
        except Exception as e:
            self.ftp.mkd(subdir)
            self.ftp.cwd(subdir)

    def close(self):
        self.ftp.quit()


if __name__ == '__main__':
    myftp = MyFTP('yun.fjhczsgc.com', '21', 'test', 'Hh@121212', )
    myftp.cwd('/test/中转站', '项目', '子上传')

