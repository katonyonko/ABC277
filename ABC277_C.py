import io
import sys

_INPUT = """\
6
4
1 4
4 3
4 10
8 3
6
1 3
1 5
1 12
3 5
3 12
5 12
3
500000000 600000000
600000000 700000000
700000000 800000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  from collections import deque
  def bfs(G,s):
    global ans
    inf=10**30
    D={k:inf for k in G}
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          ans=max(ans,y)
          dq.append(y)

  ans=1
  N=int(input())
  G=defaultdict(list)
  for i in range(N):
    A,B=map(int,input().split())
    G[A].append(B)
    G[B].append(A)
  bfs(G,1)
  print(ans)