#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit6@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit6'
password = 'DXjZPULLxYr17uwoI01bNLQbtFemEgo7'

p = ssh(username, host, port=port, password=password)

# find inhere -size 1033c ! -executable

def read_remote_file(path):
  pc = p.process(['/bin/cat', path])
  return pc.recvall()

path = '/var/lib/dpkg/info/bandit7.password' # find / -group bandit6 -user bandit7 -size 33c 2> /dev/null
bn = read_remote_file(path)
flag = bn.decode('utf8') # HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
print('flag:', flag)
