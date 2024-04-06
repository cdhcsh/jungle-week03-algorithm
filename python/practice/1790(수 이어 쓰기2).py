import sys


def solve(n: int, k: int):
    d = 1
    p = 9
    answer = 0
    while k > d * 9:
        k -= (d * p)
        answer += p
        d += 1
        p *= 10

    answer = (answer+1) + ((k-1) // d)
    if answer > n:
        return -1
    else:
        return str(answer)[(k-1)%d]


n,m = map(int,sys.stdin.readline().split())
print(solve(n,m))