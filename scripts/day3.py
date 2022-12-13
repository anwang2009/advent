with open("inputs/03.txt") as f:
    content = f.readlines()

    a = ord('a')
    A = ord('A')
    total = 0
    common_items = set()
    for i, line in enumerate(content):
        items = set([c for c in line.strip()])
        if i % 3 == 0:
            common_items = items
        common_items = common_items.intersection(items)
        if i % 3 == 2:
            c = list(common_items)[0]
            if ord(c) - a < 0:
                total += ord(c) - A + 27
            else:
                total += ord(c) - a + 1
            common_items = set()

    print("total", total)
