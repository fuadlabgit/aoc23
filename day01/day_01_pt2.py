import re 

with open("input2.txt") as file:
    lines = file.readlines()

#my_input = """two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteen"""
#
#lines = my_input.split("\n")


string_list = {"one": 1,
               "two": 2,
               "three":3,
               "four":4, 
               "five":5, 
               "six": 6,
               "seven":7,
               "eight":8,
               "nine":9, 
               # "ten":10,
               }

for i in range(10):
    string_list[str(i)] = i 


codes = []
for line in lines:
    
    found = re.findall(r"(?=("+'|'.join(list(string_list.keys()))+r"))", line)
    print(found)
    print(line)
    #if len(found) > 0:
    codes.append(string_list[found[0]] * 10 + string_list[found[-1]])

print(sum(codes))
