import unittest
from src.main import soma


class Testsoma(unittest.TestCase):
    def test_retorno_soma_10(self):
        self.assertEqual(soma(10, 10), 20)
