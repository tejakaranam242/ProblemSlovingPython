from itertools import combinations
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

best = 0
for r in range(1, n+1):
    for combo in combinations(arr, r):
        s = sum(combo)
        if s <= k:
            best = max(best, s)
print(best)