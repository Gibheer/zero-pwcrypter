#!/usr/bin/env python
# this script takes input from the pipe and generates a crypted password
# from it
# the first line is the password in cleartext
# the second line is the crypted version of the password

import sys
import crypt
import string
import random

chars = string.letters + string.digits
seed = ''
for i in range(3):
  seed = seed + random.choice(chars)
for line in sys.stdin:
  line = line.strip()
  print line
  print crypt.crypt(line, seed)
