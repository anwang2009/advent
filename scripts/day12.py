
with open("inputs/12.txt") as f:
    content = f.readlines()
    content = [l.strip() for l in content]

    height = len(content)
    width = len(content[0])
    max = 99999
    grid = [[max] * width for _ in range(height)]

    E = None
    starts = []
    a = ord('a')
    elevations = [[max] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            c = content[i][j]
            if c == "S" or c == 'a':
                elevations[i][j] = 0
                starts.append((i, j))
            elif c == "E":
                elevations[i][j] = 26
                E = (i, j)
            else:
                elevations[i][j] = ord(c) - a
    import copy
    ends = []
    print(len(starts))
    for i, s in enumerate(starts):
        g = copy.deepcopy(grid)

        to_visit = [(s, 0)]
        g[s[0]][s[1]] = 0

        steps = 0

        def assign_step(p, steps, prev_elevation):
            i, j = p
            if i < 0 or i >= height:
                return
            if j < 0 or j >= width:
                return
            count = g[i][j]
            elevation = elevations[i][j]
            if elevation <= 1 + prev_elevation:
                if count > steps:
                    g[i][j] = steps
                    return p
            return

        while to_visit:
            p, steps = to_visit.pop(0)
            i, j = p
            r = (i + 1, j)
            l = (i - 1, j)
            u = (i, j + 1)
            d = (i, j - 1)
            points = [r, l, u, d]
            ele = elevations[i][j]

            for p in points:
                p = assign_step(p, steps + 1, ele)
                if p is not None:
                    to_visit.append((p, steps + 1))

        ends.append(g[E[0]][E[1]])
    print("result 2", min(ends))



with open("inputs/12.txt") as f:
    content = f.readlines()
    content = [l.strip() for l in content]

    height = len(content)
    width = len(content[0])
    max = 99999
    grid = [[max] * width for _ in range(height)]

    a = ord('a')
    S = None
    E = None
    elevations = [[max] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            c = content[i][j]
            if c == "S":
                elevations[i][j] = -1
                S = (i, j)
            elif c == "E":
                elevations[i][j] = 26
                E = (i, j)
            else:
                elevations[i][j] = ord(c) - a

    to_visit = [(S, 0)]
    grid[S[0]][S[1]] = 0

    steps = 0

    def assign_step(p, steps, prev_elevation):
        i, j = p
        if i < 0 or i >= height:
            return
        if j < 0 or j >= width:
            return
        count = grid[i][j]
        elevation = elevations[i][j]
        if elevation <= 1 + prev_elevation:
            if count > steps:
                grid[i][j] = steps
                return p
        return

    while to_visit:
        p, steps = to_visit.pop(0)
        i, j = p
        r = (i + 1, j)
        l = (i - 1, j)
        u = (i, j + 1)
        d = (i, j - 1)
        points = [r, l, u, d]
        ele = elevations[i][j]

        for p in points:
            p = assign_step(p, steps + 1, ele)
            if p is not None:
                to_visit.append((p, steps + 1))

    print("result 1", grid[E[0]][E[1]])
