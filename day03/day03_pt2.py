digit_s = [str(i) for i in range(10)]
 
# with example input
map = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598...""".split("\n")

# with puzzle input 
with open("input.txt") as file:
    map = file.read()
map = map.split("\n")

p = 0+0j # notation for a point in 2d
 
pcoords =[]
 
import re
for r,row in enumerate(map):
    matches = list(re.finditer(r"[^0-9\.]",row))
    
    for imatch in matches:
       pcoords.append(r + (imatch.start(0))*1j)
 
gear_ratio = 0

for c in pcoords:
    
    if map[int(c.real)][int(c.imag)] != "*":
        continue
    
    neighbors = [c+1+1j, c+1j, c-1+1j, c-1, c+1, c-1-1j, c-1j, c+1-1j]
    myparts = []

    for n in neighbors:
        
        u = int(n.real)
        v = int(n.imag)

        while v < len(map) and (map[u][v] in digit_s):
            v+= 1
        end = v-1
        
        v = int(n.imag)
        while v >=0 and (map[u][v] in digit_s):
            v-=1
        start=v+1
        
        if end >= start:
            part_no = int("".join([map[u][l] for l in range(start, end+1) if map[u][l] in digit_s]))

            myparts.append(part_no)
    
    mparts = list(set(myparts))
    if len(mparts) == 2:
        gear_ratio += mparts[0] * mparts[1]

print(gear_ratio)