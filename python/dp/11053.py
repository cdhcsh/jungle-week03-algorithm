import sys

def solve(data:list)->int:
    dp = [1]*len(data)
    for i in range(1,len(data)):
        for j in range(i):
            if data[j] < data[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
print(solve(data))