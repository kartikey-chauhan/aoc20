# Using readlines() 
file = open('./advent_of_code/files/day-1_input.txt', 'r') 
lines = [int(x.strip()) for x in file.readlines()]

#print(lines)

# input = []

# for line in lines:
#     input.append(int(line.strip()))

x=len(lines)

#print(x)

for indx in range(0,x):
    #Search ahead
    for indx2 in range(indx,x):
        if lines[indx] + lines[indx2]==2020:
            print(lines[indx]*lines[indx2])


# #Part two
# for indx in range(0,x):
#     #Search ahead
#     for indx2 in range(indx,x):
#         for indx3 in range(indx2,x):
#             if input[indx] + input[indx2] + input[indx3] ==2020:
#                 print(input[indx]*input[indx2]*input[indx3])

