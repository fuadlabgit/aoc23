
def diff(x):
    y = []
    for i in range(1,len(x)):
        y.append(x[i]-x[i-1])
    return y 

def get_level(x):
    l = 0
    diffs = [x]
    while True:
        next_x = diff(diffs[-1])
        if all([nexti == 0 for nexti in next_x]):
            next_x = [0] + next_x
            break 
        diffs.append(next_x)
        l += 1
    return l, diffs

def eval_line(line):
    line = line.strip()
    x = [int(li) for li in line.split()]

    l, diffs = get_level(x)
    
    diffs = list(reversed(diffs))
    print(diffs)

    s = 0
    for i in range(1, len(diffs)):
        
        s = diffs[i][0] - diffs[i-1][0]
        diffs[i][0]  = s
        print("s", s)

    return s

lines = open("input.txt").readlines()

sol = 0
for line in lines:

    val = eval_line(line)
    sol += val

print(sol)
