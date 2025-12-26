def mazessolve(maze,image):
    i = 0
    j = 0
    forkprocessor = []
    path = []
    coords= []
    while not (i == len(maze) - 1 and j == len(maze) - 1):
        coords.append((i,j))
        if maze[i][j][0] == -2:
            i = forkprocessor[len(forkprocessor) - 3]
            j = forkprocessor[len(forkprocessor) - 2]
            while not (i == path[len(path) - 3] and j == path[
                len(path) - 2]):
                path.pop()
                path.pop()
                path.pop()
            if forkprocessor[len(forkprocessor) - 1]:
                path.pop()
                path.append(maze[i][j][1])
                if len(maze[i][j]) == 2:
                    forkprocessor.pop()
                    forkprocessor.pop()
                    forkprocessor.pop()
                else:
                    forkprocessor[len(forkprocessor) - 1] = False
                if maze[i][j][1] == 0:
                    i = i - 1
                elif maze[i][j][1] == 1:
                    i = i + 1
                elif maze[i][j][1] == 3:
                    j = j + 1
                else:
                    j = j - 1
            else:
                path.pop()
                path.append(maze[i][j][2])
                forkprocessor.pop()
                forkprocessor.pop()
                forkprocessor.pop()
                if maze[i][j][2] == 0:
                    i = i - 1
                elif maze[i][j][2] == 1:
                    i = i + 1
                elif maze[i][j][2] == 3:
                    j = j + 1
                else:
                    j = j - 1
            continue
        if len(maze[i][j]) == 1:
            if maze[i][j][0] == 0:
                i = i - 1
            elif maze[i][j][0] == 1:
                i = i + 1
            elif maze[i][j][0] == 3:
                j = j + 1
            else:
                j = j - 1
        else:
            path.append(i)
            path.append(j)
            path.append(maze[i][j][0])
            forkprocessor.append(i)
            forkprocessor.append(j)
            forkprocessor.append(True)
            if maze[i][j][0] == 0:
                i = i - 1
            elif maze[i][j][0] == 1:
                i = i + 1
            elif maze[i][j][0] == 3:
                j = j + 1
            else:
                j = j - 1
    for i in range(len(path) - 1, -1, -1):
        if not ((i + 1) % 3 == 0):
            path.pop(i)
    i = 0
    j = 0
    while not (i==len(maze)-1 and j==len(maze)-1):
        image.putpixel((j + j + 1, i + i + 1), (0, 255, 0))
        if len(maze[i][j]) == 1:
            if maze[i][j][0] == 0:
                image.putpixel((j + j + 1, i + i), (0, 255, 0))
                i = i - 1
            elif maze[i][j][0] == 1:
                image.putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                i = i + 1
            elif maze[i][j][0] == 3:
                image.putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                j = j + 1
            else:
                image.putpixel((j + j, i + i + 1), (0, 255, 0))
                j = j - 1
        else:
            image.putpixel((j + j + 1, i + i + 1), (0, 255, 0))
            if path[0] == 0:
                image.putpixel((j + j + 1, i + i), (0, 255, 0))
                i = i - 1
            elif path[0] == 1:
                image.putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                i = i + 1
            elif path[0] == 3:
                image.putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                j = j + 1
            else:
                image.putpixel((j + j, i + i + 1), (0, 255, 0))
                j = j - 1
            path.pop(0)
    return image,coords

