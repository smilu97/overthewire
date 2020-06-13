#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit5@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit5'
password = 'koReBOKuIDDepwhWk7jZC0RTdopnAYKh'

p = ssh(username, host, port=port, password=password)

# find inhere -size 1033c ! -executable

def read_remote_file(path):
  pc = p.process(['/bin/cat', path])
  return pc.recvall()

path = 'inhere/maybehere07/.file2' # find -size 1033c ! -executable
bn = read_remote_file(path)
flag = bn.decode('utf8')
print('flag:', flag) # DXjZPULLxYr17uwoI01bNLQbtFemEgo7
