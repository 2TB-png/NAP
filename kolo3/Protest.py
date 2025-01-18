N = int(input())
P = input()

m = 0  # max
c = 0  # current

for i in range(N):
    if P[i] == ".":
        c += 1
    else:
        c = 0

    if c > m:
        m = c

print(m)
