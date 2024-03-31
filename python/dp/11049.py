import sys

input = sys.stdin.readline


def solve(data: list[list]) -> int:
    n = len(data)
    if n == 1: return 0

    for d in data:
        d.append(0)

    def _multi(m1: list, m2: list) -> list:
        result = [0, 0, 0]
        result[2] = m1[2] + m1[0] * m1[1] * m2[1]
        result[0] = m1[0]
        result[1] = m2[1]
        return result

    dp = [[] for _ in range(n + 1)]
    dp[1] = data[0]
    dp[2] = _multi(data[0], data[1])
    print(dp[1])
    print(dp[2])
    for i in range(3, n + 1):
        print(i)

        # print(f'dp[{i-2}] * (data[{i-1}]) * (data[{i-0}]) = ',end='')
        # print(_multi(dp[i - 2], _multi(data[(i - 1) - 1], data[(i - 1)])))
        # print(dp[i - 2],'*',_multi(data[(i - 1) - 1], data[(i - 1)]))
        # print(f'dp[{i-1}] * (data[{i-0}]) = ',end='')
        # print(_multi(dp[i-1],data[(i-1)]))
        dp[i] = min(_multi(dp[i - 2], _multi(data[(i - 1) - 1], data[(i - 1)]))
                    ,_multi(dp[i-1],data[(i-1)]),
                    _multi(_multi(dp[i-1],data[(i-1)-1]),data[(i-1)]),

                    key=lambda l: l[2])
        [print(k,d) for k,d in enumerate(dp)]

    return dp[-1][2]


data = [list(map(int, input().split())) for _ in range(int(input()))]
print(solve(data))
