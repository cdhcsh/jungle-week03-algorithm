import sys

def solve(data:list)->int:
    data.sort(key=lambda l:(l[1],l[0]))
    time = 0
    min_time = sys.maxsize
    for t,e in data:
        if time > e-t:
            break
        min_time = min(min_time,e-t-time)
        time += t
    else:
        return min_time
    return -1

n = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(solve(data))