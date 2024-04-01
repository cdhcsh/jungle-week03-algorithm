import sys

def solve(k:int,data:list)->int:
    n = len(data)
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(k+1):
            weight,value = data[i][0],data[i-1][1]

            if j < weight:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(value + dp[i-1][j-weight],dp[i-1][j])
    return dp[n][k]


n,k = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(solve(k,data))