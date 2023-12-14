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
        smudges = 0
        perfect_fit = True  
        for r in rocks:
            dy = k - r.imag + 0.5

            mp = r.real +1j *(r.imag + 2*dy)
            if (mp.imag >=0 and mp.imag < N):
                if mp not in rocks:
                    smudges += 1
                    perfect_fit = False 
                if smudges > 1:
                    break 

        else:
            if not perfect_fit:
                mv = k + 1
                break 


    mh = None
    for i in range(M-1):
        smudges = 0
        perfect_fit = True  

        for r in rocks:
            dx = i - r.real + 0.5

            mp = (r.real + 2*dx) + 1j*(r.imag)
            if (mp.real < M and mp.real >= 0):
                if mp not in rocks:
                    smudges += 1
                    perfect_fit = False  
                if smudges > 1: 
                    break
        
        else:   
            if not perfect_fit:
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
