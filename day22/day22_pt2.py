from itertools import product 
from collections import defaultdict 

bricks = [] # map brick names to cube positions of this brick

lines = open("input.txt").readlines()

names = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6: "G", 7:"H", 8:"I"}

k = 0
for line in lines:
    bs, be = line.split("~")
    bs = [int(i.strip()) for i in bs.split(",")]
    be = [int(i.strip()) for i in be.split(",")]
    
    # sort the ranges
    bs2 = [min(bs[0],be[0]), min(bs[1],be[1]),min(bs[2],be[2])]
    be2 = [max(bs[0],be[0]),max(bs[1],be[1]),max(bs[2],be[2])]

    #bricks.append((bs2, be2, names[k]))
    bricks.append((bs2, be2, k))
    
    k += 1

def supports(bottom, top):
    # find out if bottom supports top 

    xr_bottom =  (bottom[0][0], bottom[1][0])
    xr_top = (top[0][0], top[1][0])
    dx = (max(xr_bottom[0], xr_top[0]), min(xr_bottom[1],xr_top[1]))

    yr_bottom =  (bottom[0][1], bottom[1][1])
    yr_top = (top[0][1], top[1][1])
    dy = (max(yr_bottom[0], yr_top[0]), min(yr_bottom[1],yr_top[1]))

    if dx[1] >= dx[0] and dy[1] >= dy[0]:
        return True 
    
    return False

# let bricks fall down 
bricks = sorted(bricks, key = lambda x: x[1][2])

for j, this in enumerate(bricks):

    lowest = this[1][2]
    
    highest = 1 
    for other in bricks[:j]:
        if supports(other, this):
    
            new_highest = other[1][2] + 1 
            highest = max(highest, new_highest)
    
    if highest < lowest:
        height = this[1][2] - this[0][2]
        this[0][2] = highest 
        this[1][2] = highest + height 
    
# sort bricks into layers 
layers = defaultdict(lambda: [])

for brick in bricks:

    for z in range(brick[0][2], brick[1][2] +1):
        layers[z].append(brick)

# print(dict(layers))

# find supporting blocks 
supporters_of = defaultdict(lambda: [])
supporting = defaultdict(lambda: [])

for l in range(len(layers)):

    # compare all parts in this and next layer
    for bottom in layers[l]:

        for top in layers[l+1]:
            if bottom != top: 

                # check if the bottom supports the top
                if supports(bottom, top):
                    
                    supporters_of[top[2]].append(bottom[2])
                    supporting[bottom[2]].append(top[2])


def remove(brick, fallen, t = 0):
    
    fallen.append(brick)

    for other in supporting[brick]:

        if other in fallen:
            continue 

        # print("\t" * t, brick, "supports", other)
        # see if any other would fall 
        chain = []
        
        for b in supporters_of[other]:
            if b not in fallen:
                chain.append(b)

        # print("\t" * t, "chain", chain)

        if len(chain) < 1: # will also fall?
            # print("-> " , other, "also falls")
            if other not in fallen:
                fallen.append(other)
                t = remove(other,fallen, t+1)
    
    return t


sol = 0
for brick in bricks:
    sol += remove(brick[2],[])
    # print("remove", brick[2], "-->", sol)

print(sol)