import random
from PIL import Image
def mazegenerate(n):
    maze = [[[-1] for _ in range(n)] for _ in range(n)]
    i = 0 
    j = 0 
    arr = []
    count = 0
    temp = 0
    while count < (n * n):
        if count == (n * n) - 1:
            maze[i][j][0] = -2
            break
        while True:
            arr = []
            if j - 1 >= 0:
                if maze[i][j - 1][0] == -1:
                    arr.append(2)
            if j + 1 < n:
                if maze[i][j + 1][0] == -1:
                    arr.append(3)
            if i + 1 < n:
                if maze[i + 1][j][0] == -1:
                    arr.append(1)
            if i - 1 >= 0:
                if maze[i - 1][j][0] == -1:
                    arr.append(0)
            if len(arr) == 0:
                if maze[i][j][0] == -1:
                    maze[i][j][0] = -2
                try:
                    if j - 1 >= 0:
                        for g in range(0, len(maze[i][j - 1])):
                            if maze[i][j - 1][g] == 3:
                                j = j - 1
                                raise Exception("")
                    if j + 1 < len(maze[i]):
                        for g in range(0, len(maze[i][j + 1])):
                            if maze[i][j + 1][g] == 2:
                                j = j + 1
                                raise Exception("")
                    if i + 1 < len(maze):
                        for g in range(0, len(maze[i + 1][j])):
                            if maze[i + 1][j][g] == 0:
                                i = i + 1
                                raise Exception("")
                    if i - 1 >= 0:
                        for g in range(0, len(maze[i - 1][j])):
                            if maze[i - 1][j][g] == 1:
                                i = i - 1
                                raise Exception("")
                except Exception:
                    pass
            else:
                break
        temp = arr[random.randint(0, len(arr) - 1)]
        if maze[i][j][0] == -1:
            maze[i][j][0] = temp
        else:
            maze[i][j].append(temp)

        if temp == 0:
            i = i - 1
        elif temp == 1:
            i = i + 1
        elif temp == 3:
            j = j + 1
        else:
            j = j - 1
        count = count + 1
    n = n * 2
    image = Image.new('RGB', (n + 1, n + 1), color=(0, 0, 0))
    i = 0
    j = 0
    for ci in range(1, n, 2):
        j = 0
        for cj in range(1, n, 2):
            image.putpixel((cj, ci), (255, 255, 255))
            for g in range(len(maze[i][j])):
                if maze[i][j][g] == 0:
                    image.putpixel((cj, ci - 1), (255, 255, 255))
                elif maze[i][j][g] == 1:
                    image.putpixel((cj, ci + 1), (255, 255, 255))
                elif maze[i][j][g] == 2:
                    image.putpixel((cj - 1, ci), (255, 255, 255))
                elif maze[i][j][g] == 3:
                    image.putpixel((cj + 1, ci), (255, 255, 255))
            j = j + 1
        i = i + 1
    image.putpixel((n - 1, n - 1), (0, 255, 0))
    image.putpixel((1, 1), (255, 0, 0))
    return [image, maze]