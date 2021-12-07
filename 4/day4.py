
class Board:
    def __init__(self, grid=[]):
        self.grid = grid

def main():
    print(parseInput())
    #print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    #print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    solution=1
    return solution

def part2Solution(lines):
    solution=2
    return solution

def parseInput():
    with open('input.txt') as f:
        balls = [int(x) for x in f.readline().strip().split(',')]
        boards = []
        currentBoard = []
        for line in f.read().splitlines():
            if line == '\n':
                boards.append(Board(currentBoard))
                current_board = []
            else:
                row = [int(x) for x in line.strip.split(' ')]
                currentBoard.append(row)
    
    return balls, boards

if __name__ == "__main__":
    main()
