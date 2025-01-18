N = int(input())

P = list(map(int, list(
    input().split()  # input data
)))

mx, mn = max(P), min(P)  # get graff range

G = [[" " for _1 in range(N+len(str(mx))+1)] for _ in range((mx-mn)//10+1)]


def add_scale(graf, mi_n, ma_x):

    scale = [i for i in range(mi_n, ma_x+10, 10)]
    #  print(scale)
    #  print(mi_n, ma_x)

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


def check_line(last_day, today, index, mi_n):

    last_day_index = last_day//10 - mi_n//10
    today_index = today//10 - mi_n//10

    if today_index == index:
        return True

    if last_day_index > index > today_index:
        return True

    if last_day_index < index < today_index:
        return True

    return False


def doo_graff(graf, period, data, mi_n, ma_x):

    last_day = data[0]

    for day in range(period):
        for index in range(len(graf)):

            if check_line(last_day, data[day], index, mi_n):
                graf[index][day+len(str(ma_x))+1] = "*"
            else:
                graf[index][day+len(str(ma_x))+1] = "."

        last_day = data[day]


add_scale(G, mn, mx)
doo_graff(G, N, P, mn, mx)

for row in range(len(G)):
    print(*G[len(G)-row-1], sep="")
