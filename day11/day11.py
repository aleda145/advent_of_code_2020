file = open("input", "r")

database = file.read().splitlines()

# database = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# """

# database = database.splitlines()

# top left is x=0, y=0
# x is first, y is second


def get_adjacent_seats(seat_pos):
    up_seat = (seat_pos[0], seat_pos[1] - 1)
    down_seat = (seat_pos[0], seat_pos[1] + 1)
    left_seat = (seat_pos[0] - 1, seat_pos[1])
    right_seat = (seat_pos[0] + 1, seat_pos[1])

    up_left_seat = (seat_pos[0] - 1, seat_pos[1] - 1)
    up_right_seat = (seat_pos[0] + 1, seat_pos[1] - 1)
    down_left_seat = (seat_pos[0] - 1, seat_pos[1] + 1)
    down_right_seat = (seat_pos[0] + 1, seat_pos[1] + 1)

    return [
        up_seat,
        down_seat,
        left_seat,
        right_seat,
        up_left_seat,
        up_right_seat,
        down_left_seat,
        down_right_seat,
    ]


def count_num_adjacent_occupied(seat_dictionary, adjacents):
    occupied = 0
    for adjacent_seat in adjacents:
        if adjacent_seat in seat_dictionary:
            if seat_dictionary[adjacent_seat] == "#":
                occupied += 1

    return occupied


print(get_adjacent_seats([5, 5]))

seat_dict = {}  # dictionary with tuple as key and value is seat
for row_index, row in enumerate(database):
    for column_index, seat in enumerate(row):
        seat_dict[(row_index, column_index)] = seat

print(seat_dict)

new_seat_dict = {}
num_runs = 0
while True:
    for seat_position, value in seat_dict.items():
        adjacent_seats = get_adjacent_seats(seat_position)
        new_seat_dict[seat_position] = seat_dict[seat_position]
        if value == "L":
            if count_num_adjacent_occupied(seat_dict, adjacent_seats) == 0:
                new_seat_dict[seat_position] = "#"
        elif value == "#":
            if count_num_adjacent_occupied(seat_dict, adjacent_seats) >= 4:
                new_seat_dict[seat_position] = "L"
        elif value == ".":
            pass

    if new_seat_dict == seat_dict:
        print("Stabilized")
        break
    print(f"Run:{num_runs}")
    num_runs += 1
    seat_dict = new_seat_dict.copy()
    list_of_seat_lists = []
    seat_list = []
    for key, value in new_seat_dict.items():
        seat_list.append(value)
        if key[1] == 9:
            list_of_seat_lists.append(seat_list)
            seat_list = []
    print("")
    for s_list in list_of_seat_lists:
        print("".join(s_list))
    print("")
occupied_seats = 0
for key, value in new_seat_dict.items():
    if value == "#":
        occupied_seats += 1

print(occupied_seats)