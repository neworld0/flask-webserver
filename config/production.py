from logging.config import dictConfig
from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='Y|tWr8^Po>t$:zo^y_0>ycIMot3,}0$<',
    url='ls-bf8c8b1e79db2d507f0eda93887b0dfc674ac516.cmpkivnjfsnu.ap-northeast-2.rds.amazonaws.com',
    db='flask_webserver')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf9w\xba\x02\xba\x92*\xf1\xdcS\xa1\xe8\xd6\x0e77'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
