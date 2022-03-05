#!/usr/bin/env ipython
from pwn import *
p = process(['/challenge/embryoio_level20'], stdout=open('/tmp/hezvle'))
p.interactive()
