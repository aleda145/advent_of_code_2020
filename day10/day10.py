file = open("input", "r")

database = file.read().splitlines()

# database = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# """

# database = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3
# """

# database = database.splitlines()

jolt_list = list(map(int, database))
jolt_list.append(0)
jolt_list.sort()
print(jolt_list)
num_threes = 1  # because we always add one
num_ones = 0

for index, adapter in enumerate(jolt_list):
    if index < len(jolt_list) - 1:
        next_adapter = jolt_list[index + 1] - adapter
        print(next_adapter)
        if next_adapter == 3:
            num_threes += 1
        elif next_adapter == 1:
            num_ones += 1


print("num_ones:")
print(num_ones)
print("num_threes")
print(num_threes)
print("answer:")
print(num_threes * num_ones)
