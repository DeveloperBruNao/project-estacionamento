class Config: # Configuração do banco de dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///estacionamento.db'  # Caminho do banco SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desabilita o rastreamento de modificações
