database = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
database = database.splitlines()

file = open("input", "r")

database = file.read().splitlines()

inst_list = []
for instruction in database:
    inst_list.append(instruction)

index = 0
accum = 0
visited_indexes = []
booting = True
while booting:
    op = inst_list[index][0:3]
    print(inst_list[index])
    visited_indexes.append(index)
    if op == "nop":
        index += 1
    elif op == "acc":
        if inst_list[index][4] == "+":
            accum += int(inst_list[index][5:])
        elif inst_list[index][4] == "-":
            accum -= int(inst_list[index][5:])
        index += 1

    elif op == "jmp":
        if inst_list[index][4] == "+":
            index += int(inst_list[index][5:])
        elif inst_list[index][4] == "-":
            index -= int(inst_list[index][5:])
            if index in visited_indexes:
                booting = False

print(accum)