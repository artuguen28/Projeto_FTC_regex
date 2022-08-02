import re

# A entrada do caso teste será feita via input

ip = input()

# Validação - IP

pattern_ip = r'(([0-2][0-5][0-5]).){3}(([0-2][0-5][0-5]))'

ip_fatiamento = ip.split('.')  # ['000', '000', '000', '000']
ip_status = []

if(re.match(pattern_ip, ip)):
    for i in ip_fatiamento:
        if int(ip_fatiamento[i]) >= 100:
            ip_status.append(True)
            ip_val = True
        elif 10 <= int(ip_fatiamento[i]) < 100:
            if re.match('0', ip_fatiamento[i]) == None:
                ip_status.append(True)
            else:
                ip_status.append(False)
        else:
            if re.match('0', ip_fatiamento[i]) == None:
                ip_status.append(True)
            else:
                ip_status.append(False)

if False in ip_status:
    ip_val = False
else:
    ip_val = True

print(ip_val)