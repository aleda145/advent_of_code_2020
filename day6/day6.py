file = open("input", "r")

database = file.read().splitlines()

database.append("")
answers_list = []
answers = ""
for row in database:
    answers += row
    if row == "":
        answers_list.append(answers)
        answers = ""

print(answers_list)

# get unique chars in each string
# just make it a list of sets!
answers_set = []
for answers in answers_list:
    answers_set.append(set(answers))

print(answers_set)

count = 0
for answers in answers_set:
    count += len(answers)

print(count)