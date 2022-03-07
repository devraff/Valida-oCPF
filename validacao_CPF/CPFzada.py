"""
870.185.870-00
"""

x = [8, 7, 0]
y = [1, 8, 5]
z = [8, 7, 0]
a = [0, 0]
soma_d1 = x[0] * 10 + x[1] * 9 + x[2] * 8
soma_d12 = y[0] * 7 + y[1] * 6 + y[2] * 5
soma_d13 = z[0] * 4 + z[1] * 3 + z[2] * 2
soma1 = soma_d1 + soma_d12 + soma_d13
soma_d2 = x[0] * 11 + x[1] * 10 + x[2] * 9
soma_d22 = y[0] * 8 + y[1] * 7 + y[2] * 6
soma_d23 = z[0] * 5 + z[1] * 4 + z[2] * 3
digito1 = 11 - (soma1 % 11)

if digito1 >= 9:
    digito1 = 0

soma2 = soma_d2 + soma_d22 + soma_d23 + digito1 * 2
digito2 = 11 - (soma2 % 11)

if digito2 >= 9:
    digito2 = 0

    print (f'seu CPF é {x}.{y}.{z}-{a}')

if digito1 == a[0] and digito2 == a[1]:
    print('CPF valido')
else:
    print('Deu ruim')





