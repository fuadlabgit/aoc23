
with open("input.txt","r") as file:
    lines = file.readlines()


# create card buffer
buf = {}
counter = {} 

for line in lines:

    card_no = line.split(":")[0].split("Card")[1].strip()
    if card_no in buf:
        continue
    
    set1 = set(line.split(":")[1].split("|")[0].strip().split(" "))
    set2 = set(line.split(":")[1].split("|")[1].strip().split(" "))
    

    if "" in set1:
        set1.remove("")
    if "" in set2:
        set2.remove("")
        
    set12 = set1 & set2
    # print(card_no, set12)

    if len(set12) > 0:
        worth = 2**(len(set12)-1)
        buf[int(card_no)] = (worth, len(set12))
    else:
        buf[int(card_no)] = (0, 0)
    
    counter[int(card_no)] = 1

#print(buf)        

# draw from buffer until stack is empty
deck = list(buf.keys())
tot_worth = 0

# iterate through the buffer
for k in deck:
    #print("pop", k) 
    worth, n_wins = buf[k]
    
    count = counter[k]
    for l in range(count):
        for i in range(n_wins):
            new_card = k + 1 + i 
            #print("     win", new_card)
            counter[new_card] += 1

print(sum(counter.values()))

    

