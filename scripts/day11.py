import re

program = """
old = %d
%s
"""


class Monkey:
    def __init__(self, id, items, op, divisor, true_monkey, false_monkey):
        self.id = int(id)
        self.items = [int(i) for i in items.split(", ")]
        self.inspections = 0
        self.op = op
        self.divisor = int(divisor)
        self.true_monkey = int(true_monkey)
        self.false_monkey = int(false_monkey)

    def take_turn(self, prod):
        self.inspections += 1
        item = self.items.pop(0)
        loc = {}
        exec(program % (item, self.op), loc)
        # new = loc["new"] // 3
        new = loc["new"]
        new = new % prod
        if new % self.divisor == 0:
            return self.true_monkey, new
        else:
            return self.false_monkey, new

regex = r"""Monkey (?P<id>\d+):
  Starting items: (?P<items>(\d+, )*\d+)
  Operation: (?P<op>.*)
  Test: divisible by (?P<divisor>\d+)
    If true: throw to monkey (?P<true_monkey>\d+)
    If false: throw to monkey (?P<false_monkey>\d+)
"""

with open("inputs/11.txt") as f:
    content = f.read()
    monkeys = []

    p = re.compile(regex)
    dicts = [m.groupdict() for m in p.finditer(content)]
    monkeys = [Monkey(**d) for d in dicts]

    divisors = [m.divisor for m in monkeys]
    prod = 1
    for d in divisors:
        prod *= d

    rounds = 1000
    rounds = 10000
    for j in range(rounds):
        for i, monkey in enumerate(monkeys):
            while len(monkey.items) > 0:
                to, item = monkey.take_turn(prod)
                monkeys[to].items.append(item)
    order = sorted([m.inspections for m in monkeys], reverse=True)
    print(order)
    print("result 1", order[0] * order[1])

