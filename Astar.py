import time
from f[1]generator import f[1]generate
from PIL import Image
f = [0,1]
image, f[1] =f[1]generate(20)

def heurestic(a):
    return (len(f[1]) - a[0]) ** 2 + (len(f[1]) - a[1]) ** 2


#First decide where to start
#Then use heurestics again to decide where to go
#Spots doesn't always have to contain forks


# up = 0
# down = 1
# left = 2
# right = 3


spots = [(0, 0)]
tree = {(0, 0): None}
lf = [(0, 0)]
i, j = 0, 0
y = 0
while not (i == len(f[1]) - 1 and j == len(f[1]) - 1):
    minimum = heurestic(spots[0])
    t = spots[0]
    y = 0
    for x in range(len(spots)):
        if heurestic(spots[x]) < minimum:
            minimum = heurestic(spots[x])
            t = spots[x]
            y = x #y can also be used to give the last fork of any spot in spots. if you are at any  spot i,j, and you know its y, you can tell its last fork
    i, j = t
    if len(f[1][i][j]) == 1:
        #spots.remove(t)
        if f[1][i][j][0] == 0:
            i = i - 1
            spots[y] = (i, j)
        elif f[1][i][j][0] == 1:
            i = i + 1
            spots[y] = (i, j)
        elif f[1][i][j][0] == 2:
            j = j - 1
            spots[y] = (i, j)
        elif f[1][i][j][0] == 3:
            j = j + 1
            spots[y] = (i, j)
        else:
            spots.pop(y)
            lf.pop(y)
    elif len(f[1][i][j]) == 2:
        h, k = i, j
        d = lf.pop(y)
        tree[(i, j)] = d
        lf.append((i, j))
        lf.append((i, j))

        if f[1][i][j][0] == 0:
            h = h - 1
        elif f[1][i][j][0] == 1:
            h = h + 1
        elif f[1][i][j][0] == 2:
            k = k - 1
        else:
            k = k + 1

        if f[1][i][j][1] == 0:
            i = i - 1
        elif f[1][i][j][1] == 1:
            i = i + 1
        elif f[1][i][j][1] == 2:
            j = j - 1
        else:
            j = j + 1
        spots.pop(y)
        spots.append((i, j))
        spots.append((h, k))
        if heurestic((h, k)) > heurestic((i, j)):
            pass
        else:
            i, j = h, k
        y = -1
        if i==len(f[1])-1==j:
            print(lf[-1])
            print('This is where the fork the end is supposed to come from')
            print(tree[lf[-1]])
    else:
        h, k = i, j
        g, f = i, j
        d = lf.pop(y)
        tree[(i, j)] = d
        lf.append((i, j))
        lf.append((i, j))
        lf.append((i, j))

        if f[1][i][j][0] == 0:
            h = h - 1
        elif f[1][i][j][0] == 1:
            h = h + 1
        elif f[1][i][j][0] == 2:
            k = k - 1
        else:
            k = k + 1

        if f[1][i][j][1] == 0:
            g = g - 1
        elif f[1][i][j][1] == 1:
            g = g + 1
        elif f[1][i][j][1] == 2:
            f = f - 1
        else:
            f = f + 1

        if f[1][i][j][2] == 0:
            i = i - 1
        elif f[1][i][j][2] == 1:
            i = i + 1
        elif f[1][i][j][2] == 2:
            j = j - 1
        else:
            j = j + 1
        spots.pop(y)
        spots.append((i, j))
        spots.append((h, k))
        spots.append((g, f))
        u = min([(heurestic((i, j)), (i, j)), (heurestic((h, k)), (h, k)), (heurestic((g, f)), (g, f))],
                key=lambda r: r[0])
        i, j = u[1]
        y = -1

path = [lf[y]]
d = tree[lf[y]]
while d != None:
    path.append(d)
    d = tree[d]


def traverse(something):
    #first thing in forks - found by going down first path
    #second thing in forks - found by going down second path
    #and so on
    forks = []
    h, k = something
    red = (h, k)
    g, p = h, k
    if f[1][g][p][0] == 0:
        g = g - 1
    elif f[1][g][p][0] == 1:
        g = g + 1
    elif f[1][g][p][0] == 2:
        p = p - 1
    else:
        p = p + 1

    if f[1][h][k][1] == 0:
        h = h - 1
    elif f[1][h][k][1] == 1:
        h = h + 1
    elif f[1][h][k][1] == 2:
        k = k - 1
    else:
        k = k + 1

    while True:
        if f[1][g][p][0] == -2:
            break
        elif len(f[1][g][p]) > 1:
            break
        elif g == len(f[1]) - 1 == p:
            break
        #print(g,f,'pointer',f[1][g][f])
        if f[1][g][p][0] == 0:
            g = g - 1
        elif f[1][g][p][0] == 1:
            g = g + 1
        elif f[1][g][p][0] == 2:
            p = p - 1
        else:
            p = p + 1
    forks.append((g, p))
    while True:
        if f[1][h][k][0] == -2:
            break
        elif len(f[1][h][k]) > 1:
            break
        elif h == len(f[1]) - 1 == k:
            break
        #print(h,k,'pointer',f[1][h][k])
        if f[1][h][k][0] == 0:
            h = h - 1
        elif f[1][h][k][0] == 1:
            h = h + 1
        elif f[1][h][k][0] == 2:
            k = k - 1
        else:
            k = k + 1
    forks.append((h, k))
    h, k = red
    if len(f[1][h][k]) == 3:
        if f[1][h][k][2] == 0:
            h = h - 1
        elif f[1][h][k][2] == 1:
            h = h + 1
        elif f[1][h][k][2] == 2:
            k = k - 1
        else:
            k = k + 1
        while True:
            if f[1][h][k][0] == -2:
                break
            elif len(f[1][h][k]) > 1:
                break
            elif h == len(f[1]) - 1 == k:
                break
            #print(h,k,'pointer',f[1][h][k])
            if f[1][h][k][0] == 0:
                h = h - 1
            elif f[1][h][k][0] == 1:
                h = h + 1
            elif f[1][h][k][0] == 2:
                k = k - 1
            else:
                k = k + 1
        forks.append((h, k))
    return forks


path = path[::-1]
path = path[1:]
#Now have to reconstruct the actual path
actual = []
for x in range(len(path) - 1):
    d = traverse(path[x])
    t = d.index(path[x + 1])
    actual.append(f[1][path[x][0]][path[x][1]][t])


d = traverse(path[-1])
t = d.index((len(f[1]) - 1, len(f[1]) - 1))
actual.append(f[1][path[-1][0]][path[-1][1]][t])
print(actual)
