import time

def proc(n):
    if n % 2 == 0:
        return n//2
    else:
        return (n * 3) + 1

def getMaxCycle(i, j):
    cycles = []
    for n in range(i, j+1):
        loop = 0
        while True:
            loop += 1
            if n == 1:
                break
            n = proc(n)
        cycles.append(loop)

    return max(cycles)

def getMaxCycleWithTable(i, j):
    cycles = []
    for n in range(i, j+1):
        loop = 0
        while True:
            loop += 1
            if n == 1:
                break
            if n > i and (n-i) < len(cycles):
                loop += (cycles[n-i]-1)
                break
            n = proc(n)
        cycles.append(loop)

    return max(cycles)

def getCycle(n, loop):
    if n == 1:
        return loop
    return getCycle(proc(n), loop+1)

def getMaxCycleByRecursive(i, j):
    cycles = []
    for n in range(i, j+1):
        cycles.append(getCycle(n, 1))
    return max(cycles)

input = [(1, 10), (100, 200), (1000, 2000)]
print('without table:')
start = time.time()
for (i, j) in input:
    print(f'{i} {j} {getMaxCycle(i, j)}')
print(time.time()-start)

print('with table:')
start = time.time()
for (i, j) in input:
    print(f'{i} {j} {getMaxCycleWithTable(i, j)}')
print(time.time()-start)

print('by recursive:')
start = time.time()
for (i, j) in input:
    print(f'{i} {j} {getMaxCycleByRecursive(i, j)}')
print(time.time()-start)