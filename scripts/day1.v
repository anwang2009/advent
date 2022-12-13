import os
import strconv
import math.stats

lines := os.read_lines('inputs/01.txt')! // returned []string with lines (null terminated strings)


mut calories := []int{}
mut acc := 0
for line in lines {
    calorie := strconv.atoi(line) or { -1 }
    if calorie < 0 {
        calories << acc
        acc = 0
    } else {
        acc += calorie
    }
}

mut sum := 0
for i in 0 .. 3 {
    idx := stats.max_index(calories)
    max := calories[idx]
    println('max ${max}')
    sum += max 
    calories.delete(idx)
}
println('sum ${sum}')
