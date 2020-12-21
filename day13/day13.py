file = open("input", "r")

database = file.read().splitlines()

# database = """939
# 7,13,x,x,59,x,31,19
# """

# database = database.splitlines()

timestamp = int(database[0])
buses = list(database[1].split(","))
buses = [int(bus) for bus in buses if bus != "x"]

bus_factors = []
bus_dict = {}
import math

for bus in buses:
    bus_factors.append(math.ceil(timestamp / bus) * bus)
    bus_dict[bus] = math.ceil(timestamp / bus) * bus

print(bus_factors)
min_bus_time = min(bus_factors)
chosen_bus = None
for key, value in bus_dict.items():
    if value == min_bus_time:
        chosen_bus = key

print(f"chosen_bus: {chosen_bus}")

waiting_time = min_bus_time - timestamp
print(f"waiting: {waiting_time}")
print(waiting_time * chosen_bus)
