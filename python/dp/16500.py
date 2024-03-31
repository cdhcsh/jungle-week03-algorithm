import sys

def solve(target:str,data:list):
    dp = [0] * (len(target)+1)
    dp[0] = 1
    for i in range(1,len(dp)):
        for s in data:
            if i - len(s) >= 0 and target[i-len(s):i] == s and dp[i-len(s)]:
                dp[i] = 1
    return dp[-1]

target = sys.stdin.readline().strip()
data = [sys.stdin.readline().strip() for _ in range(int(sys.stdin.readline()))]
print(solve(target,data))