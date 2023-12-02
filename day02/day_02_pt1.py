import re 

with open("input.txt") as file:
    lines = file.readlines()

games = []


def convert(s):
    x = {"blue": 0, "red": 0, "green": 0}
    for si in s.split(","):
        x[si.strip().split(" ")[1]] = int(si.strip().split(" ")[0].strip())

    return (x["red"], x["green"], x["blue"])

def valid(sample):
    if sample[0] <= 12 and sample[1] <= 13 and sample[2] <= 14:
        return True 
    return False 

ids = []

for line in lines:
    my_id = int(line.split(":")[0].split("Game ")[1])

    match = line.split(":")[1]
    
    samples = [i.strip() for i in match.strip().split(";")]
    samples = [convert(i) for i in samples]
    
    for sample in samples:
        if not valid(sample):
            break 
    else:
        ids.append(my_id)

print(ids)
print(sum(ids))
    