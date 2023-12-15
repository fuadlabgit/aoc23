x = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def hash(x):
    c = 0
    for xi in x:
        c += ord(xi)
        c *= 17 
        c = c % 256 
    return c 

sol = 0
for xi in x.split(","):
    sol += hash(xi)

print(sol)
