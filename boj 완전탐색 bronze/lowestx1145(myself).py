# 5개 입력중 적어도 3개로 나누어 떨어지는 가장 작은수 => 최소공배수 combination (list , 3) -> 가장 작은거
from itertools import combinations
import sys
import math   # math.gcd  최대공약수, math.lcm 최소공배수
lis = map(int, sys.stdin.readline().split())
combi_lis= list(combinations(lis,3))
min_multi=50000

for a in combi_lis:
    if min_multi> math.lcm(a[0],a[1],a[2]):
        min_multi=math.lcm(a[0],a[1],a[2])

print(min_multi)
