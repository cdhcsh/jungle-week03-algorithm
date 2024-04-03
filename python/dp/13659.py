import sys

def solve(data:list,order:list)->list:
    result = []
    for i in range(1,len(data)):
        data[i] += data[i-1]
    for s,e in order:
        if s == 1: result.append(data[e-1])
        else : result.append(data[e-1]-data[s-2])
    return result


n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
order = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
print(*solve(data,order),sep='\n')