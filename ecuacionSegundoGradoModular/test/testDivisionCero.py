from src.ecuacionDeSegundoGrado import raizEcuacionSegundoGrado
import pytest

def testDivisionPorCero():
    assert raizEcuacionSegundoGrado(0,1,1) == None