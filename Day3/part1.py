#This doesn't look like a solid approach
#Figured it out a min later
#Keeping it here for laughs.
#Just use set and don't copy wrong stack overflow answers :P

# def distinct(pairs):
#     stack = []
#     for i in pairs:
#         if (i[0], i[1]) not in stack and (i[0], i[1]) not in stack:
#             stack.append(i)
#     return stack

current_position = (0, 0)
visited_places = set()

#adjust for the starting position
visited_places.add((0,0))

with open("input.txt") as file:
    for direction in file.readline():
        if direction == "^":
            current_position = tuple(sum(x) for x in zip(current_position, (0, 1)))
            visited_places.add((current_position[0], current_position[1]))
        elif direction == ">":
            current_position = tuple(sum(x) for x in zip(current_position, (1, 0)))
            visited_places.add((current_position[0], current_position[1]))
        elif direction == "<":
            current_position = tuple(sum(x) for x in zip(current_position, (-1, 0)))
            visited_places.add((current_position[0], current_position[1]))
        elif direction == "v":
            current_position = tuple(sum(x) for x in zip(current_position, (0, -1)))
            visited_places.add((current_position[0], current_position[1]))

    print(len(visited_places))

