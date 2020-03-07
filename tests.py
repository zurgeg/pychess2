import requests
import os
a = requests.get('https://github.com')
  
print('Outbound testing succesful')
print('Cythoning...')
os.system('cython onlinechess.py -o online.cpp')
print('Cythoned 1 file')
print('Output:')
f = open('online.cpp')
print(f.read())
print('Outputted {} lines'.format(len(f.readlines())))

