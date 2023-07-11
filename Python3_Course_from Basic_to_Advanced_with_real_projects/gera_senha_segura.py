from random import choice
import string

tamanho_senha = int(input('Quantos digitos terá a senha?": '))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''
for i in range(tamanho_senha):
    senha_segura += choice(caracteres)

print(f"A sua senha segura é: {senha_segura}")
