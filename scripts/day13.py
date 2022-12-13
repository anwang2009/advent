import ast


with open("inputs/13.txt") as f:
    content = f.readlines()

    def read(content):
        item = content.pop(0).strip()
        return ast.literal_eval(item)

    def ordered(left, right):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if right < left:
                return False
            if left == right:
                return None

        if isinstance(left, list) and isinstance(right, int):
            right = [right]
        elif isinstance(left, int) and isinstance(right, list):
            left = [left]
        
        # compare lists
        for i in range(len(left)):
            if i >= len(right):
                return False
            res = ordered(left[i], right[i])
            if res is not None:
                return res
        if len(right) > len(left):
            return True
        return None

    idx = 1
    idx_sum = 0
    while content:
        left = read(content)
        right = read(content)

        if ordered(left, right):
            idx_sum += idx
        idx += 1

        if content:
            content.pop(0)
    print("result 1", idx_sum)


with open("inputs/13.txt") as f:
    content = f.readlines()

    def read(content):
        item = content.pop(0).strip()
        return ast.literal_eval(item)

    def ordered(left, right):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if right < left:
                return False
            if left == right:
                return None

        if isinstance(left, list) and isinstance(right, int):
            right = [right]
        elif isinstance(left, int) and isinstance(right, list):
            left = [left]
        
        # compare lists
        for i in range(len(left)):
            if i >= len(right):
                return False
            res = ordered(left[i], right[i])
            if res is not None:
                return res
        if len(right) > len(left):
            return True
        return None

    packet_left = [[2]]
    packet_right = [[6]]
    packets = []

    idx = 1
    idx_sum = 0
    while content:
        left = read(content)
        right = read(content)
        packets.append(left)
        packets.append(right)

        if content:
            content.pop(0)

    left = 0
    middle = 0
    for p in packets:
        if ordered(p, packet_left):
            left += 1
        elif ordered(p, packet_right):
            middle += 1

    print("result 2", (left + 1) * (left + middle + 2))
