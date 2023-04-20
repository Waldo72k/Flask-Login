class Config:
    SECRET_KEY = 'B!1weNAt1t&%kvhUI*S&'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'vgdb'

config={
    'development':DevelopmentConfig
}