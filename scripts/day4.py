with open("inputs/04.txt") as f:
    content = f.readlines()


    def range(section_str):
        sec = section_str.split("-")
        return int(sec[0]), int(sec[1])


    total = 0
    for line in content:
        line = line.split(",")
        start1, end1 = range(line[0])
        start2, end2 = range(line[1])

        if start1 <= start2 and end1 >= end2:
            total += 1
        elif start2 <= start1 and end2 >= end1:
            total += 1

    print("total", total)

with open("inputs/04.txt") as f:
    content = f.readlines()


    def range(section_str):
        sec = section_str.split("-")
        return int(sec[0]), int(sec[1])


    total = 0
    for line in content:
        line = line.split(",")
        start1, end1 = range(line[0])
        start2, end2 = range(line[1])

        if start1 <= start2 and end1 >= start2:
            total += 1
        elif start2 <= start1 and end2 >= start1:
            total += 1

    print("total", total)
