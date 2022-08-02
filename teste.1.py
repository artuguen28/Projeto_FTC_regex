import re

ip1 = '255'
ip2 = '033'
ip3 = '003'

if re.match('0', ip1) == None:
    print(True)
else:
    print(False)

if re.match('0', ip2) == None:
    print(True)
else:
    print(False)

if re.match('0', ip3) == None:
    print(True)
else:
    print(False)
    
