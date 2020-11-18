import os

from flask_script import Manager

from project import create_app

# 调用专门的方法创建应用实例，写入环境变量不需要修改代码
app = create_app(os.environ.get('PROJECT_CONFIG') or 'default')

# # 创建主路由
# @app.route('/')
# def index():
#     return 'Hello world!'

manager = Manager(app)

if __name__ == '__main__':
    manager.run()