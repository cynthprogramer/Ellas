import urllib.parse as parse
import secrets


class Config:
    SECRET_KEY = secrets.token_hex(16)
    # SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:194050@127.0.0.1:3306/teste'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@127.0.0.1:3306/ellasbanco'.format(parse.quote("194050"))