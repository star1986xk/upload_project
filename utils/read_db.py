import re
import json
from PyQt5.QtCore import QSettings
from utils.db_class import DBClass


class ReadDB():
    def __init__(self):
        self.db = self.get_db()

    def get_db(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        host = settings.value('host')
        port = settings.value('port')
        user = settings.value('user')
        password = settings.value('password')
        password = re.sub('[479]', '', password)
        database = settings.value('database')
        SQL = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': database,
            'charset': 'utf8'
        }
        return DBClass(SQL)

    def get_info(self):
        info = self.db.select_condition('info', [['id', '=', '1']])
        return info

    def update_info(self, info_obj, condition):
        self.db.update_many('info', [info_obj], [condition])

    def get_role(self):
        role = self.db.select_condition('role_ftp_view')
        role_d = {}
        for r in role:
            id = role_d.get(r[0])
            if id:
                role_d[r[0]][2].append(r[2])
            else:
                role_d[r[0]] = [r[0], r[1], [r[2]]]
        return [[r[0], r[1], json.dumps(r[2], ensure_ascii=False)] for r in role_d.values()]

    def get_role_ftp(self, role_id):
        role_ftp = self.db.select_condition('role_ftp_view', [['ftp_id', '!=', '1'], ['role_id', '=', role_id]])
        return [str(ftp[3]) + '_' + ftp[2] for ftp in role_ftp]

    def add_role(self, role_obj):
        return self.db.insert_many('role', [role_obj])

    def update_role(self, role_obj, condition):
        self.db.update_many('role', [role_obj], [condition])

    def delete_role(self, role_id):
        self.db.delete_many('role', [{'id': role_id}])

    def add_role_ftp(self, role_ftp):
        return self.db.insert_many('role_ftp', role_ftp)

    def delete_role_ftp(self, role_id):
        self.db.delete_many('role_ftp', [{'role_id': role_id}])

    def get_user(self):
        user = self.db.select_condition('user_role_view')
        return user

    def get_login(self, username, password):
        login = self.db.select_condition('[user]', [['username', '=', username], ['password', '=', password]])
        return login

    def add_user(self, user_obj):
        self.db.insert_many('[user]', [user_obj])

    def update_user(self, user_obj, condition):
        self.db.update_many('[user]', [user_obj], [condition])

    def delete_user(self, user_id):
        self.db.delete_many('[user]', [{'id': user_id}])

    def get_ftp(self, condition=None):
        ftp = self.db.select_condition('ftp', condition)
        return ftp

    def add_ftp(self, ftp_obj):
        self.db.insert_many('ftp', [ftp_obj])

    def update_ftp(self, ftp_obj, condition):
        self.db.update_many('ftp', [ftp_obj], [condition])

    def delete_ftp(self, user_id):
        self.db.delete_many('ftp', [{'id': user_id}])

    def get_word_view(self, condition=None):
        word = self.db.select_condition('keyword_view', condition)
        return word

    def get_word(self, condition=None):
        word = self.db.select_condition('keyword', condition)
        return word

    def add_word(self, word_list, user_id):
        self.db.insert_many('keyword', [{'word': word, 'role_id': user_id} for word in word_list])

    def delete_word(self, word_id):
        self.db.delete_many('keyword', [{'id': word_id}])

    def get_project(self, condition=None):
        project = self.db.select_condition('project_view', condition, order=['project_date'], by='DESC')
        return project

    def get_baidu(self):
        baidu = self.db.select_condition('baidu_key', [['id', '=', '1']])
        return baidu[0]

    def update_baidu(self, baidu_obj):
        self.db.update_many('baidu_key', [baidu_obj], [{'id': '1'}])

    def add_update(self, update_obj):
        return self.db.insert_many('update_file', [update_obj])

    def get_updatefile(self, condition=None):
        updatefile = self.db.select_condition('update_file', condition)
        return updatefile

    def update_updatefile(self, updatefile, condition):
        self.db.update_many('update_file', [updatefile], [condition])

    def get_check(self, condition=None):
        check = self.db.select_condition('check_view', condition)
        return check
