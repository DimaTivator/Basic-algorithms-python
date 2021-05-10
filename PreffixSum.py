a = list(map(int, input().split()))
pref = [sum(a[: i + 1]) for i in range(len(a))]
print(*pref)
