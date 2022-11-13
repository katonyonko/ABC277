import io
import sys

_INPUT = """\
6
4 3
2 3 1 4
5 2
3 5 1 4 2
6 6
1 2 3 4 5 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  P=list(map(int,input().split()))
  for i in range(N):
    if P[i]==X: print(i+1)