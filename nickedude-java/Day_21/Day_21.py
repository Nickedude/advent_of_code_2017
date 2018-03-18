def getSectionAt(art, r, c, dist):
    pattern = []
    i = 0
    for k in range(r, r+dist):
        pattern.append([])
        for p in range(c, c+dist):
            pattern[i].append(art[k][p])
        i += 1
    return pattern

def oneLine(pattern):
    temp = ""
    for i in range(0,len(pattern)):
        for j in range(0,len(pattern[i])):
            temp += pattern[i][j]
        temp += '/'
    return (temp[0:len(temp)-1])                # Don't want the last slash

def mulLine(line):
    pattern = []
    i = 0
    j = 0
    pattern.append([])
    while i < len(line):
        if line[i] == '/':
            pattern.append([])
            j += 1
        else:
            pattern[j].append(line[i])
        i += 1
    return pattern

def flipHorizontal(pattern):
    temp = ""
    size = len(pattern)-1
    for i in range(0,len(pattern)):
        for j in range(0,len(pattern)):
            temp += pattern[i][size-j]
        temp += '/'
    return (temp[0:len(temp)-1])                # Don't want the last slash

def flipVertical(pattern):
    temp = ""
    size = len(pattern)-1
    for i in range(0,len(pattern)):
        for j in range(0,len(pattern)):
            temp += pattern[size-i][size-j]
        temp += '/'
    return (temp[0:len(temp)-1])                # Don't want the last slash

def rotate(pattern):
    newPattern = []
    size = len(pattern)
    for i in range(0,size):
        newPattern.append([])
        for j in range(0,size):
            newPattern[i].append('.')

    for i in range(0,size):
        for j in range(0,size):
            newPattern[i][j] = pattern[j][size-i-1]

    return newPattern

def matchRotations(pattern, rules):
    rotated = rotate(pattern)
    temp = oneLine(rotated)

    if temp in rules:
        return mulLine(rules[temp])

    rotated = rotate(rotated)
    temp = oneLine(rotated)
    if temp in rules:
        return mulLine(rules[temp])

    rotated = rotate(rotated)
    temp = oneLine(rotated)
    if temp in rules:
        return mulLine(rules[temp])

    return None

def match(pattern, rules):

    temp = oneLine(pattern)                 # Try match directly
    if temp in rules:
        return mulLine(rules[temp])

    temp = matchRotations(pattern, rules)   # Try rotating it
    if temp != None:
        return temp

    temp = flipHorizontal(pattern)          # Try flipping horizontally
    if temp in rules:
        return mulLine(rules[temp])


    temp = mulLine(temp)
    temp = matchRotations(temp, rules)      # Try rotating it
    if temp != None:
        return temp

    temp = flipVertical(pattern)            # Try flipping it horizontally
    if temp in rules:
        return mulLine(rules[temp])

    temp = mulLine(temp)
    temp = matchRotations(temp, rules)      # Try rotating it
    if temp != None:
        return temp


    temp = flipVertical(mulLine(flipHorizontal(pattern)))   #Try flipping it along both axis'
    if temp in rules:
        return mulLine(rules[temp])

    temp = mulLine(temp)
    temp = matchRotations(temp, rules)      # Try rotating it
    if temp != None:
        return temp



    print("Something's wrong")



def enhanceThree(art, rules, size):
    newArt = []
    newSize = int((size/3) * 4)

    for i in range(0, newSize):
        newArt.append([])
        for j in range(0,newSize):
            newArt[i].append('.')

    nr = 0
    nc = 0

    print(str(newSize) + " X " + str(newSize))

    i = 0
    while i < size:
        j = 0
        nc = 0
        while j < size:
            pattern = getSectionAt(art, i, j, 3)
            newPattern = match(pattern, rules)
            for r in range(0,len(newPattern)):
                for c in range(0, len(newPattern[r])):
                    newArt[nr+r][nc+c] = newPattern[r][c]
            j += 3
            nc += 4
        i += 3
        nr += 4
    return newArt


def enhanceTwo(art, rules, size):
    newArt = []
    newSize = int((size/2) * 3)

    for i in range(0, newSize):
        newArt.append([])
        for j in range(0,newSize):
            newArt[i].append('.')

    nr = 0
    nc = 0

    print(str(newSize) + " X " + str(newSize))

    i = 0
    while i < size:
        j = 0
        nc = 0
        while j < size:
            pattern = getSectionAt(art, i, j, 2)
            newPattern = match(pattern, rules)
            for r in range(0,3):
                for c in range(0, 3):
                    newArt[nr+r][nc+c] = newPattern[r][c]
            j +=2
            nc += 3
        i += 2
        nr += 3
    return newArt




inputFile = open('Day_21.txt')
ruleLines = inputFile.readlines()

rules = {}
for i in range(0, len(ruleLines)):
    s = ruleLines[i]
    j = 0
    while s[j] != ' ':
        j += 1
    inp = s[0:j]
    j += 4
    outp = s[j:len(s)-1]
    rules[inp] = outp

art = []
art.append(['.','#','.'])
art.append(['.','.','#'])
art.append(['#','#','#'])
size = len(art)

for i in range(0,5):
    if (size % 3) == 0:
        art = enhanceThree(art, rules, size)
    elif (size % 2) == 0:
        art = enhanceTwo(art,rules, size)
    else:
        raise ValueError("Illegal size: " + str(size))
    size = len(art)
    for j in range(0,size):
        print(art[j])
    print()

count = 0
for i in range(0,len(art)):
    for j in range(0,len(art[0])):
        if art[i][j] == '#':
            count += 1

print(count)
