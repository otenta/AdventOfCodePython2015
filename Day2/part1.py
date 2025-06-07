class Package:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_dimensions(self):
        return 2 * self.length * self.width + 2 * self.width * self.height + 2 * self.height * self.length

    def find_min(self):
        return min(int(self.length * self.width), int(self.height * self.width), int(self.height * self.length))


counter = 0

with open("input.txt") as file:
    lines = file.read().splitlines()
    for i in lines:
        dimensions = i.split("x")
        package = Package(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
        counter += package.calculate_dimensions() + package.find_min()
    print(counter)
