# distutils: language=c++
# cython: boundscheck=False
# cython: wraparound=False
from libcpp.vector cimport vector
from libcpp.deque cimport deque
from cpython.list cimport PyList_GET_ITEM, PyList_GET_SIZE


cdef void mazessolvee( list maze, image):
    cdef int expanse = <int> PyList_GET_SIZE(maze)
    cdef int i = 0
    cdef int j = 0
    cdef int t1 = 0
    cdef int t2 = 0
    cdef vector[(int,int,bint)] forkprocessor
    cdef deque[int] path   
    while not (i == expanse - 1 and j == expanse - 1):
        if <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == -2:
            i = forkprocessor[forkprocessor.size()-1][0]
            j = forkprocessor[forkprocessor.size()-1][1]
            while not (i == path[path.size()-3] and j == path[path.size()-2]):
                path.pop_back()
                path.pop_back()
                path.pop_back()
            if forkprocessor[forkprocessor.size()-1][2]:
                path.pop_back()
                path.push_back(<int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,1)) )
                if <int> PyList_GET_SIZE(<list> ( <object> PyList_GET_ITEM (<list> (<object> PyList_GET_ITEM( maze, i )),j))) == 2:
                    forkprocessor.pop_back()
                else:
                    t1 = forkprocessor[forkprocessor.size()-1][0]
                    t2 = forkprocessor[forkprocessor.size()-1][1]
                    forkprocessor.pop_back()
                    forkprocessor.push_back((t1,t2,False))
                if <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,1))  == 0:
                    i = i - 1
                elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,1))  == 1:
                    i = i + 1
                elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,1))  == 3:
                    j = j + 1
                else:
                    j = j - 1
            else:
                path.pop_back()
                path.push_back(<int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,2)))
                forkprocessor.pop_back()
                if <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,2)) == 0:
                    i = i - 1
                elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,2)) == 1:
                    i = i + 1
                elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,2)) == 3:
                    j = j + 1
                else:
                    j = j - 1
            continue
        if <int> PyList_GET_SIZE(<list> ( <object> PyList_GET_ITEM (<list> (<object> PyList_GET_ITEM( maze, i )),j))) == 1:
            if <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 0:
                i = i - 1
            elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 1:
                i = i + 1
            elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 3:
                j = j + 1
            else:
                j = j - 1
        else:
            path.push_back(i)
            path.push_back(j)
            path.push_back(<int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)))
            forkprocessor.push_back((i,j,True))
            if <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 0:
                i = i - 1
            elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 1:
                i = i + 1
            elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 3:
                j = j + 1
            else:
                j = j - 1
    i = 0
    j = 0
    while not (i==expanse-1 and j==expanse-1):
        image.putpixel((j + j + 1, i + i + 1), (0, 255, 0))
        if <int> PyList_GET_SIZE(<list> ( <object> PyList_GET_ITEM (<list> (<object> PyList_GET_ITEM( maze, i )),j))) == 1:
            if <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 0:
                image.putpixel((j + j + 1, i + i), (0, 255, 0))
                i = i - 1
            elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 1:
                image.putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                i = i + 1
            elif <int> (<object>PyList_GET_ITEM(<list> ( <object> PyList_GET_ITEM( <list> ( <object> PyList_GET_ITEM(maze,i)) ,j )) ,0)) == 3:
                image.putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                j = j + 1
            else:
                image.putpixel((j + j, i + i + 1), (0, 255, 0))
                j = j - 1
        else:
            image.putpixel((j + j + 1, i + i + 1), (0, 255, 0))
            if path[2] == 0:
                image.putpixel((j + j + 1, i + i), (0, 255, 0))
                i = i - 1
            elif path[2] == 1:
                image.putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                i = i + 1
            elif path[2] == 3:
                image.putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                j = j + 1
            else:
                image.putpixel((j + j, i + i + 1), (0, 255, 0))
                j = j - 1
            path.pop_front()
            path.pop_front()
            path.pop_front()

cpdef void mazessolve(r,img):
    mazessolvee(r,img)
