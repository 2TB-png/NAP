N = int(input())

M = 0
S = 0

for i in range(N):
    M_in, S_in = input().split()

    if M_in == "K":
        if S_in == "S":
            M += 1
        if S_in == "P":
            S += 1

    if M_in == "S":
        if S_in == "P":
            M += 1
        if S_in == "K":
            S += 1

    if M_in == "P":
        if S_in == "K":
            M += 1
        if S_in == "S":
            S += 1

if S <= M:
    print("Magda")
else:
    print("Stjepan")
