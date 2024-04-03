import sys

def solve(data:list)->int:
    n = len(data)
    dp = [d.copy() for d in data]
    for i in range(1,n):
        dp[i][0] += min(dp[i-1][1],dp[i-1][2])
        dp[i][1] += min(dp[i-1][0],dp[i-1][2])
        dp[i][2] += min(dp[i-1][0],dp[i-1][1])
    return min(dp[n-1])

data = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
print(solve(data))
