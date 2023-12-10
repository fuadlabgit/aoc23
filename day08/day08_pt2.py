from itertools import cycle 

class Node:
    instances = {}
    def __init__(self, val, children=None):
        self.val = str(val).strip()
        # print(self.val)
        self.__class__.instances[val] = self 
        
        if children is None:
            self.children = []
        self.children = children

    def __repr__(self):
        return "<%s>" % self.val #  = (%s)>" % (self.val, self.children)

lines = open("input.txt","r").readlines()
instructions = list(lines[0].strip())

for line in lines[2:]:    
    s = line.split()[0]
    e = line.split("=")[1].strip()[1:-1].split(", ")
    Node(s, e)

# start at every node that ends with "A"
startnodes = [] 
for name, node in Node.instances.items():
    if name.endswith("A"):
        startnodes.append(node)

class Turtle:

    def __init__(self, node_pos, instructions):
        self.node_pos = node_pos 
        self.start_pos = node_pos
        self.instructions = cycle([i for i in instructions])
        self.z_positions = []
        self.i = 0

    def iter_path(self, n_steps): 
        
        for k in range(n_steps):

            old_pos = self.node_pos

            ins = next(self.instructions)
            self.i += 1

            if ins == "L":
                self.node_pos  = Node.instances[old_pos.children[0]]
            elif ins == "R":
                self.node_pos  = Node.instances[old_pos.children[1]]
            else:
                raise RuntimeError()
            
            if self.node_pos.val.endswith("Z"):
                self.z_positions.append(self.i) 
                self.i = 0

turtles = {}
turtles = [Turtle(s,instructions) for s in startnodes]
mycycle = cycle(instructions)
[t.iter_path(40_000) for t in turtles ]

s = [t.z_positions[0] for t in turtles ]
print(s)

# see https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(A):
    lcm = 1
    for i in A:
        lcm = lcm * i // gcd(lcm, i)
    return lcm 

print(lcm(s))
