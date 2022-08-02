import re

# A entrada do caso teste será feita via input

ip = input()

# Validação - IP

pattern_ip = r'((([0-1]?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}(([0-1][0-9][0-9])|(2[0-4][0-9])|(25[0-5]))'

if(re.match(pattern_ip, ip)):
    print(True)
else:
    print(False)

