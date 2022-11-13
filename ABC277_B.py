import io
import sys

_INPUT = """\
6
4
H3
DA
D3
SK
5
H3
DA
CK
H3
S7
4
3H
AD
3D
KS
5
00
AA
XX
YY
ZZ
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans='Yes'
  cards=set()
  for i in range(N):
    S=input()
    if S[0] not in 'HDCS' or S[1] not in 'A23456789TJQK': ans='No'
    cards.add(S)
  if len(cards)<N: ans='No'
  print(ans)