#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit3@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit3'
password = 'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'

p = ssh(username, host, port=port, password=password)
flag = p.process(['/bin/cat', './inhere/.hidden']).recvall().decode('utf8')
print('flag:', flag) # pIwrPrtPN36QITSp3EQaw936yaFoFgAB
