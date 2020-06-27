import sqlite3

con = sqlite3.connect('recibo.db')

c = con.cursor()

tabela_cad_empresa = """
CREATE TABLE cad_empresa (
    id_empresa INTEGER PRIMARY KEY,
    empresa TEXT,
    razao TEXT,
    cnpj VARCHAR(14),
    endereco TEXT
)
"""
tabela_cad_prestador = """
CREATE TABLE cad_prestador(
    id_prestador INTEGER PRIMARY KEY,
    nome_prestador TEXT,
    cpf VARCHAR(11),
    identidade VARCHAR(9),
    emissor TEXT,
    insc_municipal INT,
    data_nasc DATE,
    nome_mae TEXT NOT NULL,
    endereco_prestador TEXT NOT NULL
)
"""
tabela_recibo = """
CREATE TABLE recibos (
    id_recibo INTEGER PRIMARY KEY,
    servico TEXT,
    valor_bruto REAL,
    valor_liquido REAL,
    pis REAL,
    inss REAL,
    irrf REAL,
    iss REAL,
    recibo_pdf BLOB
)
"""

c.execute(tabela_cad_empresa)
c.execute(tabela_cad_prestador)
c.execute(tabela_recibo)
con.commit()
con.close()