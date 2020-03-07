import requests
import os
a = requests.get('https://github.com')
  
print('Outbound testing succesful')
print('Cythoning...')
os.system('cython onlinechess.py')
print('Cythoned 1 file')
print('Output:')
f = open('onlinechess.cpp')
print(f.read())
print('Outputted {} lines'.format(len(f.readlines())))

