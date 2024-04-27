import os

DEBUG =True
APP_NAME = "Flask_Course"
SECRET_KEY="secretkey@123jawk"
SQLALCHEMY_TRACK_MODIFICATIONS=False
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_HOST = 'localhost'  # ou l'adresse IP de votre serveur MySQL
MYSQL_DB = 'flask_exam_db'
FLASK_MIGRATE = True
FLASK_MIGRATE_AUTO_MIGRATE = True

SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,"db.sqlite")
NO_IMG="https://th.bing.com/th/id/OIP.gV1cXI_SNBK_nU1yrE_hcwHaGp?rs=1&pid=ImgDetMain"