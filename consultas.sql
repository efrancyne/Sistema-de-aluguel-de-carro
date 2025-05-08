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


INSERT INTO clientes (nome, cpf, telefone) VALUES
('João da Silva', '12345678901', '82-98888-1111'),
('Maria Oliveira', '98765432100', '82-97777-2222'),
('Carlos Souza', '11122233344', '82-96666-3333');

INSERT INTO veiculos (modelo, placa, status) VALUES
('Gol 1.0', 'ABC-1234', 'Disponível'),
('Fiat Uno', 'DEF-5678', 'Disponível'),
('HB20 1.6', 'GHI-9012', 'Alugado');

INSERT INTO alugueis (id_cliente, id_veiculo, data_inicio, data_fim) VALUES
(1, 3, '2025-05-01', '2025-05-05');



SELECT * FROM clientes;
SELECT * FROM veiculos;