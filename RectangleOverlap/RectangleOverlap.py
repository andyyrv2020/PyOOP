class Rectangle:
    def __init__(self, id, width, height, x, y):
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def overlaps(self, other):
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            return True
        return False

def main():
    n, m = map(int, input().split())
    rectangles = {}

    for _ in range(n):
        data = input().split()
        id = data[0]
        width = int(data[1])
        height = int(data[2])
        x = int(data[3])
        y = int(data[4])
        rectangles[id] = Rectangle(id, width, height, x, y)

    for _ in range(m):
        id1, id2 = input().split()
        if rectangles[id1].overlaps(rectangles[id2]):
            print("true")
        else:
            print("false")

if __name__ == "__main__":
    main()

