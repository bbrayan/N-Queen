import random
#global variable used everywhere dont touch
rows = []
conflicts = []
n = 0

def board(_n):
    global rows
    global conflicts
    global n
    n = _n
    rows = [0] * n
    conflicts = [0] * n
    scramble()

def scramble():
    global rows
    global n
    for i in range(0,n):
        rows[i] = i
    for i in range(n):
        randT = random.randint(0,len(rows)-1)
        rowToSwap = rows[i]
        rows[i] = rows[randT]
        rows[randT] = rowToSwap
    for i in range(n):
        conflicts[i] = num_conflicts(rows[i], i)

def update_conflicts_and_row(oldRow, col, newRow,):
    global rows
    global conflicts
    global n
    newCount = 0
    for i in range(n):
        if (i == col):
            continue
        r = rows[i]
        if(r == newRow or abs(r-newRow) == abs(i - col)):
            newCount += 1
            conflicts[i] += 1
        if(r == oldRow or abs(r-oldRow) == abs(i - col)):
            conflicts[i] -= 1
    conflicts[col] = newCount
    rows[col] = newRow

def num_conflicts(row, col):
    global rows
    count = 0
    for i in range(len(rows)):
        if (i == col):
            continue
        r = rows[i]
        if(r == row or abs(r - row) == abs(i - col)):
            count += 1
    return count

def solve():
    global rows
    global conflicts
    global n
    moves = 0
    while(True):
    #get the worst queen for swap
        maxConflicts = 0
        candidates = []
        for i in range(n):
            confli = conflicts[i]
            if confli == maxConflicts:
                candidates.append(i)
            elif confli > maxConflicts:
                maxConflicts = confli
                candidates.clear()
                candidates.append(i)
        if (maxConflicts == 0):
            print("done")
            return
        worstQueenCol = random.choice(candidates)
        minConflicts = n
        oldRow = rows[worstQueenCol]
        candidates.clear()
        for i in range(n):
            confli = num_conflicts(i, worstQueenCol)
            if confli == minConflicts:
                candidates.append(i)
            elif confli < minConflicts:
                minConflicts = confli
                candidates.clear()
                candidates.append(i)
        newRow = random.choice(candidates)
        update_conflicts_and_row(oldRow, worstQueenCol, newRow)
        moves += 1
        if moves == len(rows) * 2:
            scramble()
            moves = 0

val = int(input("Enter board size: "))
board(val)
solve()
outputFile = open('output.txt', 'w')
for i in range(len(rows)):
    print((" o " * rows[i] + ' X ' + ' o ' * (len(rows)-rows[i]-1)), file = outputFile)
outputFile.close()
