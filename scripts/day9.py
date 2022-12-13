

def move(head, tail):
    xdiff = head[0] - tail[0]
    ydiff = head[1] - tail[1]

    if abs(xdiff) <= 1 and abs(ydiff) <= 1:
        return tail

    x = tail[0]
    y = tail[1]
    if xdiff > 0:
        x += 1
    elif xdiff < 0:
        x -= 1
    if ydiff > 0:
        y += 1
    elif ydiff < 0:
        y -= 1
    return x, y


with open("inputs/09.txt") as f:
    content = f.readlines()

    visited = set([(0, 0)])
    head = (0, 0)
    tail = (0, 0)

    for line in content:
        line = line.strip()
        direction, steps = line.split(" ")

        acts = {
            "R": lambda head: (head[0] + 1, head[1]),
            "L": lambda head: (head[0] - 1, head[1]),
            "U": lambda head: (head[0], head[1] + 1),
            "D": lambda head: (head[0], head[1] - 1)
        }
        for _ in range(int(steps)):
            head = acts[direction](head)
            tail = move(head, tail)
            visited.add(tail)
    print("result 1", len(visited))


with open("inputs/09.txt") as f:
    content = f.readlines()

    visited = set([(0, 0)])
    head = (0, 0)
    tails = [(0, 0)] * 9

    for line in content:
        line = line.strip()
        direction, steps = line.split(" ")

        acts = {
            "R": lambda head: (head[0] + 1, head[1]),
            "L": lambda head: (head[0] - 1, head[1]),
            "U": lambda head: (head[0], head[1] + 1),
            "D": lambda head: (head[0], head[1] - 1)
        }
        for _ in range(int(steps)):
            head = acts[direction](head)
            curr = head
            for i in range(len(tails)):
                curr = move(curr, tails[i])
                tails[i] = curr
            visited.add(tails[len(tails) - 1])
    print("result 2", len(visited))
