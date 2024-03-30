import sys


def solve(s1: str, s2: str) -> str:
    n,m = len(s1),len(s2)
    dp = [[''] * (m + 1) for _ in range(n + 1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + s1[i-1]
            else :
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],key=lambda x:len(x))
    return dp[n][m]


s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
answer = solve(s1,s2)
print(len(answer),answer,sep='\n')
