# Using readlines() 
file = open('./advent_of_code/day-2_input.txt', 'r') 
lines = file.readlines() 

def replace(text):
    for ch in [': ','-',' ']:
        if ch in text:
            text = text.replace(ch,',')
    return text

def char_frequency(char,str):
    count=0
    for n in str:
        if char==n:
            count+=1
    return count

input = []
for line in lines:
    input.append(line.strip())

valid_count=0
invalid_count=0
for indx,val in enumerate(input):
    #Replace characters with "commas"
    val=replace(val)
    min=int(val.split(',')[0])
    max=int(val.split(',')[1])
    char=val.split(',')[2]
    pwd=val.split(',')[3]

    count=char_frequency(char,pwd)
    if min <= count <= max: 
        valid_count+=1
    else:
        invalid_count+=1
       
print(valid_count)
print(invalid_count)

valid_count=0
invalid_count=0

#Part 2
for indx,val in enumerate(input):
    #Replace characters with "commas"
    val=replace(val)
    min=int(val.split(',')[0])
    max=int(val.split(',')[1])
    char=val.split(',')[2]
    pwd=val.split(',')[3]

    if pwd[min-1] == char and pwd[max-1] ==char:
        invalid_count+=1
    elif pwd[max-1] ==char:
        valid_count+=1
    elif pwd[min-1]==char:
        valid_count+=1
    else:
        invalid_count+=1

print(valid_count)
print(invalid_count)