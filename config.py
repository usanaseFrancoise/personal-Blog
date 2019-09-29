import os 


class Config:
    # SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRECK_MODIFICATIONS=True
    SECRET_KEY=('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_TLS=False
    MAIL_USE_SSL=True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://fanny:havugima@2019@localhost/blogs"
    QUOTES_URL='http://quotes.stormconsultancy.co.uk/random.json'


class ProdConfig(Config):

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fanny:havugima@localhost/pitches'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fanny:havugima@2019@localhost/blogstest'

class DevConfig(Config):
    DEBUG = True 

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}