import logging
import os
from logging.handlers import RotatingFileHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    # 设置日志的记录级别
    logging.basicConfig(level=logging.DEBUG)
    # 日至文件
    log_dir = os.path.join(BASE_DIR, 'logs/project.log')
    # 创建日志记录器、指明日志保存路径、每个日至的大小、保存日志文件的上线
    file_log_handler = RotatingFileHandler(log_dir, maxBytes=30*1024*1024, backupCount=10)
    # 创建日志书写格式
    formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s')
    # 为刚刚创建的日志记录器设置日志格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具添加记录对象
    logging.getLogger().addHandler(file_log_handler)
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'U0Hja2HgRJe+P5TMfB7C7E68uCRLSUUVrnoUrxcp5EQ='
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 关闭数据库追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件发送
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.163.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '18258720901@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '123456'
    # 使用本地的bootstrap库
    BOOTSTRAP_SERVER_LOCAL = True
    # 文件上传
    MAX_CONTEXT_LENGTH = 8*1024*1024
    UPLOAD_PHOTOS_DEST = os.path.join(BASE_DIR, 'project/static/upload')
    
    # 初始化函数，即使没有内容也建议写上，可以在需要的时候完成特定初始化
    @staticmethod
    def init_app(app):
        pass
    
# 默认环境配置
class DefaultConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://roo:jiang@localhost:3306/'
    
# 开发环境配置
class DevelopConfig(Config):
    DEBUG = True
    TESTING = False

# 测试环境配置
class TestingConfig(Config):
    DEBUG = False
    TESTING = True

# 生产环境配置
class ProductConfig(Config):
    DEBUG = False
    TESTING = False
    
# 配置字典简化
config = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    'default':  DefaultConfig
}
