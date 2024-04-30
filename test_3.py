from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Edgar Moreano"
    edad = 45
    estatura = 1.66
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: Edgar Moreano\nEdad: 45\nEstatura: 1.66\n"
