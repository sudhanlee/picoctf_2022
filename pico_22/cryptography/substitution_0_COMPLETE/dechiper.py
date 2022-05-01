#!/usr/bin/env python3


key = "QWITJSYHXCNDFERMUKGOPVALBZ0123456789 {}_"
org = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 {}_"

encrypt = list("mxirIOS{5PW5717P710E_3V0DP710E_03055505}".upper())
decrypt = ""

for i in encrypt:
	pos = key.index(i)
	i = 0
	decrypt += org[pos]
print(decrypt)