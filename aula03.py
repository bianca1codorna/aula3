#ATV1

num = float(input('digite um número: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

#ATV2

from math import hypot
oposto = float(input('informe o comprimento do cateto oposto: '))
adjacente = float(input('informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('de acordo com o comprimento do cateto oposto {} e do adjacente {},'
      ' o comprimento da hipotenusa é {:.2f}'.format(oposto, adjacente, hipotenusa))

#ATV3

import math
angulo = float(input('Informe um ângulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))