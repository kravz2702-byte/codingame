import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
numbers = []
minimal = 10000000000
first = 0
n = int(input())
for i in range(n):
    pi = int(input())
    numbers.append(pi)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
allnums = len(numbers)

for a in numbers:
    first+=1
    for b in numbers[first:allnums]:
        if a>b and a-b<minimal:
            minimal = a-b
        elif a<b and b-a<minimal:
            minimal = b-a
        

print(minimal)