map = open("input.txt").readlines()


rocks = []
cubes = []

#print(len(map), len(map[0]))

N = len(map)
M = len(map[0].strip())

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == ".":
            continue 

        elif map[y][x] == "#":
            cubes.append(x + 1j*y)
        elif map[y][x] == "O":
            rocks.append(x + 1j*y)
        
#print(rocks)
#print(cubes)

from collections import defaultdict 

def move_rocks(rocks, cubes, d, M, N):

    rocks = rocks #  sorted(rocks, key = lambda x: x.imag)
    stuck = [] 
    # move rocks throug the map of cubes

    while rocks: 
        pos = rocks.pop()

        new_pos = pos + d 

        bndx = new_pos.real >= 0 and new_pos.real < M
        bndy = new_pos.imag >= 0 and new_pos.imag < N

        if (not bndx) or (not bndy):
            new_pos = pos 
            stuck = [pos] + stuck 
            continue 

        if new_pos in rocks: # collides with another moving rock
            rocks =  [pos] + rocks 
        
        elif new_pos in cubes:
            # collides with a cube or another stuck rock 
            stuck = [pos] + stuck 
        
        elif new_pos in stuck:
            stuck = [pos] + stuck 
        
        else:
            rocks = [new_pos] + rocks # no collision
        

    return stuck

import numpy as np 

    
def print_map(rocks,cubes, M,N):
    mymap = np.array([["."]*M]*N)
    for pos in rocks:
        #assert map[y][x] == "." 
        mymap[int(pos.imag)][int(pos.real)] = "O"
    for pos in cubes:
        #assert map[y][x] == "." 
        mymap[int(pos.imag)][int(pos.real)] = "#"
    s = ""
    for line in mymap:
        s += "".join(line)
        s += "\n"
    print(s)



def spin_cycle(rocks):
    for d in [-1j, -1, 1j, +1]:
        rocks = move_rocks(rocks,cubes, d , M, N)
    return rocks 

#print(rocks)
buf = []

for i in range(200):
    rocks = spin_cycle(rocks)
    # print_map(rocks, cubes, M, N)

    sol = 0
    for rock in rocks:
        sol += N - rock.imag 
    buf.append(int(sol))
    if i > 1:
        print("CYCLE", i+1, "sol", int(sol), buf[-1] - buf[-2])

print(int(sol))

"""
COMMENT: idea is to find the repeating pattern at the point where it does not 
change any longer. Then find the correct multiple of 100's of repetitions to find the 
value after 1_000_000... simulations 
"""