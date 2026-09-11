import sqlite3

def conectar():
    conn = sqlite3.connect("biblioteca.db")
    return conn

def criar_tabela(nome_banco="biblioteca.db"):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL,
            status TEXT NOT NULL)
    """)

    conn.commit()
    conn.close()

def cadastro_livro(titulo, autor, ano_publicacao, nome_banco="biblioteca.db"):
    if titulo.strip() == "":
        return "Título está branco, coloque um título na seção de Título."
    elif autor.strip() == "":
            return "Autor em branco, ponha um autor na seção Autor."
    # RN01 - Limite de ano
    if ano_publicacao > 2026:
        return "Ano inválido, maior que 2026. Tá querendo botar um livro que não existe, irmão?"
    
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    # RN02 - Status padrão "Não Lido"
    cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, status) VALUES (?, ?, ?, 'Não Lido')", 
                   (titulo, autor, ano_publicacao))  

    conn.commit()
    conn.close()

    return "OK"

def delete_livro(id, nome_banco="biblioteca.db"):
    if id > 0:
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM livros WHERE id = ?", (id,))  
        linhas = cursor.rowcount

        if linhas > 0:
            conn.commit()
            conn.close()
            return 1
        else:
            conn.close()
            return "ID não encontrado. O ID precisa ser existente."
    else:
        return "ID inválido"

def update_status_livro(id, status, nome_banco="biblioteca.db"):
    # RN02 - Validação simples
    if status != "Não Lido" and status != "Lendo" and status != "Lido":
        return "Status inválido"

    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET status = ? WHERE id = ?", (status, id))
    modificados = cursor.rowcount

    if modificados > 0:
        conn.commit()
        conn.close()
        return 1
    else:
        conn.close()
        return "Livro não encontrado"

def getLivros(nome_banco="biblioteca.db"):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")  
    dados = cursor.fetchall()

    conn.close()
    return dados
