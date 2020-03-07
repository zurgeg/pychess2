import requests
import os
a = requests.get('https://github.com')
  
print('Outbound testing succesful')
print('Cythoning...')
os.system('cython onlinechess.py')
print('Cythoned 1 file')
print(os.system('ls'))
