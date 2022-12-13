with open("inputs/06.txt") as f:
    content = f.readlines()
    line = content[0].strip()

    marker = line[:4]
    
    # Get repeats in initial marker
    def get_skip(marker):
        for i in range(len(marker) - 1, -1, -1):
            idx = marker.index(marker[i])
            if idx >= 0 and idx < i:
                skip = idx + 1
                return skip
        return None

    start = 0
    skip = get_skip(marker)
    while True:
        start += skip
        marker = line[start:start+4]
        skip = get_skip(marker)
        if skip is None:
            print("result", start + 4)
            break


with open("inputs/06.txt") as f:
    content = f.readlines()
    line = content[0].strip()

    marker = line[:14]
    
    # Get repeats in initial marker
    def get_skip(marker):
        for i in range(len(marker) - 1, -1, -1):
            idx = marker.index(marker[i])
            if idx >= 0 and idx < i:
                skip = idx + 1
                return skip
        return None

    start = 0
    skip = get_skip(marker)
    while True:
        start += skip
        marker = line[start:start+14]
        skip = get_skip(marker)
        if skip is None:
            print("result 2", start + 14)
            break


