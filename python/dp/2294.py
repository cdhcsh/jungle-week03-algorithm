import sys

def solve(target:int,data:list)->int:
    dp = [sys.maxsize]*(target+1)
    dp[0] = 0
    for n in data:
        for i in range(target+1-n):
            dp[i+n] = min(dp[i+n],dp[i]+1)

    if dp[target] != sys.maxsize:
        return dp[target]
    else :
        return -1


n,target = map(int,sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(n)]
print(solve(target,data))
