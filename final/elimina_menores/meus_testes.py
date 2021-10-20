import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
elimina_menores = getattr(undertest, 'elimina_menores', None)

class PublicTests(unittest.TestCase):

    def meu_teste(self):
        lista3 = [1,2,3,4,5,1,2,3]
        assert elimina_menores(2, lista3) == 2
        assert lista3 == [2,3,4,5,2,3]
        
    def test_exemplo_2(self):
        lista2 = [-5,0,-3,7,2.5,12]
        assert elimina_menores(12, lista2) == 5
        assert lista2 == [12]

     def test_exemplo_3(self):
        lista2 = [-2.7,0,3,1337.7,2.5,1,3]
        assert elimina_menores(1337.7, lista2) == 6
        assert lista2 == [1337.7]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
