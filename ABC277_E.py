import io
import sys

_INPUT = """\
6
5 5 2
1 3 0
2 3 1
5 4 1
2 1 1
1 4 0
3 4
4 4 2
4 3 0
1 2 1
1 2 0
2 1 1
2 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def bfs01(G,s):
    inf=10**20
    dist = [inf]*len(G)
    dist[s] = 0
    que = deque()
    que.append(s)
    while que:
      i = que.popleft()
      for j, c in G[i]:
          d = dist[i] + c
          if d < dist[j]:
              dist[j] = d
              if c == 1:
                  que.append(j)
              else:
                  que.appendleft(j)
    return dist

  N,M,K=map(int,input().split())
  G=[[] for _ in range(2*N)]
  for i in range(M):
    u,v,a=map(int,input().split())
    u-=1; v-=1
    if a==0:
      G[u+N].append((v+N,1))
      G[v+N].append((u+N,1))
    else:
      G[u].append((v,1))
      G[v].append((u,1))
  S=list(map(lambda x: int(x)-1, input().split()))
  for i in range(K):
    G[S[i]].append((S[i]+N,0))
    G[S[i]+N].append((S[i],0))
  D=bfs01(G,0)
  ans=min(D[N-1],D[2*N-1])
  if ans==10**20: print(-1)
  else: print(ans)