#!/bin/bash

day=$1
mkdir "./$1"
scriptPath="./$1/day$1.py"
cookie="session=$ADVENT_SESSION"
curl --cookie $cookie https://adventofcode.com/2021/day/$1/input > ./$1/input.txt

cat <<- EOF > $scriptPath
with open('input.txt') as f:
    lines = f.readlines()

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    solution=1
    return solution

def part2Solution(lines):
    solution=2
    return solution

if __name__ == "__main__":
    main()
EOF