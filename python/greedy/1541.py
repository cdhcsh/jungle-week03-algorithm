import re
import sys

def solve(data:str)->int:
    answer = 0
    flag = True
    l = re.split('([+-])',data)
    for c in l:
        if c == '+' : flag = flag & True
        elif c == '-' : flag = False
        elif flag : answer += int(c)
        else : answer -= int(c)
    return answer


print(solve(sys.stdin.readline().rstrip()))