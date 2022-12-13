
class Fs():
    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.size = 0
        self.files = {}

    def cd(self, d):
        if d == "..":
            return self.parent
        else:
            return self.files[d]

    def lsdir(self, fs):
        self.files[fs.name] = fs

    def ls(self, size, fname):
        if fname not in self.files:
            self.files[fname] = int(size)
            self.update_size(int(size))

    def update_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.update_size(size)
 

with open("inputs/07.txt") as f:
    content = f.readlines()

    all_dirs = []
    curr = Fs("/")
    all_dirs.append(curr)
    root = curr
    assert content[0].strip() == "$ cd /"
    idx = 1
    while idx < len(content):
        line = content[idx].strip()

        if line.startswith("$"):
            cmd = line[2:].split(" ")
            if cmd[0] == "cd":
                if cmd[1] == "/":
                    curr = root
                else:
                    curr = curr.cd(cmd[1])
            elif cmd[0] == "ls":
                idx += 1
                continue
            else:
                assert False
        else:
            if line.startswith("dir"):
                dname = line[4:]
                fs = Fs(dname, parent=curr)
                all_dirs.append(fs)
                curr.lsdir(fs)
            else:
                size, fname = line.split(" ")
                curr.ls(size, fname)
        idx += 1

    tot = 0
    for d in all_dirs:
        if d.size <= 100000:
            tot += d.size
    print("result 1", tot)

    unused = 70000000 - root.size
    need = 30000000 - unused
    min_size = 70000000
    for d in all_dirs:
        if d.size >= need and min_size > d.size:
            print(d.name)
            min_size = d.size
    print("result 2", min_size)
