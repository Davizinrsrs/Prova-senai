import unittest
import sqlite3
import os
import database as db

class TesteBiblioteca(unittest.TestCase):

    def setUp(self):
        self.banco = "banco_teste.db"
        db.criar_tabela(self.banco)
    
    def tearDown(self):
        if os.path.exists(self.banco):
            os.remove(self.banco)

    def test_cadastro(self):
        # Testa cadastro e status padrão
        res = db.cadastro_livro("O Hobbit", "J.R.R. Tolkien", 1937, self.banco)
        self.assertEqual(res, "OK")

        conn = sqlite3.connect(self.banco)
        c = conn.cursor()
        c.execute("SELECT * FROM livros WHERE id = 1")
        livro = c.fetchone()
        conn.close()

        self.assertEqual(livro[1], "O Hobbit")
        self.assertEqual(livro[4], "Não Lido")

    def test_ano_futuro(self):
        # Testa RN01
        res = db.cadastro_livro("Salsichas Galácticas do Futuro", "Autor", 2030, self.banco)
        self.assertNotEqual(res, "OK")

if __name__ == "main":
    unittest.main()
