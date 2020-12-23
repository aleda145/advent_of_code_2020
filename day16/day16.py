database = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""
database = database.splitlines()
file = open("input", "r")

database = file.read().splitlines()

# from collections import defaultdict

checking_req = True
checking_my_ticket = False
checking_nearby_ticket = False
req_dict = {}
ticket_dict = {}
ticket_num = 0
for row in database:
    if checking_req:
        if "" == row:
            checking_req = False
            checking_my_ticket = True
            continue
        split_req = row.split(":")
        ranges = split_req[1].replace(" ", "").split("or")
        req_dict[split_req[0]] = ranges
    if checking_my_ticket:
        if "" == row:
            checking_my_ticket = False
            checking_nearby_ticket = True
            continue
    if checking_nearby_ticket and row != "nearby tickets:":
        ticket_dict[ticket_num] = row.split(",")
        ticket_num += 1


print(req_dict)
print(ticket_dict)
# range_dict = defaultdict(list)
possible_ranges = []
for key, val in req_dict.items():
    print(key)
    for ticket_range in val:
        print(ticket_range)
        lower = int(ticket_range.split("-")[0])
        upper = int(ticket_range.split("-")[1])
        # range_dict[key].append(range(lower, (upper + 1)))
        possible_ranges.append(range(lower, (upper + 1)))
print(possible_ranges)
invalid_range = []
for ticket, ticket_ranges in ticket_dict.items():
    print(f"{ticket}, ranges: {ticket_ranges}")
    for ticket_range in ticket_ranges:
        if (any([int(ticket_range) in rng for rng in possible_ranges])) == False:
            invalid_range.append(int(ticket_range))

print(invalid_range)
print(sum(invalid_range))