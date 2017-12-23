
def newInfectedDir(oldDir):
    if oldDir == 'up':
        newDir = 'right'
    elif oldDir == 'right':
        newDir = 'down'
    elif oldDir == 'down':
        newDir = 'left'
    elif oldDir == 'left':
        newDir = 'up'
    else:
        raise ValueError("Illegal direction: " + str(oldDir))
    return newDir

def newCleanDir(oldDir):
    if oldDir == 'up':
        newDir = 'left'
    elif oldDir == 'right':
        newDir = 'up'
    elif oldDir == 'down':
        newDir = 'right'
    elif oldDir == 'left':
        newDir = 'down'
    else:
        raise ValueError("Illegal direction: " + str(oldDir))
    return newDir

def move(row,col,oldDir):
    if oldDir == 'up':
        row -= 1
    elif oldDir == 'right':
        col += 1
    elif oldDir == 'down':
        row += 1
    elif oldDir == 'left':
        col -= 1
    else:
        raise ValueError("Illegal direction: " + str(oldDir))
    return (row,col)

def step(grid,row,col,oldDir,count):
    gridVal = grid[row][col]
    if gridVal == '#':
        newDir = newInfectedDir(oldDir)
        grid[row][col] = '.'
    if gridVal == '.':
        newDir = newCleanDir(oldDir)
        grid[row][col] = '#'
        count += 1
    (row,col) = move(row,col,newDir)
    return(row,col,newDir,count)

inputFile = open('Day_22.txt')
lines = inputFile.readlines()
h = len(lines)
w = len(lines[0]) - 1
size = 1000
grid = []

print(lines)

for i in range(0,size):
    grid.append([])
    for j in range(0, size):
        grid[i].append('.')

hs = int((size/2) - (h/2))
ws = int((size/2) - (w/2))

r = 0
for i in range(hs,(hs+h)):
    c = 0
    for j in range(ws,(ws+w)):
        grid[i][j] = lines[r][c]
        c += 1
    r += 1

rs = int(size/2) - 1
cs = int(size/2) - 1

row = rs
col = cs
myDir = 'up'
count = 0

for i in range(0,10000):
    (row,col,myDir,count) = step(grid,row,col,myDir,count)

print(count)
