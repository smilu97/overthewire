#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit12@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit12'
password = '5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu'

p = ssh(username, host, port=port, password=password)
p.download('data.txt') # 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

# ./run.sh
