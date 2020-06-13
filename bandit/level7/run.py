#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit7@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit7'
password = 'HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs'

p = ssh(username, host, port=port, password=password)
sh = p.run('/bin/sh')
sh.sendline('cat data.txt | grep millionth')
bn = sh.recvline()
flag = bn.decode('utf8')
print('flag:', flag) # cvX2JJa4CFALtqS87jk27qwqGhBM9plV
