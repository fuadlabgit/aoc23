

map = open("input.txt", "r").readlines()

N = len(map) #height
M = len(map[0])-1 # width

print("M", M, "N", N)
warpx=[]
warpy=[]
 
for x in range(M):
    scanline = "".join([map[i][x] for i in range(N)])
    print("scanline", scanline)
    if all([m == "." for m in scanline.strip()]):
        warpx.append(x)

for y in range(N):
    scanline = "".join(map[y][:])
    print("scanline", scanline)
    if all([n == "." for n in scanline.strip()]):
        warpy.append(y)
 
# print("arpx, warpx", warpx, warpy)
hs=[]
 
for x in range(M):
    for y in range(N):
        if map[y][x] == "#":
            
            offsetx = 0
            offsety = 0
            for wx in warpx:
                if x >   wx:
                    offsetx+=1
                    
            for wy in warpy: 
                if y > wy:
                    offsety+=1
            
            u = x + offsetx 
            v = y + offsety 

            hs.append(u+1j*v)
   
# print(hs)
 
 
def print_map(hs):
 m = 1+int(max([w.real for w in hs]))
 n = 1+int(max([w.imag for w in hs]))
 
 s=""
 for y in range(n):
  line =""
  for x in range(m):
   if x+1j*y in hs: 
    line += "#"
   else:
    line += "."
  s += line + "\n"
 print(s)

print_map(hs)

 
# get the distance between two hotspring coordinates
"""from itertools import permutations
from bresenham import bresenham
def d(start, end):
    # shortest path
    points = list(bresenham(int(start.real), int(start.imag), int(end.real), int(end.imag)))
    pathlen = 0 # len(points)
    for i in range(1, len(points)):
    
        # check for diagonal movements

        # south east
        cond1 =  points[i][1] - points[i-1][1] > 0 and points[i][0] - points[i-1][0] > 0
        
        # north east
        cond2 =  points[i][1] - points[i-1][1] < 0 and points[i][0] - points[i-1][0] > 0
        
        # south west 
        cond3 = points[i][1] - points[i-1][1] > 0 and points[i][0] - points[i-1][0] < 0

        # north west 
        cond4 = points[i][1] - points[i-1][1] < 0 and points[i][0] - points[i-1][0] < 0

        if cond1 or cond2 or cond3 or cond4: 
            pathlen += 2 
        else:
            pathlen += 1
    
    return pathlen 
"""

def d(start, end):
    # shortest path
    dx = abs(int(end.real) - int(start.real))
    dy = abs(int(end.imag) -  int(start.imag))
    
    pathlen = dx + dy 

    return pathlen 



lens = 0 
for i, start in enumerate(hs):
   for j, end in enumerate(hs):
    
    #if start==end or (start, end) in check or (end,start) in check:
    # continue
    if i < j or i == j: 
        continue 
    # print(i, j)

    di = d(start,end)
    print(start,end, di)
    lens += di 
   

print(lens)
# 9647174 