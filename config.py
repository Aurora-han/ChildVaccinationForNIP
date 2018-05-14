class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  "mysql+pymysql://root@localhost:3306/childvaccinationfornip_mis"