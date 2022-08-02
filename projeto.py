# Importando a biblioteca regex
import re

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

if(n_letras > n_digitos):
    if(re.match('[0-9]', autor)):
        autor_val = False
    else:
        autor_val = True
else:
    autor_val = False

# Validação - Senha

pattern_senha = r'((([A-F]\d)|(\d[A-F])|(\d\d)).){3}(([A-F]\d)|(\d[A-F])|(\d\d))'
senha_val = re.match(pattern_senha, elementos[1])


# Validação - IP

pattern_ip = r'((([0-1]?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}(([0-1]?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))'

ip_fatiamento = elementos[2].split('.')  # ['000', '000', '000', '000']

ip_status = []

if(re.match(pattern_ip, elementos[2])):

    for i in ip_fatiamento:
        if int(i) >= 100:
            ip_status.append(True)

        elif 10 <= int(i) < 100:
            if re.match('0', i) == None:
                ip_status.append(True)
            else:
                ip_status.append(False)
        elif 1 <= int(i) < 10:
            if re.match('00', i) == None:
                ip_status.append(True)
            else:
                ip_status.append(False)
        elif i == '000' or i == '00':
            ip_status.append(False)
        else:
            ip_status.append(True)

else:
    ip_val = False

if False in ip_status:
    ip_val = False
else:
    ip_val = True


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

pattern_trans = r'((pull)|(push)|(stash)|(fork)|(pop))'
trans_val = re.match(pattern_trans, elementos[4])

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
