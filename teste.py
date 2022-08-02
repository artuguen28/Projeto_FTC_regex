import re

# A entrada do caso teste será feita via input

ip = input()

# Validação - IP

pattern_ip = r'((([0-1]?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}(([0-1]?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))'

ip_fatiamento = ip.split('.')  # ['000', '000', '000', '000']
print(ip_fatiamento)

ip_status = []

print(f"IP Status before: {ip_status}")

if(re.match(pattern_ip, ip)):

    for i in ip_fatiamento:
        if int(i) >= 100:
            ip_status.append(True)

        elif 10 <= int(i) < 100:
            if re.match('0', i) == None:
                ip_status.append(True)
            else:
                ip_status.append(False)
        else:
            if re.match('0', i) == None:
                ip_status.append(True)
            else:
                ip_status.append(False)

else:
    ip_val = False

print(f"IP Status after: {ip_status}")

if False in ip_status:
    ip_val = False
else:
    ip_val = True

print(ip_val)