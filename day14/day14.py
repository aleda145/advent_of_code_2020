file = open("input", "r")

database = file.read().splitlines()

# database = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# """
# database = database.splitlines()
mem = {}
mask = ""
for row in database:
    if "mask" in row:
        mask = row.split(" = ")[1]
    elif "mem" in row:
        number = int(row.split(" = ")[1])
        address = int(row.split(" = ")[0].split("mem[")[1][:-1])
        # apply mask
        print(bin(number))
        result = []
        last_index = 0
        result = [char if char != "X" else "0" for char in mask]
        for index, num in enumerate(reversed(bin(number)[2:])):  # [2:] to skip 0b
            print(f"idx: {index}, num: {num}")
            mask_val = mask[len(mask) - index - 1]
            print(f"mask_val : {mask_val}")
            if mask_val == "0" or mask_val == "1":
                print("make change!")
                result[len(result) - index - 1] = mask_val
            else:
                result[len(result) - index - 1] = num
        print("".join(result))
        mem[address] = int("".join(result), 2)


print(sum(mem.values()))