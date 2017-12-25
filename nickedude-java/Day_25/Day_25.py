
def stateA(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos += 1
    else:
        tape[pos] = 0
        pos -= 1
    nextState = 'B'
    return(tape,pos,nextState)

def stateB(tape,pos):
    if tape[pos] == 0:
        tape[pos] = 0
        pos += 1
        nextState = 'C'
    else:
        tape[pos] = 1
        pos -= 1
        nextState = 'B'
    return(tape,pos,nextState)

def stateC(tape,pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos += 1
        nextState = 'D'
    else:
        tape[pos] = 0
        pos -= 1
        nextState = 'A'
    return(tape,pos,nextState)

def stateD(tape,pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos -= 1
        nextState = 'E'
    else:
        tape[pos] = 1
        pos -= 1
        nextState = 'F'
    return(tape,pos,nextState)

def stateE(tape,pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos -= 1
        nextState = 'A'
    else:
        tape[pos] = 0
        pos -= 1
        nextState = 'D'
    return(tape,pos,nextState)

def stateF(tape,pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos += 1
        nextState = 'A'
    else:
        tape[pos] = 1
        pos -= 1
        nextState = 'E'
    return(tape,pos,nextState)


nrOfIterations = 12629077

tape = []
for i in range(0,10000):
    tape.append(0)

pos = 5000
state = 'A'
for i in range(0,nrOfIterations):
    if state == 'A':
        (tape, pos, state) = stateA(tape,pos)
    elif state == 'B':
        (tape, pos, state) = stateB(tape,pos)
    elif state == 'C':
        (tape, pos, state) = stateC(tape,pos)
    elif state == 'D':
        (tape, pos, state) = stateD(tape,pos)
    elif state == 'E':
        (tape, pos, state) = stateE(tape,pos)
    elif state == 'F':
        (tape, pos, state) = stateF(tape,pos)

count = 0
for i in range(0,len(tape)):
    if tape[i] == 1:
        count += 1

print(count)
