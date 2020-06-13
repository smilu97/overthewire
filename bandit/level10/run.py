#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit10@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit10'
password = 'truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk'

p = ssh(username, host, port=port, password=password)
sh = p.run('/bin/sh')
sh.sendline('base64 -d data.txt')
bn = sh.recvline()
flag = bn.decode('utf8')
print('flag:', flag) # IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
