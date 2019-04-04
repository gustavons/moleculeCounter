import unittest

import app.mainContagemPronto as contar


class TestContagem(unittest.TestCase):
    def setUp(self):
        self.analizar = contar

    def test_molecula1_returns_correct_result(self):
        self.assertEqual({'H': 2, 'C': 4}, self.analizar.analise('../test/arquivos/1.txt',-1)[0])

    def test_molecula2_returns_correct_result(self):
        self.assertEqual({'H': 4, 'N': 2, 'C': 1, 'O': 1}, self.analizar.analise('../test/arquivos/2.txt',-1)[0])

    def test_molecula3_returns_correct_result(self):
        self.assertEqual({'Al': 2, 'H': 2, 'O': 6, 'Si': 1}, self.analizar.analise('../test/arquivos/3.txt',-1)[0])

    def test_molecula4_returns_correct_result(self):
        self.assertEqual({'As': 2, 'H': 0, 'O': 3}, self.analizar.analise('../test/arquivos/4.txt',-1)[0])


    def test_molecula5_returns_correct_result(self):
        self.assertEqual({'H': 5, 'C': 5, 'S': 1}, self.analizar.analise('../test/arquivos/5.txt',-1)[0])

    def test_molecula6_returns_correct_result(self):
        self.assertEqual({'H': 11, 'C': 4, 'P': 1}, self.analizar.analise('../test/arquivos/6.txt',-1)[0])
    def test_molecula7_returns_correct_result(self):
        self.assertEqual({'H': 10, 'C': 4, 'S': 1}, self.analizar.analise('../test/arquivos/7.txt',-1)[0])

    def test_molecula8_returns_correct_result(self):
        self.assertEqual({'H': 5, 'C': 5, 'S': 1}, self.analizar.analise('../test/arquivos/8.txt',-1)[0])

    def test_molecula9_returns_correct_result(self):
        self.assertEqual({'H': 12, 'C': 4, 'S': 1}, self.analizar.analise('../test/arquivos/9.txt',-1)[0])

    def test_molecula10_returns_correct_result(self):
        self.assertEqual({'C': 6, 'H': 11,'Na': 3, 'O': 7}, self.analizar.analise('../test/arquivos/10.txt', -1)[0])

    def test_molecula11_returns_correct_result(self):
        self.assertEqual({'H': 2, 'O': 1}, self.analizar.analise('../test/arquivos/11.txt', -1)[0])


    # def test_molecula12_returns_correct_result(self):
    #     self.assertEqual({'C': 20, 'H': 24, 'N': 2, 'O': 1, 'S': 1}, self.analizar.analise('../test/arquivos/12.txt', -1)[0])

    #
    def test_molecula15_returns_correct_result(self):
        self.assertEqual({'C': 2, 'H': 8, 'O': 8}, self.analizar.analise('../test/arquivos/15.txt', -1)[0])

    def test_molecula25_returns_correct_result(self):
        self.assertEqual({'H': 7, 'C': 3, 'O': 3, 'N': 1}, self.analizar.analise('../test/arquivos/25.txt',-1)[0])

    def test_molecula39_returns_correct_result(self):
        self.assertEqual({'H': 9, 'C': 4, 'O': 2, 'N': 3}, self.analizar.analise('../test/arquivos/39.txt',-1)[0])
    #
    def test_molecula219_returns_correct_result(self):
        self.assertEqual({'H': 20, 'C': 17, 'S': 1, 'N': 4}, self.analizar.analise('../test/arquivos/219.txt',-1)[0])

    def test_molecula680_returns_correct_result(self):
        self.assertEqual({'H': 6, 'C': 4, 'S': 2, 'O': 3, 'N': 4}, self.analizar.analise('../test/arquivos/680.txt',-1)[0])
    #
    def test_molecula927_returns_correct_result(self):
        self.assertEqual({'H': 8, 'C': 2, 'O': 7, 'P': 2}, self.analizar.analise('../test/arquivos/927.txt',-1)[0])

    def test_molecula805_returns_correct_result(self):
        self.assertEqual({'H': 7, 'C': 6, 'O': 1, 'N': 3}, self.analizar.analise('../test/arquivos/805.txt',-1)[0])



if __name__ == '__main__':
    unittest.main()