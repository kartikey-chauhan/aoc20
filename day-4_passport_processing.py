import re


with open('./advent_of_code/files/day-4_input.txt', mode='r') as f:
    puzzle_input = [input.replace('\n', ' ')
                    for input in f.read().split('\n\n')]

fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']  # ,'cid']

valid_list = []

for input in puzzle_input:
    valid_flag = 0
    for field in fields:
        if field not in input:
            valid_flag = 1

    valid_list.append(valid_flag == 0)

# print(valid_list.count(True))

# Part 2

def length(i):
    return len(str(i))

def num_digits(n):
    count = 0
    while(n > 0):
        count = count+1
        n = n//10
    return count


valid_list = []
#puzzle_input = ["hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"]
for input in puzzle_input:
    input_dict = dict((x.strip(), y.strip()) for x, y in (
        element.split(':') for element in input.split(' ')))
    print(input_dict)
    valid_flag = 1

    try:
        byr = int(input_dict['byr'])
        iyr = int(input_dict['iyr'])
        eyr = int(input_dict['eyr'])
        hgt = input_dict['hgt']
        hcl = input_dict['hcl']
        ecl = input_dict['ecl']
        pid = input_dict['pid']
        #cid = input_dict['cid']

        # four digits; at least 1920 and at most 2002.
        if not (1920 <= byr <= 2002 and num_digits(byr) == 4):
            print("Invalid byr "+str(byr))
            valid_flag = 0

        # four digits; at least 2010 and at most 2020.
        if not (2010 <= iyr <= 2020 and num_digits(iyr) == 4):
            print("Invalid iyr "+str(iyr))
            valid_flag = 0

        # four digits; at least 2020 and at most 2030.
        if not (2020 <= eyr <= 2030 and num_digits(eyr) == 4):
            print("Invalid eyr "+str(eyr))
            valid_flag = 0

        # hgt (Height) - a number followed by either cm or in:
        # If in, the number must be at least 59 and at most 76.
        if hgt[-2:] not in ['in', 'cm'] or not hgt[:-2].isnumeric():
            valid_flag = 0
        if hgt[-2:] == 'in' and not (59 <= int(hgt[:-2]) <= 76):
            print("Invalid hgt in")
            valid_flag = 0

        # If cm, the number must be at least 150 and at most 193.
        if hgt[-2:] == 'cm' and not (150 <= int(hgt[:-2]) <= 193):
            print("Invalid hgt cm")
            valid_flag = 0

        # a # followed by exactly six characters 0-9 or a-f
        if not (bool(re.match(r"#[0-9a-f]+", hcl)) and length(hcl) == 7):
            print("Invalid hcl")
            valid_flag = 0

        # exactly one of: amb blu brn gry grn hzl oth.
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            print("Invalid ecl")
            valid_flag = 0

        # a nine-digit number, including leading zeroes.
        if not (pid.isnumeric() and length(pid) == 9):
            print("Invalid pid")
            valid_flag = 0

    except KeyError:
        valid_flag = 0

    valid_list.append(valid_flag == 1)

print(valid_list.count(True))
