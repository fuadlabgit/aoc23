

map = open("input.txt", "r").readlines()

N = len(map) #height
M = len(map[0])-1 # width

# print("M", M, "N", N)
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
                    offsetx+=999_999
                    
            for wy in warpy: 
                if y > wy:
                    offsety+=999_999
            
            u = x + offsetx 
            v = y + offsety 

            hs.append(u+1j*v)
   

# get the distance between two hotspring coordinates

def d(start, end):
    # shortest path
    dx = abs(int(end.real) - int(start.real))
    dy = abs(int(end.imag) -  int(start.imag))
    
    pathlen = dx + dy 

    return pathlen 


#print("LEN(HS)", len(hs))

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
   
# 289729176592 too low 
# 377319269864 too high
# 377318892554 
print(lens)