import unittest

import app.mainContagemPronto as contar


class TestContagem(unittest.TestCase):
    def setUp(self):
        self.analizar = contar


    def test_molecula25_returns_correct_result(self):
        self.assertEqual({'H': 7, 'C': 3, 'O': 3, 'N': 1}, self.analizar.analise('../test/arquivos/25.txt',-1)[0])

    def test_molecula39_returns_correct_result(self):
        self.assertEqual({'H': 9, 'C': 4, 'O': 2, 'N': 3}, self.analizar.analise('../test/arquivos/39.txt',-1)[0])

    def test_molecula680_returns_correct_result(self):
        self.assertEqual({'H': 8, 'C': 4, 'S': 2, 'O': 3, 'N': 4}, self.analizar.analise('../test/arquivos/680.txt',-1)[0])

    def test_molecula927_returns_correct_result(self):
        self.assertEqual({'H': 8, 'C': 2, 'O': 7, 'P': 2}, self.analizar.analise('../test/arquivos/927.txt',-1)[0])

    def test_molecula805_returns_correct_result(self):
        self.assertEqual({'H': 8, 'C': 6, 'O': 1, 'N': 3}, self.analizar.analise('../test/arquivos/805.txt',-1)[0])
if __name__ == '__main__':
    unittest.main()