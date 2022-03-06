#!/usr/bin/env python3
from pwn import *
p = process(['/challenge/embryoio_level27'], stdout=open('/tmp/nxmhkh', 'w'))
p.wait_for_close()
