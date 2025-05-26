CREATE_TABLE_ENDERECO = """
CREATE TABLE IF NOT EXISTS Endereco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    logradouro TEXT NOT NULL,
    numero TEXT NOT NULL,
    complemento TEXT,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    uf TEXT NOT NULL,
    cep TEXT NOT NULL
);
"""
INSERT_ENDERECO = """
INSERT INTO Endereco (logradouro, numero, complemento, bairro, cidade, uf, cep)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""
UPDATE_ENDERECO = """
UPDATE Endereco
SET logradouro = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, uf = ?, cep = ?
WHERE id = ?;
"""
DELETE_ENDERECO = """
DELETE FROM Endereco
WHERE id = ?;
"""
GET_ENDERECO_BY_ID = """
SELECT id, logradouro, numero, complemento, bairro, cidade, uf, cep
FROM Endereco
WHERE id = ?;
"""
GET_ENDERECOS_BY_PAGE = """
SELECT id, logradouro, numero, complemento, bairro, cidade, uf, cep
FROM Endereco
ORDER BY logradouro ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_CIDADE = """
SELECT id, logradouro, numero, complemento, bairro, cidade, uf, cep
FROM Endereco
WHERE cidade = ?
ORDER BY logradouro ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_BAIRRO = """
SELECT id, logradouro, numero, complemento, bairro, cidade, uf, cep
FROM Endereco
WHERE bairro = ?
ORDER BY logradouro ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_UF = """
SELECT id, logradouro, numero, complemento, bairro, cidade, uf, cep
FROM Endereco
WHERE uf = ?
ORDER BY logradouro ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_CEP = """
SELECT id, logradouro, numero, complemento, bairro, cidade, uf, cep
FROM Endereco
WHERE cep = ?
ORDER BY logradouro ASC
LIMIT ? OFFSET ?;
"""
