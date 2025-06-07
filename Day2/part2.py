class Ribbon:
    def __init__(self, sides):
        self.sides = sides

    def calculate_distance(self):
        return 2 * self.sides[0] + 2 * self.sides[1]

    def calculate_wrapping(self):
        return self.sides[0] * self.sides[1] * self.sides[2]

    def find_shorted(self):
        return max(self.sides[0], self.sides[1], self.sides[2])


counter = 0

with open("input.txt") as file:
    lines = file.read().splitlines()
    for i in lines:
        array = []
        dimensions = i.split("x")

        array.append(int(dimensions[0]))
        array.append(int(dimensions[1]))
        array.append(int(dimensions[2]))

        ribbon = Ribbon(array)

        counter += ribbon.calculate_wrapping()

        array.remove(ribbon.find_shorted())

        counter += ribbon.calculate_distance()

    print(counter)
