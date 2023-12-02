
with open("input.txt") as file:
    lines = file.readlines()

codes = []
for line in lines:

    thiscode = []
    for char in line:
        if char in [str(i) for i in range(10)]:
            thiscode.append(int(char))
        
    codes.append( 10* thiscode[0] + thiscode[-1])

print(sum(codes))