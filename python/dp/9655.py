import sys

def solve(n:int)->str:
    if n % 2: return 'SK'
    else : return 'CY'

print(solve(int(sys.stdin.readline())))