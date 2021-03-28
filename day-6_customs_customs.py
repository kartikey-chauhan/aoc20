import shlex

with open('./files/day-6_input.txt', mode='r') as f:
    puzzle_input = [input.replace('\n', ' ')
                    for input in f.read().split('\n\n')]

def get_count(str):
    split_str = str.split(' ')
    all_chars = []
    for ans in split_str:
        chars = [char for char in ans]
        for char in chars: 
            all_chars.append(char)
    unique_list = []
    for char in all_chars:
        if char in unique_list:
            continue
        else:
            unique_list.append(char)
    return len(unique_list)

def get_uniq_count(str):
    split_str = str.split(' ')
    all_chars = []
    for ans in split_str:
        chars = [char for char in ans]
        for char in chars: 
            all_chars.append(char)
    
    unique_list = []
    for char in all_chars:
        if char in unique_list:
            continue
        else:
            unique_list.append(char)
    
    count = 0 
    
    for char in unique_list:
        in_all_flag=1
        for str in split_str:
            if char in str:
                continue
            else:
                in_all_flag=0
        
        if in_all_flag == 1:
            count = count +1 

    return count  
        
sum = 0
for group in puzzle_input : 
    sum = sum + get_uniq_count(group)

print(sum)