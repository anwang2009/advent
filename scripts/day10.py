
with open("inputs/10.txt") as f:
    content = f.readlines()
    for i, line in enumerate(content):
        line = line.strip()
        content[i] = line


    crt = [["."] * 40 for _ in range(6)]
    def print_crt():
        for line in crt:
            print("".join(line))

    inst = 0
    cycle = 1
    X = 1
    strength = 0
    in_progress = False
    change = 0
    print_crt()
    while inst < len(content):
        if cycle % 40 == 20:
            strength += cycle * X
        for x in range(X, X+3):
            if cycle % 40 == x % 40:
                crt[(cycle-1)//40][cycle%40 - 1] = "#"
                break

        if in_progress:
            in_progress = False
            X += change
        else:
            cmd = content[inst]
            if cmd.startswith("addx"):
                change = int(cmd.split(" ")[1])
                in_progress = True
            inst += 1
        cycle += 1

        
    print("result 1", strength)
    print_crt()
