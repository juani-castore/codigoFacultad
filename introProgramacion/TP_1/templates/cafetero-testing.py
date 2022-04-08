import unittest

from numpy import NaN

# Se importa el código a testear.
from cafetero import filtrar_solo_CAFE, es_cafetero, n_esimo_cafetero, cafeteros_entre, generar_mensaje

#####################################################################
class TestFiltrarSoloCafe(unittest.TestCase):

    def test_solo_nros(self):
        self.assertEqual(filtrar_solo_CAFE("1234"),"")
        self.assertEqual(filtrar_solo_CAFE("1"),"")
        self.assertEqual(filtrar_solo_CAFE("0"),"")
        self.assertEqual(filtrar_solo_CAFE("9999"),"")
    
    def test_str_vacio(self):
        self.assertEqual(filtrar_solo_CAFE(""),"")

    def test_str_minusculas(self):
        self.assertEqual(filtrar_solo_CAFE("abcdefghijklmnopqrstuvwxyz"),"")
        self.assertEqual(filtrar_solo_CAFE("cafe"),"")
        self.assertEqual(filtrar_solo_CAFE("ccccaaaaffffeeeee"),"")

    def test_mayusculas(self):
        self.assertEqual(filtrar_solo_CAFE("CAFE"),"CAFE")
        self.assertEqual(filtrar_solo_CAFE("ABCCAFEXYZ"),"ACCAFE")
        self.assertEqual(filtrar_solo_CAFE("CcAaFfEe"),"CAFE")
        self.assertEqual(filtrar_solo_CAFE("CafE"),"CE")

    
    def test_repetidas(self):
        self.assertEqual(filtrar_solo_CAFE("CCCCCCAAAAAFFFFFEEEEE"),"CCCCCCAAAAAFFFFFEEEEE")
        self.assertEqual(filtrar_solo_CAFE("CAFECAFECAFE"),"CAFECAFECAFE")
    
        
class TestEsCafetero(unittest.TestCase):
    
    def test_nro_cafetero(self):
        self.assertEqual(es_cafetero(51966),True)
        self.assertEqual(es_cafetero(314110),True)
        self.assertEqual(es_cafetero(641790),True)
        self.assertEqual(es_cafetero(822014),True)
        self.assertEqual(es_cafetero(831460),True)
    
    def test_nro_no_cafetero(self):
        self.assertEqual(es_cafetero(1),False)
        self.assertEqual(es_cafetero(100),False)
        self.assertEqual(es_cafetero(100000),False)
        self.assertEqual(es_cafetero(999999999),False)
        self.assertEqual(es_cafetero(123456789),False)

    def test_letras_validas_repetidas(self):
        self.assertEqual(es_cafetero(831470),False)
        self.assertEqual(es_cafetero(3405695742),False)

    
    def test_orden_letras_validas(self):
        self.assertEqual(es_cafetero(45036),False)
        self.assertEqual(es_cafetero(65226),False)

    def test_letras_no_validas(self):
        self.assertEqual(es_cafetero(831467),False)
        self.assertEqual(es_cafetero(903934),False)
        self.assertEqual(es_cafetero(13287405),False)
    

class TestNesimoCafetero(unittest.TestCase):

    # def test_n_negativo_o_0(self):
    #     self.assertEqual(n_esimo_cafetero(0),"")
    #     self.assertEqual(n_esimo_cafetero(-10),"")
    #     self.assertEqual(n_esimo_cafetero(-20),"")
    
    def test_n_valido(self):
        self.assertEqual(n_esimo_cafetero(1),51966)
        self.assertEqual(n_esimo_cafetero(10),641790)
        self.assertEqual(n_esimo_cafetero(100),1880041)


class TestCafeterosEntreNyM(unittest.TestCase):
    def test_n_y_m_valido(self):
        self.assertEqual(cafeteros_entre(1,1000),[])
        self.assertEqual(cafeteros_entre(1000,100000),[51966])
        self.assertEqual(cafeteros_entre(99999,200000),[117502,183038])

class TestGenrarMensaje(unittest.TestCase):
    def test_generar_si_es_cafetero(self):
        self.assertEqual(generar_mensaje(True,51966),"El " + str(51966) + " es cafetero." )

    def test_generar_no_es_cafetero(self):
        self.assertEqual(generar_mensaje(False,1),"El " + str(1) + " no es cafetero." )


    # def test_...(self):
    #     ...
## y así con el resto de las funciones a testear.

unittest.main()
