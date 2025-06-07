with open("input.txt") as file:
    counter = 0
    for i in file.readline():
        if i == "(":
            counter += 1
        else:
            counter -= 1
    print(counter)