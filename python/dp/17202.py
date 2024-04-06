import sys


def solve(s1: list, s2: list) -> list:
    n = len(s1)
    table = [[(i+j)%10 for j in range(10)] for i in range(10)]
    dp = [0] * (2*n)
    for i in range(0,len(dp),2):
        dp[i] = s1[i//2]
        dp[i+1] = s2[i//2]
    for m in range(1, len(dp) - 1):
        for i in range(len(dp)- m):
            dp[i] = table[dp[i]][dp[i+1]]
    return dp[:2]

s1 = list(map(int,list(sys.stdin.readline().strip())))
s2 = list(map(int,list(sys.stdin.readline().strip())))
print(*solve(s1,s2),sep='')
