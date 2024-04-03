import sys

def solve(data:list)->int:
    if len(data) < 3:
        return sum(data)
    dp = [0] * len(data)
    dp[0] = data[0]
    dp[1] = dp[0] + data[1]
    dp[2] = max(data[0],data[1])+data[2]
    for i in range(3,len(dp)):
        dp[i] = max(dp[i-3]+data[i-1],dp[i-2]) + data[i]
    return dp[-1]



data = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
print(solve(data))
