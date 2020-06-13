#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit9@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit9'
password = 'UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR'

p = ssh(username, host, port=port, password=password)
sh = p.run('/bin/sh')
sh.sendline('cat data.txt | strings | grep =====')
while 1:
  bn = sh.recvline(timeout=3)
  flag = bn.decode('utf8')
  print('flag:', flag) # truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
