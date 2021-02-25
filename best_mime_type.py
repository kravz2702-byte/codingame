n = int(input())  
q = int(input())  
assoc = {None : 'UNKNOWN'}

for i in range(n):
    ext, mt = input().split()
    assoc[ext.upper()] = mt

for i in range(q):
    fname = input()
    split_fname = fname.split('.')
    ext = split_fname[-1].upper() if len(split_fname) > 1 else None
    print(assoc.get(ext, "UNKNOWN"))