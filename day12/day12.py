# database = """F10
# N3
# F7
# R90
# F11
# """

# database = database.splitlines()

file = open("input", "r")

database = file.read().splitlines()

east_west_pos = 0  # east is pos, west is neg
north_south_pos = 0  # north is pos, south is neg
facing = "E"


def calc_facing(cur_facing, left_or_right, degrees):
    facing_dict = {"E": 0, "S": 90, "W": 180, "N": 270}

    cur_deg = facing_dict[cur_facing]
    if left_or_right == "L":
        new_deg = cur_deg - degrees
    elif left_or_right == "R":
        new_deg = cur_deg + degrees
    new_deg = new_deg % 360
    for key, val in facing_dict.items():
        if val == new_deg:
            return key


for instruction in database:
    command = instruction[0]
    value = int(instruction[1:])
    print(f"command: {command} value: {value}")
    if command == "N":
        north_south_pos += value
    elif command == "S":
        north_south_pos -= value
    elif command == "E":
        east_west_pos += value
    elif command == "W":
        east_west_pos -= value
    elif command == "L" or command == "R":
        facing = calc_facing(facing, command, value)
    elif command == "F":
        if facing == "E":
            east_west_pos += value
        elif facing == "W":
            east_west_pos -= value
        if facing == "N":
            north_south_pos += value
        elif facing == "S":
            north_south_pos -= value


print(abs(east_west_pos) + abs(north_south_pos))
