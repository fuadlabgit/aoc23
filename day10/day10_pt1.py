
from collections import defaultdict
pipes = defaultdict(lambda: [])

map = open("input.txt").readlines()


# fill pipes info from map
for y in range(len(map)):
    for x in range(len(map[y])):
        pos = x+y*1j
        pipe = map[y][x]

        conn = []
        
        if pipe== "L":
                conn =[pos-1j, pos+1]
        if pipe== "F":
                conn = [pos+1,pos+1j]
        if pipe== "J":
                conn = [pos-1, pos-1j]
        if pipe== "7":
                conn = [pos-1, pos+1j]
        if pipe== "|":
                conn = [pos-1j,pos+1j]
        if pipe== "-":
                conn = [pos-1,pos+1] 
        if pipe== "S":
                start = pos
        # print(pos, "connects to ", conn)
        for conni in conn:
            pipes[pos].append(conni)
 
def get_map(pos):
    return map[int(pos.imag)][int(pos.real)]

# fix start node 
for n in [start+1,start-1, start+1j, start-1j]:
    if start in pipes[n]:
        if not (n in pipes[start]):
            pipes[start].append(n)

def is_dead_end(pos, last_pos):
    if len(pipes[pos]) == 1 and pipes[pos][0] == last_pos:
        return True 
    return False 

visited = []

q = [start]
while q: 
    
    qi = q[0]
    q = q[1:]

    for n in pipes[qi]:
        if n not in visited:
            visited.append(n)
            q.append(n)

print(int(len(visited)/2))