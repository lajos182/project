from flask import Flask

from config import config
from extensions import config_extensions
from project.views import config_blueprint

def create_app(config_name):
    # 创建应用的对象
    app = Flask(__name__)
    # 配置初始化
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 配置扩展
    config_extensions(app)
    # 配置蓝本
    config_blueprint(app)
    # 返回对象

    return app