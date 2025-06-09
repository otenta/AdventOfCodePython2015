current_position = (0, 0)
visited_places = set()

current_santa = (0, 0)
current_robot = (0, 0)

# adjust for the starting position
visited_places.add((0, 0))

#Dumb duplicate code just to find the solution

#This looks like a better solution, but i still think these statements are a bit much
def update_coordinates(current_state, visited):
    if direction == "^":
        current_state = tuple(sum(x) for x in zip(current_state, (0, 1)))
        visited.add((current_state[0], current_state[1]))
    elif direction == ">":
        current_state = tuple(sum(x) for x in zip(current_state, (1, 0)))
        visited.add((current_state[0], current_state[1]))
    elif direction == "<":
        current_state = tuple(sum(x) for x in zip(current_state, (-1, 0)))
        visited.add((current_state[0], current_state[1]))
    elif direction == "v":
        current_state = tuple(sum(x) for x in zip(current_state, (0, -1)))
        visited.add((current_state[0], current_state[1]))
    return visited, current_state

counter = 0

with open("input.txt") as file:
    for direction in file.readline():
        if counter % 2 == 0:
            visited_places, current_santa = update_coordinates(current_santa, visited_places)

            # if direction == "^":
            #     current_santa = tuple(sum(x) for x in zip(current_santa, (0, 1)))
            #     visited_places.add((current_santa[0], current_santa[1]))
            # elif direction == ">":
            #     current_santa = tuple(sum(x) for x in zip(current_santa, (1, 0)))
            #     visited_places.add((current_santa[0], current_santa[1]))
            # elif direction == "<":
            #     current_santa = tuple(sum(x) for x in zip(current_santa, (-1, 0)))
            #     visited_places.add((current_santa[0], current_santa[1]))
            # elif direction == "v":
            #     current_santa = tuple(sum(x) for x in zip(current_santa, (0, -1)))
            #     visited_places.add((current_santa[0], current_santa[1]))
        else:
            visited_places, current_robot = update_coordinates(current_robot, visited_places)

            # if direction == "^":
            #     current_robot = tuple(sum(x) for x in zip(current_robot, (0, 1)))
            #     visited_places.add((current_robot[0], current_robot[1]))
            # elif direction == ">":
            #     current_robot = tuple(sum(x) for x in zip(current_robot, (1, 0)))
            #     visited_places.add((current_robot[0], current_robot[1]))
            # elif direction == "<":
            #     current_robot = tuple(sum(x) for x in zip(current_robot, (-1, 0)))
            #     visited_places.add((current_robot[0], current_robot[1]))
            # elif direction == "v":
            #     current_robot = tuple(sum(x) for x in zip(current_robot, (0, -1)))
            #     visited_places.add((current_robot[0], current_robot[1]))

        counter += 1

    print(len(visited_places))
