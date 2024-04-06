import sys

def solve(n:int)->int:
    dp = [sys.maxsize] * (n+1)
    dp[n] = 0
    for i in range(n,0,-1):
        if i >= 2: dp[i-2] = min(dp[i-2],dp[i]+1)
        if i >= 5: dp[i-5] = min(dp[i-5],dp[i]+1)

    if dp[0] == sys.maxsize:
        return -1
    else :
        return dp[0]


print(solve(int(sys.stdin.readline())))
