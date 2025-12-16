import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    OWL_FILE_PATH = os.path.join(os.path.dirname(__file__), 'ontology', 'shapes.owl')