# distutils: language=c++
# cython: boundscheck=False
# cython: wraparound=False
from PIL import Image
from libcpp.vector cimport vector
from libcpp.random cimport random_device
from libc.stdlib cimport rand,srand
import numpy as np
cimport numpy as np

np.import_array()
cdef void secure_seed():
    cdef random_device rd
    cdef unsigned int seed = rd()  
    srand(seed)

secure_seed()

cdef vector[vector[vector[int]]] maze
cdef int n = 0

cdef void create_maze(int t):
    global maze
    maze.resize(t)
    cdef vector[vector[int]] row
    cdef vector[int] r
    r.push_back(-1)
    row.assign(t, r)   # Create a row of 't' items, all -1
    maze.assign(t, row) # Assign 't' copies of that row to the maze


cdef void mazegeneratee(int e):
    global n
    n = e
    create_maze(n)
    cdef int i = 0 
    cdef int j = 0 
    cdef vector[int] arr
    cdef int count = 0
    cdef int temp = 0
    cdef bint check = False
    cdef int g = 0
    while count < (n * n):
        if count == (n * n) - 1:
            maze[i][j][0] = -2
            break
        while True:
            arr.clear()
            if j - 1 >= 0:
                if maze[i][j - 1][0] == -1:
                    arr.push_back(2)
            if j + 1 < n:
                if maze[i][j + 1][0] == -1:
                    arr.push_back(3)
            if i + 1 < n:
                if maze[i + 1][j][0] == -1:
                    arr.push_back(1)
            if i - 1 >= 0:
                if maze[i - 1][j][0] == -1:
                    arr.push_back(0)
            if arr.size() == 0:
                if maze[i][j][0] == -1:
                    maze[i][j][0] = -2
                #Backtracking logic
                if j - 1 >= 0:
                    for g in range(0, maze[i][j - 1].size()):
                        if maze[i][j - 1][g] == 3:
                            j = j - 1
                            check = True
                            break
                if check:
                    check = False
                    continue
                if j + 1 < n:
                    for g in range(0, maze[i][j + 1].size()):
                        if maze[i][j + 1][g] == 2:
                            j = j + 1
                            check = True
                            break
                if check:
                    check = False
                    continue
                if i + 1 < n:
                    for g in range(0, maze[i + 1][j].size()):
                        if maze[i + 1][j][g] == 0:
                            i = i + 1
                            check = True
                            break
                if check:
                    check = False
                    continue
                if i - 1 >= 0:
                    for g in range(0, maze[i - 1][j].size()):
                        if maze[i - 1][j][g] == 1:
                            i = i - 1
                            check = True
                            break
                if check:
                    check = False
            else:
                break
        temp = arr[rand() % arr.size()]
        if maze[i][j][0] == -1:
            maze[i][j][0] = temp
        else:
            maze[i][j].push_back(temp)

        if temp == 0:
            i = i - 1
        elif temp == 1:
            i = i + 1
        elif temp == 3:
            j = j + 1
        else:
            j = j - 1
        count = count + 1


cdef img():
    global n
    cdef int size = n*2
    cdef np.ndarray[np.uint8_t, ndim=3] l = np.zeros((size+1, size+1, 3), dtype=np.uint8)
    cdef unsigned char[:, :, :] view = l
    cdef int tj = 0
    cdef int ti = 0
    cdef int g = 0
    cdef int ci = 0
    cdef int cj = 0
    for ci in range(1,size,2):
        tj = 0
        for cj in range(1,size,2):
            view[ci,cj,0] = 255
            view[ci,cj,1] = 255
            view[ci,cj,2] = 255
            for g in range(maze[ti][tj].size()):
                if maze[ti][tj][g] == 0:
                    view[ci-1,cj,0] = 255
                    view[ci-1,cj,1] = 255
                    view[ci-1,cj,2] = 255
                elif maze[ti][tj][g] == 1:
                    view[ci+1,cj,0] = 255
                    view[ci+1,cj,1] = 255
                    view[ci+1,cj,2] = 255
                elif maze[ti][tj][g]==2:
                    view[ci,cj-1,0] = 255
                    view[ci,cj-1,1] = 255
                    view[ci,cj-1,2] = 255
                elif maze[ti][tj][g] == 3:
                    view[ci,cj+1,0] = 255
                    view[ci,cj+1,1] = 255
                    view[ci,cj+1,2] = 255
            tj = tj+1
        ti = ti + 1
    view[1,1,0] = 255
    view[1,1,1] = 0
    view[1,1,2] = 0

    view[size-1,size-1,0] = 0
    view[size-1,size-1,1] = 255
    view[size-1,size-1,2] = 0
    return Image.fromarray(l)

cpdef mazegenerate(p):
    mazegeneratee(p)
    return [img(),maze]

