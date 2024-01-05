"""
Values Truthy e Falsy, Mutable and Immutable Types
Mutable   => [] {} set()
Immutable => () "" 0 0.0 None False range(0, 10)
"""

list_ = []
dictionary = dict()
conjunct = set()
tuple_ = ()
string = ''
integer = 0
float_ = 0.0
nothing = None
false = False
interval = range(0)


def falsy(value):
    return 'falsy'if not value else 'truthy'


print(f"TESTE", falsy("TESTE"))
print(f'{list_=}', falsy(list_))
print(f'{dictionary=}', falsy(dictionary))
print(f'{conjunct=}', falsy(conjunct))
print(f'{tuple_=}', falsy(tuple_))
print(f'{string=}', falsy(string))
print(f'{integer=}', falsy(integer))
print(f'{float_=}', falsy(float_))
print(f'{nothing=}', falsy(nothing))
print(f'{false=}', falsy(false))
print(f'{interval=}', falsy(interval))
