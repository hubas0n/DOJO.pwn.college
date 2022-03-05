#!/usr/bin/env python3
from pwn import *
#My 'iinuvx' environment variable should have a value of cekgsjiqsi
p = process(['/challenge/embryoio_level25'], env={'iinuvx':'cekgsjiqsi'})
p.interactive()
