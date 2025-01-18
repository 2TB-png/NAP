N = int(input())

P = list(map(int, list(
    input().split()  # input data
)))

mx, mn = max(P), min(P)  # get graff range

G = [[" " for _1 in range(N+len(str(mx))+1)] for _ in range((mx-mn)//10+1)]


def add_scale(graf, mi_n, ma_x):

    scale = [mx-i for i in range(mi_n, ma_x+10, 10)]
    # print(scale)

    dig_len = len(str(ma_x))

    for i in range(len(graf)):
        graf[i][dig_len] = "|"

        graf[i][dig_len-1] = 0

        #  add numbers
        if scale[i] > 9:
            graf[i][dig_len-2] = str(scale[i])[-2]

        if scale[i] > 99:
            graf[i][dig_len-3] = str(scale[i])[-3]

        if scale[i] > 999:
            graf[i][dig_len-4] = str(scale[i])[-4]


add_scale(G, mn, mx)

for row in G:
    print(*row, sep="")
