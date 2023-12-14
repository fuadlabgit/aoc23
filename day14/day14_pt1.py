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
    # print("sorted rocks", rocks)
    # move rocks throug the map of cubes

    while rocks: 
        pos = rocks.pop()
        
        new_pos = pos + d 

        bndx = new_pos.real >= 0 and new_pos.real < M
        bndy = new_pos.imag >= 0 and new_pos.imag < N

        # print("try", pos, ">", new_pos, bndy, bndx)
        if (not bndx) or (not bndy):
            new_pos = pos 
            stuck = [pos] + stuck 
            # print(" >> stuck.")
            continue 

        if new_pos in rocks: # collides with another moving rock
            # print("   > collides with another moving")
            rocks =  [pos] + rocks # .append(pos)
        
        elif new_pos in cubes:
            # collides with a cube or another stuck rock 
            # print("   > collides with cube ")
            stuck = [pos] + stuck # .append(pos)
        
        elif new_pos in stuck:
            # print("   > collides with other stuck")
            stuck = [pos] + stuck # .append(new_pos)
        
        else:
            #vprint("    > no collision")
            rocks = [new_pos] + rocks #     .append(new_pos)
        # print("\n")

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
    # print(s)


# print_map(rocks, cubes, M, N)
rocks = move_rocks(rocks,cubes,-1j,M,N)

#print(rocks)
# print_map(rocks, cubes, M, N)

sol = 0
for rock in rocks:
    sol += N - rock.imag 

print(int(sol))