CREATE_TABLE_ENDERECO = """
CREATE TABLE IF NOT EXISTS Endereco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rua TEXT NOT NULL,
    numero TEXT NOT NULL,
    complemento TEXT,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    cep TEXT NOT NULL
);
"""
INSERT_ENDERECO = """
INSERT INTO Endereco (rua, numero, complemento, bairro, cidade, estado, cep)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""
UPDATE_ENDERECO = """
UPDATE Endereco
SET rua = ?, numero = ?, complemento = ?, bairro = ?, cidade = ?, estado = ?, cep = ?
WHERE id = ?;
"""
DELETE_ENDERECO = """
DELETE FROM Endereco
WHERE id = ?;
"""
GET_ENDERECO_BY_ID = """
SELECT id, rua, numero, complemento, bairro, cidade, estado, cep
FROM Endereco
WHERE id = ?;
"""
GET_ENDERECOS_BY_PAGE = """
SELECT id, rua, numero, complemento, bairro, cidade, estado, cep
FROM Endereco
ORDER BY rua ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_CIDADE = """
SELECT id, rua, numero, complemento, bairro, cidade, estado, cep
FROM Endereco
WHERE cidade = ?
ORDER BY rua ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_BAIRRO = """
SELECT id, rua, numero, complemento, bairro, cidade, estado, cep
FROM Endereco
WHERE bairro = ?
ORDER BY rua ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_UF = """
SELECT id, rua, numero, complemento, bairro, cidade, estado, cep
FROM Endereco
WHERE estado = ?
ORDER BY rua ASC
LIMIT ? OFFSET ?;
"""
GET_ENDERECOS_BY_CEP = """
SELECT id, rua, numero, complemento, bairro, cidade, estado, cep
FROM Endereco
WHERE cep = ?
ORDER BY rua ASC
LIMIT ? OFFSET ?;
"""
