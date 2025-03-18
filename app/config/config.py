from app.database.config import DATABASE_CONFIG

class Config:
    """Configuração base usada por todos os ambientes."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelopmentConfig(Config):
    """Configurações específicas para o ambiente de desenvolvimento."""
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = DATABASE_CONFIG["DATABASE_URI"]
    
    

class ProductionConfig(Config):
    """Configurações específicas para o ambiente de produção."""
    DEBUG = False
    TESTING = False
    
    SQLALCHEMY_DATABASE_URI = DATABASE_CONFIG["DATABASE_URI"]
    
    
# Dicionário para mapear os ambientes
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
