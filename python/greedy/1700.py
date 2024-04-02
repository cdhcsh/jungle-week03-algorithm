import sys
from heapq import heappush,heappop
def solve(n:int,k:int,data:list)->int:


    distances = [0] * (n+1)
    holes = set()
    answer = 0
    def _find_next_distance(start:int)->int:
        base = data[start]
        for i in range(start+1, len(data)):
            if data[i] == base:
                return i
        else: return 1001

    def _min_dist()->int:
        max = 0
        res = 0
        for n in holes:
            if max < distances[n]:
                max = distances[n]
                res = n
        return res


    for i in range(len(data)):
        t = data[i]
        if len(holes) >= k:
            if t in holes :
                distances[t] = _find_next_distance(i)
                continue
            n = _min_dist()
            holes.remove(n)
            answer += 1
        holes.add(t)
        distances[t] = _find_next_distance(i)

    return answer

k,n = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
print(solve(n,k,data))



