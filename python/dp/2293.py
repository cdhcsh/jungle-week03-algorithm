import sys

def solve(n:int,target:int,coins:list)->int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin,target+1):
            dp[i] += dp[i-coin]
    return dp[-1]

n,k = map(int,sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
print(solve(n,k,coins))