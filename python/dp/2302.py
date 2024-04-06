import sys


def solve(n: int, data: list) -> int:
    prev = 0

    dp = [0] * 41
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2]
    answer = 1
    for s in data:
        answer *= dp[s - prev - 1]
        prev = s
    answer *= dp[n - prev]

    return answer


n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
print(solve(n, data))
