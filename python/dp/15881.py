import sys

def solve(n:int,data:str)->int:
    answer = 0
    i = 0
    while i < n :
        if data[i:i+4] == 'pPAp':
            answer += 1
            i+=4
        else: i+=1
    return answer


n = int(sys.stdin.readline())
data = sys.stdin.readline().strip()
print(solve(n,data))