import sys

def solve(n:int)->list:
    dp = [0] * (n+1)
    pre = [0] * (n+1)
    dp[1] = 1
    pre[1] = 0
    for i in range(2,n+1):
        dp[i] = dp[i-1]
        pre[i] = i-1
        if i % 2 == 0 and dp[i//2] < dp[i]:
            dp[i] = dp[i//2]
            pre[i] = i//2
        if i % 3 == 0 and dp[i//3] < dp[i]:
            dp[i] = dp[i//3]
            pre[i] = i//3
        dp[i] += 1
    result = []
    t = n
    while t > 0:
        result.append(t)

        t = pre[t]
    return [dp[n]-1,result]

n = int(sys.stdin.readline())
answer = solve(n)
print(answer[0])
print(*answer[1])
