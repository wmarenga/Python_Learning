# Desafio 43:
# Desenvolva uma lógica que leia o peso e a altura de uma
# pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso;
# - Entre 18.5 e 25: Peso ideal;
# - 25 até 30:Sobrepeso:
# - 30 até 40: Obesidade:
# - Acima de 40: Obesidade mórbida.

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(
        'Seu IMC é {:.1f} \n\033[1;31mCOMA MAIS!\033[m pois está \033[7;33mABAIXO\033[m do peso.'.format(imc))
# alternativas:
# elif 18.5 <= imc < 25:
# elif imc >= 18.5 and imc < 25:
elif imc < 25:
    print(
        'Seu IMC é {:.1f} \n\033[1;32mPARABÉNS!\033[m pois está com \033[7;32mPESO IDEAL\033[m.'.format(imc))
elif imc < 30:
    print(
        'Seu IMC é {:.1f} \n\033[1;31mATENÇÃO COMA MELHOR!\033[m pois está com\033[7;35mSOBREPESO\033[m do peso.'.format(imc))
elif imc < 40:
    print(
        'Seu IMC é {:.1f} \n\033[1;31mFAÇA DIETA URGENTE!\033[m pois está com\033[7;37mOBESIDADE\033[m do peso.'.format(imc))
# Também posso usar o "else:"
elif imc >= 40:
    print(
        'Seu IMC é {:.1f} \n\033[1;31mVÁ OU MÉDICO!\033[m pois está com\033[7;31mOBESIDADE MÓRBIDA\033[m do peso.'.format(imc))
