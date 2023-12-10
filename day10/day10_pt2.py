
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


def out_of_bounds(p):
    
    if p.real < 0 or p.imag < 0 or p.real >= len(map[0]) or p.imag >= len(map):
        # print("          out of bounds", p)
        return True 
    return False


def make_mainloop(start):
    snake = []

    node = start 
    k = 0
    while (k == 0 or (not node == start)): #  and k < 10:
        k+= 1

        if node in snake[:-1]: 
            break 
        
        nextnode = None 
        for option in pipes[node]:
            if len(snake) < 2 or option != snake[-1]:
                nextnode = option 
                
        snake.append(node)
        
        node = nextnode

    return snake 


def find_enclosed(pipes,node,nextnode):
    my_inner = []

    dy = int(node.real - nextnode.real)
    dx = int(node.imag - nextnode.imag)
    d = -dx + dy*1j
    #d = +dx - dy*1j 
    # NOTE IT MAKES A DIFFERENCE WHICH TO TAKE: EXPERIMENTAL
    
    for mynode in [node, nextnode]:
        # walk until next node or out of bounds
        found = False 
        n = 0
        l = []
        while True:
            n += 1
            p = mynode + d*n 
            if p not in pipes:
                l.append(p)
            if out_of_bounds(p):
                break
            if p in pipes:
                found = True     
                break 

        ##if len(l) > 0 and found:
        #    print("   found ", l, found)

        if found: 
            my_inner += l
    
    return my_inner



def get_inner(pipes,start):
    snake = []
    inner = []

    node = start 
    k = 0
    while (k == 0 or (not node == start)): #  and k < 10:
        k+= 1

        if node in snake[:-1]: 
            break 
        
        nextnode = None 
        for option in pipes[node]:
            if len(snake) < 2 or option != snake[-1]:
                nextnode = option 
                
        snake.append(node)
        
        inner += find_enclosed(pipes,node, nextnode)
        node = nextnode

    return inner 


# NOTE IT MAKES A DIFFERENCE WHERE TO START
start = pipes[start][1]
snake = make_mainloop(start)

all_pipes = {k:v for k,v in pipes.items()}
pipes = {}

for k,v in all_pipes.items():
    if k in snake:
        pipes[k] = all_pipes[k]


new_map = map
for y in range(len(new_map)):
    newline = ""
    for x in range(len(new_map[0])):
        if not x + y*1j in pipes:
            newline += "."
        else:
            newline += map[y][x]
    new_map[y] = newline


# print("\n".join(new_map))
map = new_map 

inner = list(set(get_inner(pipes,start)))

for y in range(len(new_map)):
    newline = ""
    for x in range(len(new_map[0])):
        if x + y*1j in inner:
            newline += "I"
        else:
            newline += map[y][x]
    new_map[y] = newline

# print("\n".join(new_map))
# print("\n\n")

# print([(i,get_map(i)) for i in inner])
print(len(inner))
