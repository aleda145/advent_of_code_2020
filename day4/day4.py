file = open("input","r")

database = file.read().splitlines()

def check_if_valid_passport(passport):
    valid_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    }
    optional = "cid"
    valid_count = 0
    pass_fields = passport.split(" ")
    pass_set = set()
    num_fields = 0
    for pass_field in pass_fields:
        if pass_field != "":
            pass_key = pass_field.split(":")[0]
            if pass_key != optional:
                num_fields += 1
                pass_set.add(pass_key)
    if pass_set == valid_fields and num_fields == 7:
        return True
    else:
        print("missing:")
        print(valid_fields-pass_set)
        return False


passport = ""
passport_list = []
for row in database:
    passport+=(" "+ row)
    #print(row)
    if row =="":
        passport_list.append(passport)
        passport = ""


print(passport_list)
print(len(passport_list))
valid_pass = 0
for passport in passport_list:
    print(passport)
    if check_if_valid_passport(passport):
        valid_pass += 1
        print("valid!")
    

print(valid_pass)
    