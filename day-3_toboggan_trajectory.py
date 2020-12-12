# Using readlines() 
file = open('./advent_of_code/files/day-3_input.txt', 'r') 
lines = file.readlines() 

input = []

def split(word): 
    return [char for char in word]  

for line in lines:
    input.append(line.strip()*100)

count=0

j=0
for i in range(0,len(input)-1):
    #Down 1
    i=i+1
    j+=3
    if split(input[i])[j]=='#':
        count+=1
print(count)


#part2 
path=[(1,1),(3,1),(5,1),(7,1),(1,2)]
print(path)
answer=1
for x,y in path :
    count=0
    j=0
    for i in range(0,len(input)-y,y):
        # try:
            i=i+y
            j=j+x
            if split(input[i])[j]=='#':
                count+=1
        # except IndexError:
        #     break
        #print("Iteration {} , x={}, y={}, count={}".format(i,x,y,count))
    print("count={}".format(count))
    answer=answer*count
print(answer)


##better way
with open('./advent_of_code/files/day-3_input.txt', mode='r') as f:
    puzzle_input = [list(x.strip()) for x in f.readlines()]


def tree_hitting_function(right, down, tree_input):
    # Get the height and width based on the list lengths
    height = len(tree_input)
    width = len(tree_input[0])

    # Set initial values
    trees = 0
    step = 0

    # Walk down the "hill" using range.
    for y in range(down, height, down):
        # We need to track steps down so we know how far to the right.
        step += 1

        # Modulo trick to cycle through the width values and loop back around to the front
        x_axis = (step * right) % width

        # Check if a tree and increment
        if tree_input[y][x_axis] == "#":
            trees += 1

    return trees


def slope_multiplier(slopes, tree_input):
    total = 1

    # Loop through the slopes and calc the trees hit.  Multiply them together.
    for slope in slopes:
        right = slope[0]
        down = slope[1]
        total *= tree_hitting_function(right, down, tree_input)

    return total


if __name__ == '__main__':
    print(tree_hitting_function(3, 1, puzzle_input))

    slope_list = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    print(slope_multiplier(slope_list, puzzle_input))
