#!/usr/bin/env ipython
from pwn import *
p = process(['/challenge/embryoio_level21'], env={})
