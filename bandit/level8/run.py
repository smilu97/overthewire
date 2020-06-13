#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit8@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit8'
password = 'cvX2JJa4CFALtqS87jk27qwqGhBM9plV'

p = ssh(username, host, port=port, password=password)
sh = p.run('/bin/sh')
sh.sendline('cat data.txt | sort | uniq -u')
bn = sh.recvline()
flag = bn.decode('utf8')
print('flag:', flag) # UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
