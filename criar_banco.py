import sqlite3

conn = sqlite3.connect("aluguel_carros.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS alugueis;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS veiculos;

CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    telefone TEXT
);

CREATE TABLE veiculos (
    id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    placa TEXT UNIQUE NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE alugueis (
    id_aluguel INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_veiculo INTEGER,
    data_inicio TEXT,
    data_fim TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo)
);

-- Dados iniciais
INSERT INTO clientes (nome, cpf, telefone) VALUES
('Joao da Silva', '12345678901', '82999999999');

INSERT INTO veiculos (modelo, placa, status) VALUES
('Gol 1.0', 'ABC1234', 'Disponivel'),
('HB20', 'XYZ9876', 'Disponivel');
""")

conn.commit()
conn.close()

print("Banco criado com sucesso.")