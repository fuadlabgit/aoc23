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
 
class Beam:

    def __init__(self, start, direction):
        self.pos = start 
        self.start = start 
        self.dir = direction
        self.start_dir = direction
        self.pathlen = 0

    def __repr__(self):
        return "[%s, %s]" % (self.pos, self.dir)


def find_energize(start_pos, start_dir ): 
    
    active_beams =  [Beam(start_pos, start_dir)]
    finished_beams = [] 
    visited = {}

    def add_beam(next_pos, next_dir, mybeams, finished):
        for other in mybeams + finished: 
            if other.start == next_pos and other.start_dir == next_dir:
                break 
        else:
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
    
    # 7440 too low 

    # print the solution 
    return len(visited) - 1

e = 0 
for x in range(M):
    e = max(e,find_energize(x-1j, 0+1j))

for x in range(M):
    e = max(e,find_energize(x+(N)*1j, 0-1j))

print(e)
