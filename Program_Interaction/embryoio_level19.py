#!/usr/bin/env ipython
from pwn import *
p = process(['/challenge/embryoio_level19'], stdin=open('/tmp/fmnmle'))
