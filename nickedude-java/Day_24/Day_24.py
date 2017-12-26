class Port:
    def __init__(self, inp, outp):
        self.inp = inp
        self.outp = outp

    def __repr__(self):
        return ("(" + str(self.inp) + "," + str(self.outp) + ")")

    def __str__(self):
        return ("(" + str(self.inp) + "," + str(self.outp) + ")")

def findMaxStrength(connection, connectionsToPorts, used, size):
    listOfPorts = connectionsToPorts[connection]
    sizeToReturn = size

    for i in range(0,len(listOfPorts)):
        p = listOfPorts[i]

        if not p in used:
            newUsed = used.copy()
            newUsed.add(p)
            newSize = size + p.inp + p.outp
            k = 0
            if p.inp == connection:
                k = findMaxStrength(p.outp, connectionsToPorts, newUsed, newSize)
            elif p.outp == connection:
                k = findMaxStrength(p.inp, connectionsToPorts, newUsed, newSize)
            else:
                print("Something's wrong")

            if k > sizeToReturn:
                sizeToReturn = k

    return sizeToReturn

def findMaxStrengthAndLength(connection, connectionsToPorts, used, strength, longestStrength):
    listOfPorts = connectionsToPorts[connection]
    strengthToReturn = strength
    longestStrengthToReturn = longestStrength
    lengthToReturn = len(used)

    for i in range(0,len(listOfPorts)):
        p = listOfPorts[i]

        if not p in used:
            newUsed = used.copy()
            newUsed.add(p)
            newStrength = strength + p.inp + p.outp
            newLongestStrength = strength + p.inp + p.outp
            k = 0
            if p.inp == connection:
                (k, p, l) = findMaxStrengthAndLength(p.outp, connectionsToPorts, newUsed, newStrength, newLongestStrength)
            elif p.outp == connection:
                (k, p, l) = findMaxStrengthAndLength(p.inp, connectionsToPorts, newUsed, newStrength, newLongestStrength)
            else:
                print("Something's wrong")

            if k > strengthToReturn:
                strengthToReturn = k

            if l > lengthToReturn:
                lengthToReturn = l
                longestStrengthToReturn = p

    return (strengthToReturn, longestStrengthToReturn, lengthToReturn)

inputFile = open('Day_24.txt')
lines = inputFile.readlines()
ports = []
for i in range(0,len(lines)):
    s = str(lines[i])
    s = s.split('/')
    inp = int(s[0])
    outp = int(s[1])
    p = Port(inp,outp)
    ports.append(p)

starters = []
connectionsToPorts = {}

for i in range(0,len(ports)):
    if (ports[i].inp == 0) | (ports[i].outp == 0):
        starters.append(ports[i])

    inp = ports[i].inp
    outp = ports[i].outp

    if not inp in connectionsToPorts:
        connectionsToPorts[inp] = []

    if not outp in connectionsToPorts:
        connectionsToPorts[outp] = []

    connectionsToPorts[inp].append(ports[i])
    if inp != outp:
        connectionsToPorts[outp].append(ports[i])

maximum = 0
strengthOfLongest = 0
for i in range(0,len(starters)):
    s = set()
    s.add(starters[i])
    if starters[i].inp == 0:
        (a, b, dontCare) = findMaxStrengthAndLength(starters[i].outp, connectionsToPorts, s, starters[i].outp, starters[i].outp)
    else:
        (a, b, dontCare) = findMaxStrengthAndLength(starters[i].inp, connectionsToPorts, s, starters[i].inp, starters[i].inp)

    if a > maximum:
        maximum = a
    if b > strengthOfLongest:
        strengthOfLongest = b

print("Max strength: " + str(maximum))
print("Strength of longest: " + str(strengthOfLongest))
