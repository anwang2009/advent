import re
from collections import deque


class Crates():
    def __init__(self, lines):
        num = lines[-1]
        stacks = re.findall(r'\d+', lines[-1])
        self.stacks = {}
        for stack in stacks:
            self.stacks[int(stack)] = deque()

        for i in range(-2, -len(lines) - 1, -1):
            line = lines[i]
            for s in range(1, len(self.stacks) + 1):
                j = 1 + ((s - 1) * 4)
                if j >= len(line):
                    break
                c = line[j]
                if c != " ":
                    self.stacks[s].append(c)

    def move(self, num, start, dest):
        start_stack = self.stacks[start]
        end_stack = self.stacks[dest]
        for i in range(num):
            end_stack.append(start_stack.pop())

    def move_2(self, num, start, dest):
        start_stack = self.stacks[start]
        end_stack = self.stacks[dest]
        items = []
        for i in range(num):
            items.append(start_stack.pop())
        for i in range(num):
            end_stack.append(items.pop())

    def tops(self):
        ret = ""
        for i in range(1, len(self.stacks) + 1):
            ret += self.stacks[i].pop()
        return ret


with open("inputs/05.txt") as f:
    content = f.readlines()
    
    crate_lines = []
    crates = None
    for line in content:
        if crates is None:
            if line == "\n":
                crates = Crates(crate_lines)
                continue
            crate_lines.append(line)

        if crates is not None:
            match = re.search("move (\d+) from (\d+) to (\d+)\n", line)
            crates.move(*[int(i) for i in match.groups()])

    print("res 1", crates.tops())

# part two
with open("inputs/05.txt") as f:
    content = f.readlines()
    
    crate_lines = []
    crates = None
    for line in content:
        if crates is None:
            if line == "\n":
                crates = Crates(crate_lines)
                continue
            crate_lines.append(line)

        if crates is not None:
            match = re.search("move (\d+) from (\d+) to (\d+)\n", line)
            crates.move_2(*[int(i) for i in match.groups()])

    print("res 1", crates.tops())
