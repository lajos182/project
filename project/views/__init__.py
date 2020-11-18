
from .auth import auth

# 专门配置蓝本
DEFAULT_BLUEPRINT = (
    (auth, '/'),
)

def config_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)