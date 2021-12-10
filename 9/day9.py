with open("input.txt", "r") as f:
    input = f.read().strip().split("\n")
    inputList = [list(map(int, list(row))) for row in input]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(inputList)))
    print("The solution for part 2 is: {0}".format(part2Solution(inputList)))

def part1Solution(inputList):
    risk = []
    for i in range(len(inputList)):
        for j in range(len(inputList[0])):
            neighbors = getNeighbors(inputList, i, j)
            if inputList[i][j] < min(neighbors):
                risk.append(inputList[i][j] + 1)

    return sum(risk)

#def part1Solution(lines):
#    for line in lines:
#        lineList = [ num for num in line.strip()]
#        for i,point in enumerate(lineList):
#            if i <= (len(lineList)-1):
#                if line[i] < line[i+1]:
#                    if line[i] < line [i-1]:
#                        print("horizontal low point discovered. Line: %s  Value :%s" % (line,point))
#    return list(lines)

def part2Solution(lines):
    
    return 2

def getNeighbors(inputList, rowIdx, numIdx):
    neighbors = []
    if rowIdx > 0:
        neighbors.append(inputList[rowIdx - 1][numIdx])
    if rowIdx < len(inputList) - 1:
        neighbors.append(inputList[rowIdx + 1][numIdx])
    if numIdx > 0:
        neighbors.append(inputList[rowIdx][numIdx - 1])
    if numIdx < len(inputList[0]) - 1:
        neighbors.append(inputList[rowIdx][numIdx + 1])
    return neighbors

if __name__ == "__main__":
    main()
