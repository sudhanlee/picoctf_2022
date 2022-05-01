#!/usr/bin/env python3

import re

f = open("drawing.flag.svg","r")
flag = ""
lst = f.readlines()

for i in lst:
	if "</tspan" in i:
		flag += "".join(re.findall(">(.*)</tspan",i)[0].split())
print(flag)
f.close()