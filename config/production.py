from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'webserver.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'JjK~n\xf7\x85A\xb3&F\x18\xa6f$\xc8'
