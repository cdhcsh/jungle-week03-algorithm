import sys

def solve(data:list)->int:
    n = len(data)
    data.sort(key=lambda l:(l[1],l[0]))
    answer = 0

    k = 0
    for s,e in data:
        if s >= k:
            answer +=1
            k = e
    return answer



data = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
print(solve(data))