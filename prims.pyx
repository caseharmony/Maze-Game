# distutils: language=c++
# cython: boundscheck=False
# cython: wraparound=False
from PIL import Image
from libcpp.vector cimport vector
from libcpp.utility cimport pair
from libcpp.random cimport mt19937
from libcpp.random cimport random_device
import numpy as np
cimport numpy as np

np.import_array()
cdef random_device rd
cdef unsigned int seed = rd()  
cdef mt19937 rng = mt19937(seed)


cdef void create_maze(int t):
    global maze
    maze.resize(t)
    cdef vector[vector[int]] row
    cdef vector[int] r
    r.push_back(-1)
    row.assign(t, r)   # Create a row of 't' items, all -1
    maze.assign(t, row) # Assign 't' copies of that row to the maze


#Need to fix this code
cdef vector[pair[int, int]] removeall(vector[pair[int,int]] x, pair[int,int] ele):
    cdef vector[pair[int,int]] y
    cdef int e
    for e in range(x.size()):
        if x[e] != ele:
            y.push_back(x[e])
    return y


cdef vector[vector[vector[int]]] maze
cdef int n = 0

cdef  vector[pair[int,int]] possible(int i,int j):
    cdef vector[pair[int,int]] u
    if i>0 and maze[i-1][j][0]==-1: #In range and unvisited
        u.push_back(pair[int,int](i-1,j))
    if i+1<n and maze[i+1][j][0]==-1:
        u.push_back(pair[int,int](i+1,j))
    if j>0 and maze[i][j-1][0]==-1:
        u.push_back(pair[int,int](i,j-1))
    if j+1<n and maze[i][j+1][0]==-1:
        u.push_back(pair[int,int](i,j+1))
    return u


cdef (int,int,int) closest(int i,int j):
    cdef vector[(int,int,int)] p
    if i>0 and maze[i-1][j][0]!=-1:
        p.push_back((i-1,j,1))
    if i+1<n and maze[i+1][j][0]!=-1:
        p.push_back((i+1,j,0))
    if j>0 and maze[i][j-1][0]!=-1:
        p.push_back((i,j-1,3))
    if j+1<n and maze[i][j+1][0]!=-1:
        p.push_back((i,j+1,2))
    return p[rng() % p.size()]

cdef void prims(int e):
    global maze,n
    n = e
    create_maze(n)
    cdef vector[pair[int, int]] bb
    #maze = [[[-1] for _ in range(n)] for _ in range(n)]
    #visited = [(0,0)]
    cdef vector[pair[int,int]] options = possible(0,0)
    if rng()%2==0:
        maze[0][0][0] = 3
        maze[0][1][0] = -2
        options = removeall(options,(0,1))
        bb = possible(0,1)
        options.insert(options.end(),bb.begin(),bb.end())
    else:
        maze[0][0][0] = 1
        maze[1][0][0] = -2
        options = removeall(options,(1,0))
        bb = possible(1,0)
        options.insert(options.end(),bb.begin(),bb.end())
    cdef int r
    cdef pair[int, int] t
    cdef (int,int,int) y
    cdef int temp
    while options.size()!=0:
        r = rng() % options.size()
        t = options[r]
        temp = 0
        while temp!=options.size():
            if options[temp]==t:
                options[temp]=options[options.size()-1]
                options.pop_back()
                temp = temp-1
            temp = temp+1
        y = closest(t.first,t.second)
        bb = possible(t.first,t.second)
        options.insert(options.end(),bb.begin(),bb.end())
        maze[t.first][t.second][0] = -2
        if maze[y[0]][y[1]][0]==-2:
            maze[y[0]][y[1]][0] = y[2]
        else:
            maze[y[0]][y[1]].push_back(y[2])


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
    
    
cpdef prim(r):
    prims(r)
    return [img(),maze]



