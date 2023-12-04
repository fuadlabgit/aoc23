

with open("input.txt","r") as file:
    lines = file.readlines()

worth = 0 

for line in lines:
    set1 = set(line.split(":")[1].split("|")[0].strip().split(" "))
    set2 = set(line.split(":")[1].split("|")[1].strip().split(" "))

    if "" in set1:
        set1.remove("")
    if "" in set2:
        set2.remove("")
        
    set12 = set1 & set2
    if len(set12) > 0:
        worth += 2**(len(set12)-1)
    print(set12, "--->",  2**(len(set12)-1))
print(worth)

