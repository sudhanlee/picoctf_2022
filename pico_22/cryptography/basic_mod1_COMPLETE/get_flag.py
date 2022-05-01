#!/usr/bin/env python3

import string

key = string.ascii_uppercase + string.digits + '_'

with open("message.txt","r") as f:
	lst = f.readlines()[0].split()
	flag = ""
	for i in lst:
		flag += key[int(i)%37]

print("picoCTF{" + flag + "}")
