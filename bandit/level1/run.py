#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit1@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit1'
password = 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1'

p = ssh(username, host, port=port, password=password)
flag = p.process(['/bin/cat', './-']).recvall().decode('utf8')
print('flag:', flag)
