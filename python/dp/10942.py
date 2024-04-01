import sys

def solve(data:list,command:list)->list:
    n = len(data)
    dp = [[0] * (n) for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
        if i+1 < n:
            dp[i+1][i] = 1
    for r in range(1,n):
        for i in range(n-r):
            j = i + r
            dp[i][j] = int(dp[i+1][j-1] and data[i] == data[j])
    return  list(map(lambda l : dp[l[0]-1][l[1]-1],command))

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
command = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
print(*solve(data,command),sep='\n')

