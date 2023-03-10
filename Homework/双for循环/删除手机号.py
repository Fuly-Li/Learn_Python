import pymysql

from pymysql.cursors import DictCursor
class MySqlUtils:
    def __init__(self, host=None, port=0, user=None, passwd=None, db=None,
                 charset='utf8'):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    passwd=passwd,  # password也可以
                                    db=db,  #数据库名称
                                    charset=charset,  # 如果查询有中文需要指定数据库编码
                                    cursorclass=DictCursor) #返回字典
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, fetchall=True):
        self.cursor.execute(sql, args=args)
        if fetchall:  #默认查询所有数据
            res = self.cursor.fetchall()
        else:
            res = self.cursor.fetchone()
        return res

    def close_db(self):#关闭游标、连接
        self.cursor.close()
        self.conn.close()


mysql_utils = MySqlUtils(host='47.242.43.178', user='wowed', passwd='Wowed159Qaz!', port=3306, db='wowed_activity')

res = mysql_utils.query('select device_id from login_award_chat_card')
for i in range(len(res)):
    print(res[i]['device_id'])

mysql_utils.close_db()