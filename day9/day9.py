# database = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576"""

# database = database.splitlines()

file = open("input", "r")
database = file.read().splitlines()

preamble_num = 25


def get_possible_numbers(number_list):
    possible_nums = []
    for num_1 in number_list:
        for num_2 in number_list:
            if num_1 + num_2 not in possible_nums:
                possible_nums.append(num_1 + num_2)
    return possible_nums


def check_if_num_is_valid(number, previous):
    print(number)
    num_list = list(map(int, previous))
    possible_numbers = get_possible_numbers(num_list)
    possible_numbers.sort()
    print(possible_numbers)
    if number in possible_numbers:
        return True
    else:
        return False


for index, num in enumerate(database):
    if index < preamble_num:
        print(num)
    else:
        previous_num = database[index - preamble_num : index]
        if not check_if_num_is_valid(int(num), previous_num):
            print("found!")
            print(num)
            break
