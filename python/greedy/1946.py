import sys


def solve(data: list) -> list:
    result = []

    for mans in data:
        answer = 1
        mans.sort()
        pre = mans[0][1]
        for i in range(1, len(mans)):
            if pre > mans[i][1]:
                answer += 1
                pre = mans[i][1]

        result.append(answer)

    return result


data = []
for _ in range(int(sys.stdin.readline())):
    data.append([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))])
print(*(solve(data)), sep='\n')
