from . import app


class Config:
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "newspaper_blog"
    DATABASE = app.instance_path + '/news.db'
    REPLICA = app.instance_path + "/replica"