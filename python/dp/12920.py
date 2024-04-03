import sys
input = sys.stdin.readline

def solve(n:int,k:int,data:list)->int:
    dp = [0] * (k+1)
    for weight,value,cnt in data:
        t = 1
        while cnt > 0:
            d = min(cnt,t)
            t *= 2
            now_weight = weight * d
            now_value = value * d
            for p in range(k,now_weight-1,-1):
                dp[p] = max(dp[p],dp[p-now_weight] + now_value)
            cnt -= d

    return dp[k]


n,k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
print(solve(n,k,data))