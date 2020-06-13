#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit11@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit11'
password = 'IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR'

p = ssh(username, host, port=port, password=password)
txt = p.process(['/bin/cat', 'data.txt']).recvall().decode('utf8')
print('txt:', txt)

def rot13_char(x):
  if ord('a') <= ord(x) <= ord('z'):
    if ord(x) <= ord('m'):
      return chr(ord(x)+13)
    else:
      return chr(ord(x)-13)
  if ord('A') <= ord(x) <= ord('Z'):
    if ord(x) <= ord('M'):
      return chr(ord(x)+13)
    else:
      return chr(ord(x)-13)
  return x

def rot13(s):
  return ''.join([rot13_char(x) for x in s])

flag = rot13(txt)
print('flag:', flag) # 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
