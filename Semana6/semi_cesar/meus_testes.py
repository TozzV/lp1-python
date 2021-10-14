import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
cesar = getattr(undertest, 'cesar', None)

class PublicTests(unittest.TestCase):

    def meu_teste(self):
        assert cesar("2! Exemplo", 4) == "2! Ebiqtps"
    
    def meu_teste2(self):
        assert cesar("v1t0r", 2) == "x1v0t"
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
