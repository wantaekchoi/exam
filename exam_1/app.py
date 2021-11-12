import time

def func(n):
    if n % 2 == 0:
        return n//2
    else:
        return (n * 3) + 1

def proc(i, j):
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
            n = func(n)
        cycles.append(loop)
    msg = f'{i} {j} {max(cycles)}'
    print(msg)

start = time.time()
proc(1, 10)
proc(100, 200)
proc(1000, 2000)
print(time.time()-start)
