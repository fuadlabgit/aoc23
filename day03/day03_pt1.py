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
 
parts = {}
all_parts = [] 

for c in pcoords:
    #print("coord" , c)

    neighbors = [c+1+1j, c+1j, c-1+1j, c-1, c+1, c-1-1j, c-1j, c+1-1j]
    myparts = [] 
    for n in neighbors:
        # walk to the right
        u = int(n.real)
        v = int(n.imag)
        # print(" neighbor", n)
        # print(u,v)
        # print(map[u][v])
        while v < len(map) and (map[u][v] in digit_s):
            v+= 1
            # print(" > walk", u,v)
        end = v-1
        
        v = int(n.imag)
        while v >=0 and (map[u][v] in digit_s):
            v-=1
            # print(" < walk", u,v)
        start=v+1
        #print(start, end)
        
        if end >= start:
            part_no = int("".join([map[u][l] for l in range(start, end+1) if map[u][l] in digit_s]))
            
            #print("    found part", part_no)
        
            #for l in range(start,end+1):
            #    parts[u+l*1j] = part_no
            parts[start] = part_no
            myparts.append(part_no)
        
    for p in set(myparts):
        all_parts.append(p)
 

#print(list(parts.values()))
#print(sum(list(parts.values())))

#print(list(all_parts))
print(sum(list(all_parts)))

