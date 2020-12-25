file = open('./files/day-5_input.txt', 'r') 
lines = [x.strip() for x in file.readlines()]

seats=[]

for line in lines:
    rows= list(range(128))
    cols= list(range(8))
    for i in range(10):
        if i<7: 
            length = len(rows)
            middle_index = length//2
            if line[i]=='B':
                rows=rows[middle_index:]
            if line[i]=='F':
                rows=rows[:middle_index]
        else:
            length = len(cols)
            middle_index = length//2
            if line[i]=='R':
                cols=cols[middle_index:]
            if line[i]=='L':
                cols=cols[:middle_index]
    seats.append((rows[0],cols[0],rows[0]*8+cols[0]))
   
seatid_list =[seat[2] for seat in seats]
all_seats = [(x, y, x*8+y) for x in list(range(1,127)) for y in list(range(8))]

for seat in all_seats :
    if seat not in seats\
    and seat[2] not in seatid_list\
    and seat[2]+1 in seatid_list\
    and seat[2]-1 in seatid_list:

        print(seat)

 