import sys

def solve(k:int,data:list)->int:
    n = len(data)
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for item in range(1,n+1):
        weight,value = data[item-1][0],data[item-1][1]
        for w in range(k+1):

            if w < weight:
                dp[item][w] = dp[item-1][w]
            else:
                dp[item][w] = max(value + dp[item-1][w-weight],dp[item-1][w])
    return dp[n][k]


n,k = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(solve(k,data))