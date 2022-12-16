USERNAME = "root"
PASSWORD = "root"  #每个人设置的名字和账号会不同，这里是自己设定的账号密码
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'dot_view'  #这里是数据库文件名
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True