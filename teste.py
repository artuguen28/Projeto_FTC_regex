import re

from numpy import append

elementos = input()


# Validação - Senha
lista_senha = elementos.split('.')

t = 1

# Senha - 2 digitos por casa
for i in lista_senha:
    if len(i) == 2:
        t = t*1
    else:
        t = t*0
        


# Senha - validar caracteres

for i in lista_senha:
    if re.findall(r'((\d\d)|([A-F]\d)|(\d[A-F]))', i):
        t = t*1

    else:
        t = t*0

for i in lista_senha:
    if re.findall(r'[0-9][0-9]', i):
        if i[0] != i[1]:
            t = t*1

        else:
            t = t*0

# Senha - Validar listas

if t:
    senha_val = True
else:
    senha_val = False

print(senha_val)