# Com este template conseguimos importar arquivos de outros módulos

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
                # ../../ (duas pastas anteriores = acima)
            )
        )
    )
except ImportError:
    raise

from pacote1.modulo1 import variavel1
variavel2 = 'variavel2'
