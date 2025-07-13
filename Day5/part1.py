import re

pattern_double = r"([a-z])\1"
nice_list = []
forbidden = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]

def check_double(text_to_search):
    return re.search(pattern_double, text_to_search)

def check_not_forbidden(text_to_search):
    return not any(o in text_to_search for o in forbidden)

def check_vowels(text_to_search):
    return sum(1 for char in text_to_search.lower() if char in vowels) >= 3


with open(file="input.txt") as file:
    popo = file.readlines()
    for i in range(0, len(popo)):
        clean_strips = popo[i].strip()
        if check_vowels(clean_strips):
            if check_not_forbidden(clean_strips):
                if check_double(clean_strips):
                    nice_list.append(clean_strips)

    print(len(nice_list))
