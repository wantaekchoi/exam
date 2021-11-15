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
            if n > i and (n-i) < len(cycles):
                loop += (cycles[n-i]-1)
                break
            n = proc(n)
        cycles.append(loop)
    return max(cycles)

start = time.time()
input = [(1, 10), (100, 200), (1000, 2000)]
for (i, j) in input:
    msg = f'{i} {j} {getMaxCycle(i, j)}'
    print(msg)
print(time.time()-start)
