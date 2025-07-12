import hashlib
import re
pattern = r"^0{5,}" #Same for part 2 but with 6 here

target = 1
count = 0

with open("input.txt") as file:
    secret = file.readline()
    found = False
    while not found:
        to_hash = secret + str(target)
        res = hashlib.md5(to_hash.encode())
        match = re.match(pattern, res.hexdigest())
        if match:
            found = True
            print(f"Target decimal is {target}")
        count = 0
        target +=1


