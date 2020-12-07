def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return True
    for node in graph[start]:
        if node not in path:
            newpath = find_all_paths(graph, node, end, path)
            if newpath:
                return newpath


file = open("input", "r")

database = file.read().splitlines()

# database = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """
# datebase = database.splitlines()
bag_graph = {}

# shiny gold bag is the root
for row in database:
    bags = row.replace(".", "")
    split_str = bags.split(" bags contain ")
    key = split_str[0]
    if split_str[1] == "no other bags":
        bag_graph[key] = ""
    else:
        value = split_str[1].replace(" bags", "").replace(" bag", "")
        bag_graph[key] = [val[2:] for val in value.split(", ")]

for dic in bag_graph.items():
    print(dic)

num_paths = 0
for key_bag in bag_graph.keys():
    if find_all_paths(bag_graph, key_bag, "shiny gold") and key_bag != "shiny gold":
        print(key_bag + " can reach golden")
        num_paths += 1

print(num_paths)