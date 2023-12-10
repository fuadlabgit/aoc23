
class Node:
    instances = {}
    def __init__(self, val, children=None):
        self.val = val 
        self.__class__.instances[val] = self 
        
        if children is None:
            self.children = []
        self.children = children

    def __repr__(self):
        return "<%s = (%s)>" % (self.val, self.children)

lines = open("input.txt","r").readlines()
instructions = list(lines[0].strip())
# print("instructions", instructions)

for line in lines[2:]:    
    s = line.split()[0]
    e = line.split("=")[1].strip()[1:-1].split(", ")
    Node(s, e)

startname = "AAA" # lines[2].split()[0]
startnode = Node.instances[startname]

buf = {}

def iter_path(startnode, instructions, step0 = 0, visited = None):

    if startnode in buf:
        return buf[startnode] 
    
    n = startnode 
    step = step0

    for ins in instructions:
        
        if n.val == "ZZZ":
            break 
        
        if ins == "L":
            n = Node.instances[n.children[0]]
        else: # elif ins == "R":
            n = Node.instances[n.children[1]]
        
        # assert isinstance(n, Node)

        if visited is not None:
            if n in visited:
                visited[n] += 1
            else:
                visited[n] = 1 
        
        step += 1

    endnode = n
    buf[startnode] = (endnode, step-step0)
    return endnode, step 


steps = 0
endnode = startnode 
while not endnode.val == "ZZZ":
    endnode, step = iter_path(startnode, instructions, step0 = steps)
    startnode = endnode
    
    steps = step 

# print("BUFFER",len(buf))
print(steps)
