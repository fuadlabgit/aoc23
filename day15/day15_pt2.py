#x = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
x = open("input.txt").read().strip()

def hash(x):
    c = 0
    for xi in x:
        c += ord(xi)
        c *= 17 
        c = c % 256 
    return c 


boxes = {255-t: {} for t in range(256)}
labels = [] 

for xi in x.split(","):

    if len(xi.split("=")) > 1:
        # replace 
        label = xi.split("=")[0]
        box_no = hash(label)
        fl = int(xi.split("=")[1])
        boxes[box_no][label] = fl
            
    else:
        # remove 
        label = xi.split("-")[0]
        box_no = hash(label)

        if label in boxes[box_no]:
            del boxes[box_no][label]

    
    if label not in labels:
        labels.append(label)

"""
for t in range(256):
    if len(boxes[t]) > 0:
        print("Box %i: "%t, boxes[t])
"""

fp = {l: 0 for l in labels}

for label in labels:
    for t, box in boxes.items():
        if label in box:
            
            a = t + 1
            b = list(box.keys()).index(label) + 1
            c = box[label] 

            fp[label] += a * b * c 

#for label, power in fp.items():
#    print(label, power)

print(sum(fp.values()))