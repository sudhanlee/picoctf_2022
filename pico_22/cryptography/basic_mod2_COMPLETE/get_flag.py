#!/usr/bin/env python3

import string

key = string.ascii_uppercase + string.digits + '_'

with open("message.txt","r") as f:
	lst = f.readlines()[0].split()
	flag = ""
	for i in lst:
		flag += key[pow(int(i),-1,41)-1]

print("picoCTF{" + flag + "}")
