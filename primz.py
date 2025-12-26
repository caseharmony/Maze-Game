import random
from PIL import Image

def removeall(x,ele):
    y = []
    for i in x:
        if i != ele:
            y.append(i)
    return y


maze = []
n = 0

def possible(i,j):
    x = []
    if i>0 and maze[i-1][j][0]==-1: #In range and unvisited
        x.append((i-1,j))
    if i+1<n and maze[i+1][j][0]==-1:
        x.append((i+1,j))
    if j>0 and maze[i][j-1][0]==-1:
        x.append((i,j-1))
    if j+1<n and maze[i][j+1][0]==-1:
        x.append((i,j+1))
    #print(x,'possible from ',i,j)
    #display()
    return x

def closest(i,j):
    x = []
    if i>0 and maze[i-1][j][0]!=-1:
        x.append((i-1,j,1))
    if i+1<n and maze[i+1][j][0]!=-1:
        x.append((i+1,j,0))
    if j>0 and maze[i][j-1][0]!=-1:
        x.append((i,j-1,3))
    if j+1<n and maze[i][j+1][0]!=-1:
        x.append((i,j+1,2))
    return random.choice(x)

def prim(e):
    global maze,n
    n = e
    maze = [[[-1] for _ in range(n)] for _ in range(n)]
    #visited = [(0,0)]
    options = possible(0,0)
    if random.randint(0,1)==0:
        maze[0][0][0] = 3
        maze[0][1][0] = -2
        options.remove((0,1))
        options.extend(possible(0,1))
    else:
        maze[0][0][0] = 1
        maze[1][0][0] = -2
        options.remove((1,0))
        options.extend(possible(1,0))
    while len(options)!=0:
        r = random.randint(0,len(options)-1)
        t = options[r]
        options = removeall(options,options[r])
        y = closest(t[0],t[1])
        options.extend(possible(t[0],t[1]))
        maze[t[0]][t[1]][0] = -2
        if maze[y[0]][y[1]][0]==-2:
            maze[y[0]][y[1]][0] = y[2]
        else:
            maze[y[0]][y[1]].append(y[2])
    n = n * 2
    image = Image.new('RGB', (n + 1, n + 1), color=(0, 0, 0))
    ti = 0
    tj = 0
    for ci in range(1, n, 2):
        tj = 0
        for cj in range(1, n, 2):
            image.putpixel((cj, ci), (255, 255, 255))
            for g in range(len(maze[ti][tj])):
                if maze[ti][tj][g] == 0:
                    image.putpixel((cj, ci - 1), (255, 255, 255))
                elif maze[ti][tj][g] == 1:
                    image.putpixel((cj, ci + 1), (255, 255, 255))
                elif maze[ti][tj][g] == 2:
                    image.putpixel((cj - 1, ci), (255, 255, 255))
                elif maze[ti][tj][g] == 3:
                    image.putpixel((cj + 1, ci), (255, 255, 255))
            tj = tj + 1
        ti = ti + 1
    image.putpixel((1,1),(255,0,0))
    image.putpixel((n-1,n-1),(0,255,0))
    return [image,maze]



