import unittest
from main import soma

caminho = "C:\\Users\\wmare\\Desktop\\Curso_Atual\\src\\main"


class TesteSoma(unittest.TestCase):
    def test_retorno_soma_10(self):
        self.assertEqual(soma(10, 10), 20)
