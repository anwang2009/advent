import os

lines := os.read_lines('inputs/02.txt')! // returned []string with lines (null terminated strings)


mut score := 0
mut acc := 0
for line in lines {
    round := line.split(" ")
    opp := round[0][0] - "A"[0]
    me := round[1][0] - "X"[0]

    // Score points for the item selected
    score += me + 1
    if me == opp + 1 || (me == 0 && opp == 2) {
        score += 6
    } else if me == opp {
        score += 3
    }
}
println('score ${score}')

score = 0
mut count := 3
for line in lines {
    round := line.split(" ")
    println("round ${round}")
    opp := round[0][0] - "A"[0]
    me := round[1]

    if me == "Z" {
        score += 6
        println("opp ${opp}, opp + 1 ${(opp + 1) % 3}")
        score += ((opp + 1) % 3) + 1
    } else if me == "Y" {
        score += 3
        score += opp + 1
        println("opp ${opp}, opp + 1 ${(opp + 1)}")
    } else {
        score += 0
        score += ((2 + opp) % 3) + 1
        println("opp ${opp}, opp - 1 ${(opp + 2) % 3}")
    }
    count -= 1
    if count == 0 {
        continue
    }
}
println('score ${score}')
