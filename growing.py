import random
from PIL import Image



def growing(e,p):
    global maze,n
    n = e
    maze = [[[-1] for _ in range(n)] for _ in range(n)]
    stak = []
    stak.append((0,0))
    maze[0][0][0] = -2
    count = 1
    #0 - pure dfs, 100 - pure prims
    n2 = n**2 + 1
    i,j=0,0
    while count!=n2:
        x = []
        if random.random()>p:
            #dfs
            while x==[] and len(stak)>0:
                i,j = stak[-1]
                if i>0 and maze[i-1][j][0]==-1: #In range and unvisited
                    x.append((i-1,j,0))
                if i+1<n and maze[i+1][j][0]==-1:
                    x.append((i+1,j,1))
                if j>0 and maze[i][j-1][0]==-1:
                    x.append((i,j-1,2))
                if j+1<n and maze[i][j+1][0]==-1:
                    x.append((i,j+1,3))
                
                if x==[]:
                    stak.pop()
            if len(stak)==0:
                break
            x = random.choice(x)
            maze[x[0]][x[1]][0] = -2
            if maze[i][j][0]==-2:
                maze[i][j][0] = x[2]
            else:
                maze[i][j].append(x[2]) 
            stak.append((x[0],x[1]))
            count+=1
        else:
            while x==[] and len(stak)>0:
                r = random.randint(0,len(stak)-1)
                i,j = stak[r]
                if i>0 and maze[i-1][j][0]==-1: #In range and unvisited
                    x.append((i-1,j,0))
                if i+1<n and maze[i+1][j][0]==-1:
                    x.append((i+1,j,1))
                if j>0 and maze[i][j-1][0]==-1:
                    x.append((i,j-1,2))
                if j+1<n and maze[i][j+1][0]==-1:
                    x.append((i,j+1,3))
                
                if x==[]:
                    stak.pop(r)
            if len(stak)==0:
                break
            x = random.choice(x)
            maze[x[0]][x[1]][0] = -2
            if maze[i][j][0]==-2:
                maze[i][j][0] = x[2]
            else:
                maze[i][j].append(x[2]) 
            stak.append((x[0],x[1]))
            count+=1
    

    #print(len(stak),'length when my optimization stopped')
    #print(stak)
    




    
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



