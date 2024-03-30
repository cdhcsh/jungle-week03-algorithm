import sys

def solve(target:int,data:list)->int:
    dp = [0] * (target+1)
    dp[0] = 1
    for num,k in data:
        tmp = dp.copy()
        for d in range(1,k+1):
            now = num * d
            for i in range(0,target+1-now):
                tmp[i+now] += dp[i]
        dp = tmp
    return dp[target]

target = int(sys.stdin.readline())
n = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(solve(target,data))