#!/usr/bin/env ipython
from pwn import *
p = process('/challenge/embryoio_level16')
p.recv()
p.interactive()
