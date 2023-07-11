""" Descrição rápida e simples.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer quis augue id
diam luctus porttitor at in justo. Fusce dapibus fringilla lectus a ornare.
Pellentesque ullamcorper dolor eros, non molestie metus mattis non. Nullam in
sodales arcu, at laoreet nunc. Cras at facilisis lectus. Pellentesque blandit
sapien eu velit cursus, id venenatis mi consectetur. Orci varius natoque
penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi
dapibus leo vitae ullamcorper auctor. Etiam pulvinar convallis justo, sed
tempus eros tincidunt ut. Nunc pulvinar, lorem vitae aliquam consectetur,
nunc enim finibus enim, sed tristique est massa sit amet mi. Fusce nunc
turpis, tempus quis est sit amet, pretium dapibus sapien.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
inceptos himenaeos. Sed consequat dapibus ligula. Donec libero metus,
condimentum ac libero sed, feugiat dapibus nibh. Integer quis risus augue.
Sed non ultricies ex, vitae vestibulum massa. Curabitur imperdiet, dolor
vitae ultrices commodo, sapien leo bibendum tortor, sit amet facilisis
sapien nulla at felis. Etiam vulputate et metus quis semper. Maecenas
non magna erat. Cras sed felis justo. Cras vitae ipsum nisl. Vestibulum
in metus vitae enim imperdiet cursus ac in leo. Nam in nibh sit amet lorem
egestas varius. Praesent mattis diam pulvinar dapibus egestas. In hac
habitasse platea dictumst.
"""

variavel_1 = 'valor 1'


def soma(x, y):
    """
    Soma x e y

    :parametro x: Primeiro número
    :type x: int or float
    :parametro y: Segundo número
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y


def multiplica(x, y, z=None):
    """
    Multiplica x, y, z

    Multiplica x, y e z. O programador poderá omitir a variável z caso
    não tenha necessidade de usá-la.

    :parametro x: Primeiro número
    :type x: int or float
    :parametro y: Segundo número
    :type y: int or float
    :parametro z: Terceiro número (opcional)
    :type z: int or float

    :return: A multiplicação entre x, y e z
    :rtype: int or float
    """
    if z:
        return x * y
    else:
        return x * y * z


variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'
