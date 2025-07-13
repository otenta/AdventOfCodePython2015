import re

pattern_double = r"([a-z]{2}).*?\1"
nice_list = []
pattern_separated = r"(.).\1"


def check_double(text_to_search):
    return len(re.findall(pattern_double, text_to_search)) >= 1

def check_separated(text_to_search):
    return re.search(pattern_separated, text_to_search)


with open(file="input.txt") as file:
    popo = file.readlines()
    for i in range(0, len(popo)):
        clean_strips = popo[i].strip()
        if check_separated(clean_strips):
            if check_double(clean_strips):
                nice_list.append(clean_strips)

    print(len(nice_list))
