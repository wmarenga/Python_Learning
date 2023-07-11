# Desafio 11:
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua
# área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2m2.

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg * alt
lt_tinta = área / 2  # 2m2 por litro
print(' A sua parede tem a dimensão de {:.2f} m X {:.2F} m e\n a área total é de {:.2f} m2, sendo assim\n você precisa de {:.1f} litros de tinta.'.format(
    larg, alt, área, lt_tinta))
