import re

str = 'an example word:cato!!'
match = re.search(r'word:\w\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')