import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
bubblesort = getattr(undertest, 'bubblesort', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        lista = [1,9,3,2]
        bubblesort(lista)
        assert lista == [1,2,3,9]

    def meu_teste(self):
        lista = [1,7,3,3]
        bubblesort(lista)
        assert lista == [1,3,3,7]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
