# distutils: language=c++
# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True
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




cdef void growingg(int e, unsigned int p):
    global maze,n
    n = e
    create_maze(n)
    cdef vector[(int,int,int)] x 
    cdef vector[(int,int)] stak 
    stak.push_back((0,0))
    maze[0][0][0] = -2
    cdef int count = 1
    cdef int i
    cdef int j
    cdef int r
    cdef (int,int,int) g
    #0 - pure dfs, 100 - pure prims
    cdef int n2 = n**2 + 1
    while count!=n2:
        #print(stak)
        x.clear()
        if rng()>p:
            #dfs
            while x.size()==0 and stak.size()>0:
                i,j = stak.back()
                if i>0 and maze[i-1][j][0]==-1: #In range and unvisited
                    x.push_back((i-1,j,0))
                if i+1<n and maze[i+1][j][0]==-1:
                    x.push_back((i+1,j,1))
                if j>0 and maze[i][j-1][0]==-1:
                    x.push_back((i,j-1,2))
                if j+1<n and maze[i][j+1][0]==-1:
                    x.push_back((i,j+1,3))
                
                if x.size()==0:
                    stak.pop_back()
            if stak.size()==0:
                break
            g = x[rng()%x.size()]
            maze[g[0]][g[1]][0] = -2
            if maze[i][j][0]==-2:
                maze[i][j][0] = g[2]
            else:
                maze[i][j].push_back(g[2]) 
            stak.push_back((g[0],g[1]))
            count = count + 1
        else:
            while x.size()==0 and stak.size()>0:
                r = rng() % stak.size()
                i,j = stak[r]
                if i>0 and maze[i-1][j][0]==-1: #In range and unvisited
                    x.push_back((i-1,j,0))
                if i+1<n and maze[i+1][j][0]==-1:
                    x.push_back((i+1,j,1))
                if j>0 and maze[i][j-1][0]==-1:
                    x.push_back((i,j-1,2))
                if j+1<n and maze[i][j+1][0]==-1:
                    x.push_back((i,j+1,3))
                
                if x.size()==0:
                    stak.erase(stak.begin()+r)
            if stak.size()==0:
                break
            g = x[rng()%x.size()]
            maze[g[0]][g[1]][0] = -2
            if maze[i][j][0]==-2:
                maze[i][j][0] = g[2]
            else:
                maze[i][j].push_back(g[2]) 
            stak.push_back((g[0],g[1]))
            count = count + 1
    

    #print(stak.size(),'length when my optimization stopped')
    #print(stak)

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




cpdef cgrowing(r,pe):
    growingg(r,(pe*4294967295)//1)
    return [img(),maze]