import io
import sys

_INPUT = """\
6
9 7
3 0 2 5 5 3 0 6 3
1 10
4
20 20
18 16 15 9 8 8 17 1 3 17 11 9 12 11 7 3 2 14 3 12
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  d=defaultdict(int)
  ans=0
  for i in range(N):
    d[A[i]%M]+=A[i]
  checked={key:False for key in d}
  for key in d:
    if checked[key]==True: continue
    tmp=0
    k=key
    while (k-1)%M in d and (k-1)%M!=key: k=(k-1)%M
    if (k-1)%M==key:
      ans=sum(A)
      break
    while k in d:
      tmp+=d[k]
      checked[k]=True
      k=(k+1)%M
    ans=max(ans,tmp)
  print(sum(A)-ans)