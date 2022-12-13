import os

lines := os.read_lines('inputs/03.txt')! // returned []string with lines (null terminated strings)

mut total := 0
a_up := "A"[0]
a := "a"[0]
for line in lines {
    mut half := []u8{}
    for c in line.substr(line.len/2, line.len) {
        half << c
    }
    for c in line.substr(0, line.len/2) {
        if half.contains(c) {
            if c - a < 0 {
                total += c - a_up + 27
            } else {
                total += c - a + 1
            }
            break
        }
    }
}

println("total part 1 " + total.str())

for line in lines {
}
