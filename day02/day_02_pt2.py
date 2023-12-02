import re 

with open("input2.txt") as file:
    lines = file.readlines()

games = []


def convert(s):
    x = {"blue": 0, "red": 0, "green": 0}
    for si in s.split(","):
        x[si.strip().split(" ")[1]] = int(si.strip().split(" ")[0].strip())

    return (x["red"], x["green"], x["blue"])


sols = []

for line in lines:
    my_id = int(line.split(":")[0].split("Game ")[1])

    match = line.split(":")[1]
    
    samples = [i.strip() for i in match.strip().split(";")]
    samples = [convert(i) for i in samples]
    
    u = max(sample_i[0] for sample_i in samples)
    v = max(sample_i[1] for sample_i in samples)
    w = max(sample_i[2] for sample_i in samples)
    print(u,v,w,"   ", u*v*w)
    sols.append(u*v*w)

print(sum(sols))
    