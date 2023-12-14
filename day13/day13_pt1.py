maps=open("input.txt").read()
 
def read_map(map):
    rocks = []
    
    for x in range(M):
        for y in range(N):
            if map[y][x] == "#":
                rocks.append(x+1j*y)
    
    return rocks 

sol = 0 

for map in maps.split("\n\n"):
    #print("\n\n")
    #print(map)
    #print("\n")
    
    map = map.strip().split("\n")
    N = len(map)
    M = len(map[0])
    
    rocks = read_map(map)
    
    mv = None   
    for k in range(N-1):
        for r in rocks:
            dy = k - r.imag + 0.5

            mp = r.real +1j *(r.imag + 2*dy)
            if (not mp in rocks) and (mp.imag >=0 and mp.imag < N):
                break
    
        else:
            mv = k + 1
            break 
    
    mh = None
    for i in range(M-1):
        for r in rocks:
            dx = i - r.real + 0.5
            mp = (r.real + 2*dx) + 1j*(r.imag)
            if (not mp in rocks) and (mp.real < M and mp.real >= 0):
                break
        else:
            mh = i + 1
            break
    
    #print(mh,mv)
    res = 0
    if mh is not None:
        res += mh
    if mv is not None:
        res += mv*100
    
    #print(mh,mv,res)
    sol += res 

print(sol)
