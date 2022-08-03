# Importando a biblioteca regex
import re

from soupsieve import match

try:
    # A entrada do caso teste será feita via input

    entrada = input().strip()

    # Validação - Excesso de ''

    elementos = entrada.split(' ')
    while('' in elementos):
        elementos.remove('')

    # Validação - Quantidade de elementos

    if(len(elementos) != 7):
        print(False)
        exit()

    # Validação - Autor

    autor = elementos[0]
    n_letras = re.findall('[a-zA-Z]', autor)
    n_digitos = re.findall('[0-9]', autor)

    if(len(n_letras) >= len(n_digitos)):

        if(re.match('[0-9]', autor)):
            autor_val = False
        else:
            autor_val = True
    else:
        autor_val = False


    # Validação - Senha

    lista_senha = elementos[1].split('.')

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


    # Validação - IP

    ip_fatiamento = elementos[2].split('.')  # ['000', '000', '000', '000']

    p = 1

    if(len(ip_fatiamento) == 4):

        for i in ip_fatiamento:
            if int(i) >= 100:
                p = p * 1

            elif 10 <= int(i) < 100:
                if re.match('0', i) == None:
                    p = p * 1
                else:
                    p = p * 0

            elif 1 <= int(i) < 10:
                if re.match('00', i) == None:
                    p = p * 1
                else:
                    p = p * 0

            elif i == '000' or i == '00':
                p = p * 0
            else:
                p = p * 1

        if p:
            ip_val = True
        else:
            ip_val = False

    else:
        ip_val = False
    

    # Validação - E-mail

    arrobas = 0
    pattern_email1 = r'([a-zA-Z0-9]+([\.\-\_][a-zA-Z0-9]+)*)'
    pattern_email2 = r'([\w]+\.[\w]+)(\.[\w]+)*'

    for i in range(len(elementos[3])):
        if elementos[3][i] == '@':
            arrobas += 1

    if arrobas == 1:
        email_groups = elementos[3].split("@")
        email_1 = re.match(pattern_email1, email_groups[0])
        email_2 = re.match(pattern_email2, email_groups[1])

        if email_1 and email_2:
            email_val = True
        else:
            email_val = False
    else:
        email_val = False



    # Validação - Tipo de transação

    pattern_trans = ['pull', 'push', 'stash', 'pop']
    

    

    # Validação - Repositório

    pattern_rep = r'([\w_]+)'
    rep_val = re.match(pattern_rep, elementos[5])

    # Validação - Hash

    pattern_hash = r'(\d|[a-f]){32}'
    hash_val = re.match(pattern_hash, elementos[6])

    # Validando resposta final

    if (autor_val and senha_val and ip_val and email_val and trans_val and rep_val and hash_val):
        result = True
    else:
        result = False

    # Exibindo resultado

    print(result)

except EOFError:
    print(False)