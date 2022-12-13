
def print_tracker(t):
    for line in t:
        print(line)


def mark_visible(line, tracker, row=None, col=None, reversed=False):
    if row is None and col is None:
        assert False
    max = -1
    for j, c in enumerate(line):
        if int(c) > max:
            if row is not None:
                if reversed:
                    tracker[row][len(tracker) - j - 1] = True
                else:
                    tracker[row][j] = True
            else:
                if reversed:
                    tracker[len(tracker) - j - 1][col] = True
                else:
                    tracker[j][col] = True
            max = int(c)


with open("inputs/08.txt") as f:
    content = f.readlines()
    content = [line.strip() for line in content]
    n = len(content[0])

    grid = [[False] * n for _ in range(n)]
    for i, line in enumerate(content):
        mark_visible(line, grid, row=i)
        mark_visible(reversed(line), grid, row=i, reversed=True)

    for j in range(n):
        line = "".join([line[j] for line in content])
        mark_visible(line, grid, col=j)
        mark_visible(reversed(line), grid, col=j, reversed=True)

total = 0
for line in grid:
    total += line.count(True)

print("result 1", total)


def count_visible(c, line):
    count = 0
    for i, item in enumerate(line):
        if int(item) >= c:
            return i + 1
        count += 1
    return count

with open("inputs/08.txt") as f:
    content = f.readlines()
    content = [line.strip() for line in content]
    n = len(content[0])

    max_view = 0
    for i in range(n):
        for j in range(n):
            c = int(content[i][j])

            view = count_visible(c, content[i][j+1:])
            view *= count_visible(c, reversed(content[i][:j]))
            
            line = "".join([line[j] for line in content])
            view *= count_visible(c, line[i+1:])
            view *= count_visible(c, reversed(line[:i]))

            if view > max_view:
                max_view = view

    print("result 2", max_view)
