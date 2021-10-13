import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
tem_afinidade = getattr(undertest, 'tem_afinidade', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l3 = ['bruno e marrone', 'joao', 'pedro', 'u2']
        l4 = ['joao', 'u2', 'jquest']
        assert tem_afinidade(l3, l4) == False
        

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
