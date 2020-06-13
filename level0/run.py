#!/usr/bin/env python

from pwn import *

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit0'
password = 'bandit0'
p = ssh(username, host, port=port, password=password)
flag = p.process(['/bin/cat', 'readme']).recvall().decode('utf8')
print('flag:', flag)
