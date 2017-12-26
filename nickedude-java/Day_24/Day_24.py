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
for i in range(0,len(starters)):
    print("Running: " + str(starters[i]))
    s = set()
    s.add(starters[i])
    if starters[i].inp == 0:
        k = findMaxStrength(starters[i].outp, connectionsToPorts, s, starters[i].outp)
    else:
        k = findMaxStrength(starters[i].inp, connectionsToPorts, s, starters[i].inp)

    if k > maximum:
        maximum = k

print()
print(maximum)
