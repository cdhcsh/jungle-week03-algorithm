import sys
def solve(n:int)->int:
    dp = [sys.maxsize] * (n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2,n+1):
        dp[i] = dp[i-1]
        if i % 2 == 0 : dp[i] = min(dp[i//2],dp[i])
        if i % 3 == 0 : dp[i] = min(dp[i//3],dp[i])
        dp[i] += 1
    return dp[n]

print(solve(int(input())))