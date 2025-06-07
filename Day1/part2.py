stack = []

with open("input.txt") as file:
    counter = 0
    for i in file.readline():
        counter += 1
        if not stack and i == ")":
            print(counter)
            break
        if i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()

