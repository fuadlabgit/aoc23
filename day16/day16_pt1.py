map = open("input.txt").readlines()


N=len(map)
M = len(map[0])-1
parts = {}

for y in range(N):
 for x in range(M):
  if map[y][x] != ".":
   parts[x+1j*y] = map[y][x]

movemap = {
1:   {"|": [1j, -1j], "/": [-1j], "\\": [1j], "-": [1],},
-1:  {"|": [-1j, 1j], "/": [1j], "\\": [-1j], "-": [-1],},
1j:  {"|": [1j], "/": [-1], "\\": [1], "-": [-1,1],},
-1j: {"|": [-1j], "/": [1], "\\": [-1], "-": [-1,1],}
}

turtles = {} 
# start: pos, dir

class Beam:

    def __init__(self, start, direction):
        self.pos = start 
        self.start = start 
        self.dir = direction
        self.start_dir = direction
        self.pathlen = 0

    def __repr__(self):
        return "[%s, %s]" % (self.pos, self.dir)


active_beams =  [Beam(-1+0j, 1+0j)]
finished_beams = [] 
visited = {}

def add_beam(next_pos, next_dir, mybeams, finished):
    for other in mybeams + finished: 
        if other.start == next_pos and other.start_dir == next_dir:
            break 
    else:
        print("     add new beam ", next_pos, next_dir)

        mybeams = [Beam(next_pos, next_dir)] + mybeams
    return mybeams 


k = 0
while active_beams: # active_beams:
    k += 1 

    beam = active_beams.pop() 
    
    if beam.pos in visited:
        
        if beam.dir in [v for v in visited[beam.pos][1]]: 
            finished_beams.append(beam)
            continue 
        
        visited[beam.pos][0] += 1 
        visited[beam.pos][1].append(beam.dir)

    else:
        visited[beam.pos] = [1, [beam.dir]]
    
    next_pos = beam.pos + beam.dir

    if not (0 <= next_pos.real < M and 0 <= next_pos.imag < N):
        finished_beams.append(beam)
        continue 
    
    if next_pos in parts:
        next_dirs = movemap[beam.dir][parts[next_pos]]
    else:
        next_dirs = [beam.dir]
    
    if len(next_dirs) > 1:  #  add split beam  
        next_dir = next_dirs[1]
        active_beams = add_beam(next_pos, next_dir, active_beams, finished_beams)

    next_dir = next_dirs[0] 
    beam.dir = next_dir 
    beam.pos = next_pos 
    active_beams = [beam] + active_beams
    

# print the map 
print("\n\n")

mystr = {
        -1j: "^",
        1j: "v" ,
        1: ">",
        -1: "<"
        }

s= ""
for y in range(-1,N+1):
    for x in range(-1,M+1):
        si = "."
        pos = x + 1j * y 
   
        if pos in parts:
            si = parts[pos]
        
        else:
            if pos in visited:
                if visited[pos][0] == 1:
                    si = mystr[visited[pos][1][-1]]
                else:
                    n = visited[pos][0] 
                    if n < 9:
                        si= str(visited[pos][0])
                    else:
                        si = "x"
            #else:
            #    si = "o"
        s+= si.strip().replace("B","\\")
    s+="\n"
   
print(s)

# print the solution 
print(len(visited) - 1)