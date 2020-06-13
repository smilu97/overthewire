#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit4@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit4'
password = 'pIwrPrtPN36QITSp3EQaw936yaFoFgAB'

p = ssh(username, host, port=port, password=password)

def read_remote_file(path):
  pc = p.process(['/bin/cat', path])
  return pc.recvall()

for i in range(10):
  path = './inhere/-file0' + str(i)
  res = read_remote_file(path)
  try:
    res = res.decode('utf8')
    print('found:', res) # koReBOKuIDDepwhWk7jZC0RTdopnAYKh
    break
  except:
    pass
