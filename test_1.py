from programa import imprimir_nombre
from io import StringIO

def test_imprimir_nombre(capsys):
    imprimir_nombre('edgar')
    stdout, stderr = capsys.readouterr()
    assert stdout == 'Hola edgar\n'