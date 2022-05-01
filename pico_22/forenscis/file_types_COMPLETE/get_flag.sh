#!/bin/bash

mv Flag.pdf flag.sh
sh flag.sh
ar x flag
mv flag flag.cpio
cpio --file flag.cpio -i
mv flag flag.bz2
bzip2 -d flag.bz2
mv flag flag.gz
gzip -d flag.gz
lzip -d flag
mv flag.out flag.lz4
lz4 -d flag.lz4
mv flag flag.lzma
lzma -d flag.lzma
mv flag flag.lzop
lzop -d flag.lzop
lzip -d flag
mv flag.out flag.xz
xz -d flag.xz
cat flag | xxd -r -p