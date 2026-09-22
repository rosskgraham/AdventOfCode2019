w1 = "R8,U5,L5,D3".split(",")
w1_points = set()
w1_points.add((0, 0))
w2_points = set()
w2_points.add((0, 0))


def draw(w1_points: set, w2_points: set):
    x, y = (
        [p[0] for p in w1_points.union(w2_points)],
        [p[1] for p in w1_points.union(w2_points)],
    )
    x_min, x_max, y_min, y_max = min(x), max(x), min(y), max(y)
    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1):
            if (x, y) == (0, 0):
                icon = "o"
            elif (x, y) in w1_points and (x, y) in w2_points:
                icon = "\033[31m+\033[0m"
            elif (x, y) in w1_points:
                icon = "\033[32m+\033[0m"
            elif (x, y) in w2_points:
                icon = "\033[33m+\033[0m"
            else:
                icon = "."
            print(icon, end="")
        print()


def line_points(start_pos: tuple[int], direction: str, distance: int) -> set:
    if direction == "R":
        points = {
            (x, start_pos[1]) for x in range(start_pos[0], start_pos[0] + distance + 1)
        }
    elif direction == "L":
        points = {
            (x, start_pos[1])
            for x in range(start_pos[0], start_pos[0] - distance - 1, -1)
        }
    elif direction == "U":
        points = {
            (start_pos[0], y) for y in range(start_pos[1], start_pos[1] + distance + 1)
        }
    elif direction == "D":
        points = {
            (start_pos[0], y) for y in range(start_pos[1], start_pos[1] - distance - 1, -1)
        }
    return points


# w1_points.add((0, 10))
# w2_points.add((-3, 0))
# w2_points.add((3, 0))

# draw(w1_points, w2_points)

# print(line_points((0, 0), "R", 3))
# print(line_points((0, 0), "L", 3))
# print(line_points((0, 0), "U", 3))
# print(line_points((0, 0), "D", 3))

w1_points = w1_points.union(line_points((0, 0), "R", 3))
w1_points = w1_points.union(line_points((0, 0), "L", 3))
w2_points = w2_points.union(line_points((0, 0), "U", 3))
w1_points = w1_points.union(line_points((0, 0), "D", 3))
draw(w1_points, w2_points)
