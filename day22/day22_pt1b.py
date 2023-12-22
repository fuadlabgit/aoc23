from itertools import product 

bricks = {}

lines = open("example.txt").readlines()

max_x = 0
max_y = 0
max_z = 0

k = 0
for line in lines:
    bs, be = line.split("~")
    bs = [int(i.strip()) for i in bs.split(",")]
    be = [int(i.strip()) for i in be.split(",")]

    bricks[k] = (bs, be) # .append((bs,be, k))
    k+= 1

    max_x = max(max_x, max(bs[0], be[0]))
    max_y = max(max_y, max(bs[1], be[2]))
    max_z = max(max_z, max(bs[2], be[2]))

N = 1+ max(max_x, max(max_y, max_z)) # make a giant space cube
print("DIM", N)


"""
(a,b,c,d) - (e,f,g,h)
            
          e  _____________ h
            /8    /  7   /|
           /_____/______/ |
          /|5   /| 6   /| |
       f /_|___/_|__g_/ |/| 3
      a->| | 4 | |    |/| |   
         |-|__-| |___-| |/ d
         | /  1| /  2 | /
         |/____|/_____|/
        b              c

            e = (x,y,z+2m)
            |
            |
            |
        a = (x,y,z) ----- d = (x,y+2m,z)
           /
          /
        b = (x+2m,y,z)



(u,v,w) rough quadrant (u//256, v//256, w//256)
"""

class Oct:
    def __init__(self, a, N):

        self.elems = [] # elements stored in this oct
        
        self.N = N
        self.a = (int(a[0]), int(a[1]), int(a[2]))
        
        self.m = int(0.5* N)
        m = self.m 
        if self.m <= 4:
            self.children = None  # is elementary cube 
        
        else:
            self.children = {
                (1,0,0): Oct((a[0]+m,a[1],a[2]), m), # cube 1
                (1,1,0): Oct((a[0]+m,a[1]+m, a[2]),m), # cube 2
                (0,1,0): Oct((a[0],a[1]+m,a[2]),m), # cube 3
                (0,0,0): Oct((a[0],a[1],a[2]),m), # cube 4
                (1,0,1): Oct((a[0]+m,a[1],a[2]+m),m), # cube 5
                (1,1,1): Oct((a[0]+m,a[1]+m,a[2]+m),m), # cube 6
                (0,1,1): Oct((a[0],a[1]+m,a[2]+m),m), # cube 7
                (0,0,1): Oct((a[0],a[1],a[2]+m),m), # cube 8
            }
    
    def __repr__(self):
        return "[Oct %s]" % (str(self.a))

    def add_elem(self, p, elem, depth=0):
        # add a cube at position p 
        if self.children is None:
            self.elems.append(elem)
            return self 
        
        new_idx = ((p[0]-self.a[0])//self.m, (p[1]-self.a[1])//self.m, (p[2]-self.a[2])//self.m)
        # print("\t" * depth, "  add", elem, new_idx)

        last_child = self.children[new_idx].add_elem(p, elem, depth+1)
        return last_child 


    def get_elems(self):
        # get all items in this oct 

        if self.children is None:
            return self.elems 
        
        el = []
        for idx, c in self.children.items():
            el += c.get_elems()
        
        return el


myoct = Oct((0,0,0), 16)

oct_dict = {}

for brick_id, brick in bricks.items():

    print(brick_id, brick)
    points = [] 
    
    for x in range(brick[0][0], 1+brick[1][0]):
        points.append((x, brick[0][1],brick[0][2]))
    
    for y in range(brick[0][1], 1+brick[1][1]):
        points.append((brick[0][0], y, brick[0][2]))
    
    for z in range(brick[0][2], 1+brick[1][2]):
        points.append((brick[0][0], brick[0][1],z))
    
    points = set(points)
    print("points", points)

    # add all cubes of brick 
    octs = []
    for p in points:
        octs.append(myoct.add_elem(p, brick_id))
    
    oct_dict[brick_id] = set(octs)


# print octants
#for k,v in oct_dict.items():
#    print(k,v)


