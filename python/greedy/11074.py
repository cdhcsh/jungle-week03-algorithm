import sys

def solve(data:list,target:int)->int:
    p = len(data)-1
    cnt = 0
    while target > 0:
        if data[p] <= target:
            k = target // data[p]
            target %= data[p]
            cnt += k
        else : p-=1
    return cnt

n,target = map(int,sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(n)]
print(solve(data,target))