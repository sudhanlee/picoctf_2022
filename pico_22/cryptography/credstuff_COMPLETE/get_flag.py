#!/usr/bin/env python3

import codecs

f_user = open("leak/usernames.txt","r")
f_pass = open("leak/passwords.txt","r")

user_lst = f_user.readlines()
pass_lst = f_pass.readlines()

for name in user_lst:
	if name == "cultiris\n":
		flag = pass_lst[user_lst.index(name)]

flag = codecs.decode(flag,"rot_13")
print(flag)
