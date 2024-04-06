import sys
from bisect import bisect_left

def solve(data:list,question:list)->list:
    result = []
    data.sort();
    for q in question:
        d = bisect_left(data,q)
        if d < len(data) and data[d] == q : result.append(d)
        else: result.append(-1)
    return result



n,m = map(int,sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(n)]
question = [int(sys.stdin.readline()) for _ in range(m)]
print(*solve(data,question),sep='\n')