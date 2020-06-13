#!/usr/bin/env python

from pwn import *

# ssh -p 2220 bandit2@bandit.labs.overthewire.org

port = 2220
host = 'bandit.labs.overthewire.org'
username = 'bandit2'
password = 'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'

p = ssh(username, host, port=port, password=password)
flag = p.process(['/bin/cat', 'spaces in this filename']).recvall().decode('utf8')
print('flag:', flag) # UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
