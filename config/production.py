from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'~\x8cP\x05\xa4\x1a\xbe\xf9%+L\xbe\x83\x80\x87\xb0'
