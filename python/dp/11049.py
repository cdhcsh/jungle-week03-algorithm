import sys

def solve(data:list)->int:
    dp = [[0] * (n) for _ in range(n)]

    for level in range(1, n):
        for i in range(n):
            j = i + level
            if j == n:
                break
            dp[i][j] = int(1e9)
            for t in range(i, j):
                dp[i][j] = min(dp[i][j],
                               dp[i][t] + dp[t + 1][j] + data[i][0] * data[t][1] * data[j][1])

    return dp[0][n-1]


n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solve(data))