import sys
input = sys.stdin.readline

def solve(n:int)->int:
    dp = [0] * (n+2)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+2):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n+1]

n = int(input())
print(solve(n))