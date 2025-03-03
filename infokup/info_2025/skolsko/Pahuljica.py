x_l = [0, 0, 0, 0, 0, 0, 0]
y_l = [0, 0, 0, 0, 0, 0, 0]

# input points
for i in range(7):
    x_l[i], y_l[i] = tuple(map(int, input().split()))

# make a backup
org_x_l = x_l.copy()
org_y_l = y_l.copy()

# calculate borders
x_min, x_max = min(x_l), max(x_l)
y_min, y_max = min(y_l), max(y_l)


if not abs(x_min - x_max) == abs(y_min - y_max):
    # delite your problems :)
    if not x_l.count(x_max)-1:
        x_l.remove(x_max)
    if not x_l.count(x_min)-1:
        x_l.remove(x_min)

    if not y_l.count(y_max)-1:
        y_l.remove(y_max)
    if not y_l.count(y_min)-1:
        y_l.remove(y_min)

    x_min, x_max = min(x_l), max(x_l)
    y_min, y_max = min(y_l), max(y_l)

# calculate origins
origen = [(x_min+x_max)//2, (y_min+y_max)//2]

# restore points
x_l = org_x_l.copy()
y_l = org_y_l.copy()

# transform origen to 0,0
# print(origen[0], origen[1], origen)
# print(x_l, y_l)
for i in range(7):
    x_l[i] -= origen[0]
for i in range(7):
    y_l[i] -= origen[1]
# print(x_l, y_l)

# delite your problems, agen :)
find = []
for point in range(7):
    if [-x_l[point], -y_l[point]] in find:
        find.remove([-x_l[point], -y_l[point]])
    else:
        find.append([x_l[point], y_l[point]])

# exit
# print(find)
print(-find[0][0]+origen[0], -find[0][1]+origen[1])
# print(origen)
