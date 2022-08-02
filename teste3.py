import re

str = 'purple lbp.7@outlook.com  monkey dishwasher'

match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print('Encontrado: ', match.group())  ## 'alice-b@google.com'