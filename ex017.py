from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hip = hypot(co, ca)
print(f'A hipotenusa vai medir {hip:.2f}')
