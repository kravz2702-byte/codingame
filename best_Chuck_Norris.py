import sys
import math

msg = input()
out=""
bn=""
b=""

for c in msg:
    bn += bin(ord(c))[2:].zfill(7)

for c in bn:
    if c == "1" != b:
        out += " 0 "
        b="1"
    elif c == "0" != b:
        out += " 00 "
        b="0"
    out += "0"

print(out.strip())
