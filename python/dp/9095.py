import sys

def solve(n:int)->int:
    dp = [0] * 12
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,12):
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    return dp[n]


for _ in range(int(sys.stdin.readline())):
    print(solve(int(sys.stdin.readline())))