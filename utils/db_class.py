# -*- coding: utf-8 -*-
import pymssql
from DBUtils.PooledDB import PooledDB


class DBClass(object):

    def __init__(self, SQL=None):
        self.SQL = SQL
        self.pool = self.create_pool()

    def create_pool(self):
        '''
        创建数据库连接池
        :return:连接池
        '''
        pool = PooledDB(creator=pymssql,
                        maxconnections=50,  # 连接池允许的最大连接数，0和None表示不限制连接数
                        mincached=15,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                        maxcached=0,  # 链接池中最多闲置的链接，0和None不限制
                        maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
                        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                        host=self.SQL['host'],
                        port=self.SQL['port'],
                        user=self.SQL['user'],
                        password=self.SQL['password'],
                        database=self.SQL['database'],
                        charset=self.SQL['charset'])
        return pool

    def getWhere(self, condition: list) -> (str, tuple):
        return (' where ' + ' and '.join([li[0] + ' ' + li[1] + ' %s' for li in condition]),
                tuple([str(li[2]) for li in condition])) if condition else ('', ())

    def getORDER(self, order: list, by: str):
        return ' ORDER BY ' + ','.join([li for li in order]) + ' ' + by if order else ''

    def select_count(self, table_name: str, condition: list = None) -> int:
        '''
        条件查询\n
        如:select count(*) from table1 where id=1 and name like '%xx%';\n
        传参数：[['id','=','1'],['name','like','%xx%']]\n
        @param table_name: 表名
        @param condition:[[字段,符号,值],[]...]
        @return: 查询后的数据条数
        '''
        try:
            (where, data) = self.getWhere(condition)
            con = self.pool.connection()
            cur = con.cursor()
            _sql = 'SELECT count(*) FROM ' + table_name + where + ';'
            cur.execute(_sql, data)
            result = cur.fetchall()
            con.commit()
            return result[0][0]
        except Exception as e:
            con.rollback()  # 事务回滚
            print(e)
            return None
        finally:
            cur.close()
            con.close()

    def select_condition(self, table_name: str, condition: list = None, order: list = None, by: str = 'ASC') -> list:
        '''
        条件查询\n
        如:select * from table1 where id=1 and name like '%xx%';\n
        传参数：[['id','=','1'],['name','like','%xx%']]\n
        @param table_name: 表名
        @param condition:[[字段,符号,值],[]...]
        @return: 查询后的数据集合
        '''
        try:
            (where, data) = self.getWhere(condition)
            con = self.pool.connection()
            cur = con.cursor()
            _sql = 'SELECT * FROM ' + table_name + where + self.getORDER(order, by) + ';'
            cur.execute(_sql, data)
            result = cur.fetchall()
            con.commit()
            return result
        except Exception as e:
            con.rollback()  # 事务回滚
            print(e)
            return None
        finally:
            cur.close()
            con.close()

    def select_desc(self, table_name):
        try:
            con = self.pool.connection()
            cur = con.cursor()
            _sql = 'SELECT top 1 * from ' + table_name + ' where IsChange=0 order by id desc;'
            cur.execute(_sql)
            result = cur.fetchall()
            _sql = 'update ' + table_name + ' set IsChange=9 where id=' + str(result[0][0]) + ';'
            cur.execute(_sql)
            con.commit()
            return result
        except Exception as e:
            con.rollback()  # 事务回滚
            print(e)
            return None
        finally:
            cur.close()
            con.close()

    def insert_many(self, table_name, obj_list):
        '''
        批量插入相同格式的一批数据\n
        如:\n
        insert table1(name,age) values('小明',30);\n
        insert table1(name,age) values('老王',30);\n
        可传参数:\n
        obj_list = [{'name':'小明','age':'10'},{'name':'老王','age':'30'}]\n
        @param table_name: 表名
        @param obj_list: [{'字段'：'值',,,},,,]
        @return: True|False
        '''
        try:
            con = self.pool.connection()
            cur = con.cursor()
            _sql = 'INSERT ' + table_name + '(' + ','.join([k for k in obj_list[0].keys()]) + ') VALUES(' + \
                   ','.join(['%s' for k in obj_list[0]]) + ');'
            datas = tuple(tuple(v for v in li.values()) for li in obj_list)
            cur.executemany(_sql, datas)
            con.commit()
            return int(cur.lastrowid)
        except Exception as e:
            con.rollback()  # 事务回滚
            print(e)
            return None
        finally:
            cur.close()
            con.close()

    def update_many(self, table_name, obj_list, condition_list):
        '''
        批量更新相同格式的一批数据\n
        如: \n
        update table1 set name='小明',age=10 where id=1;\n
        update table1 set name='老王',age=30 where id=2;\n
        可这样传参数:\n
        obj_list = [{'name':'小明','age':'10'},{'name':'老王','age':'30'}]\n
        condition_list = [{'id':'1'},{'id':'2'}]
        @param table_name: 表名
        @param obj_list: [{'字段'：'值',,,},,,]
        @param condition_list: [{'字段'：'值',,,},,,]
        @return:True|False
        '''
        try:
            con = self.pool.connection()
            cur = con.cursor()
            _sql = 'UPDATE ' + table_name + ' SET ' + ','.join(
                [k + '=%s' for k in obj_list[0].keys()]) + ' WHERE ' + \
                   ' and '.join([k + '=%s' for k in condition_list[0].keys()]) + ';'
            datas = tuple(
                tuple(obj.values()) + tuple(condition.values()) for obj, condition in zip(obj_list, condition_list))
            cur.executemany(_sql, datas)
            con.commit()
            return True
        except Exception as e:
            con.rollback()  # 事务回滚
            print(e)
            return None
        finally:
            cur.close()
            con.close()

    def delete_many(self, table_name, condition_list):
        '''
        批量删除\n
        如：\n
        delete from table1 where id=1 and name='xxx'\n
        delete from table1 where id=3 and name='yy'\n
        可传参数\n
        condition_list = [{id:'1','name':'xxx'},{id:'3','name':'yy'}]
        @param table_name: 表名
        @param condition_list: [{'字段': '值',,,},,,]
        @return: True|False
        '''
        try:
            con = self.pool.connection()
            cur = con.cursor()
            _sql = 'DELETE FROM ' + table_name + ' WHERE ' + ' and '.join(
                [k + '=%s' for k in condition_list[0].keys()]) + ';'
            datas = tuple(tuple(condition.values()) for condition in condition_list)
            cur.executemany(_sql, datas)
            con.commit()
            return True
        except Exception as e:
            con.rollback()  # 事务回滚
            print(e)
            return None
        finally:
            cur.close()
            con.close()

    def truncate_table(self, table_name):
        '''
        清空表数据
        :param table_name: 表名
        :return:
        '''
        try:
            con = self.pool.connection()
            cur = con.cursor()
            _sql = 'TRUNCATE TABLE ' + table_name + ';'
            cur.execute(_sql)
            con.commit()
            return True
        except Exception as e:
            con.rollback()  # 事务回滚
            print(e)
            return None
        finally:
            cur.close()
            con.close()
