# Aqui se importa de funciones.py los 2 metodos
from funciones import check_char
from funciones import caps_switch

# Se realizan 5 test, uno para cada caso


# Caso A
def test_1():
    assert check_char("A") == "0"


# Caso switch
def test_2():
    assert caps_switch("a") == "A"


# Caso B
def test_3():
    assert check_char("aB") == "Error B"


# Caso C
def test_4():
    assert check_char("a2") == "Error C"


# Caso D
def test_5():
    assert check_char(123) == "Error D"
