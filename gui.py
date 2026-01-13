from dfs import mazegenerate
from primz import prim
from bruteforce import mazessolve
from sendemail import otp
from login import login,signup,savefile,importsave,exportsave
import customtkinter as tk
from tkinter import filedialog
from PIL import Image
from pygame import mixer as mk
import pywinstyles
import os

def traverse(something):
    global f
    forks = []
    o, p = something
    red = (o, p)
    q, r = o, p
    if f[1][q][r][0] == 0:
        q = q - 1
    elif f[1][q][r][0] == 1:
        q = q + 1
    elif f[1][q][r][0] == 2:
        r = r - 1
    else:
        r = r + 1
    try:
        if f[1][o][p][1] == 0:
            o = o - 1
        elif f[1][o][p][1] == 1:
            o = o + 1
        elif f[1][o][p][1] == 2:
            p = p - 1
        else:
            p = p + 1
    except IndexError:
        pass
    while True:
        if f[1][q][r][0] == -2:
            break
        elif len(f[1][q][r]) > 1:
            break
        elif q == len(f[1]) - 1 == r:
            break
        if f[1][q][r][0] == 0:
            q = q - 1
        elif f[1][q][r][0] == 1:
            q = q + 1
        elif f[1][q][r][0] == 2:
            r = r - 1
        else:
            r = r + 1
    forks.append((q, r))
    while True:
        if f[1][o][p][0] == -2:
            break
        elif len(f[1][o][p]) > 1:
            break
        elif o == len(f[1]) - 1 == p:
            break
        if f[1][o][p][0] == 0:
            o = o - 1
        elif f[1][o][p][0] == 1:
            o = o + 1
        elif f[1][o][p][0] == 2:
            p = p - 1
        else:
            p = p + 1
    forks.append((o, p))
    o, p = red
    if len(f[1][o][p]) == 3:
        if f[1][o][p][2] == 0:
            o = o - 1
        elif f[1][o][p][2] == 1:
            o = o + 1
        elif f[1][o][p][2] == 2:
            p = p - 1
        else:
            p = p + 1
        while True:
            if f[1][o][p][0] == -2:
                break
            elif len(f[1][o][p]) > 1:
                break
            elif o == len(f[1]) - 1 == p:
                break
            if f[1][o][p][0] == 0:
                o = o - 1
            elif f[1][o][p][0] == 1:
                o = o + 1
            elif f[1][o][p][0] == 2:
                p = p - 1
            else:
                p = p + 1
        forks.append((o, p))
    return forks

def heurestic(a):
    return (len(f[1]) - a[0]) ** 2 + (len(f[1]) - a[1]) ** 2

def realtimeastar():
    global f
    spots=[(0,0)]
    tree={(0,0): (0,0)}
    lf=[(0,0)]
    i1,j1=0,0
    y1=0
    while not (i1==len(f[1]) - 1 and j1==len(f[1]) - 1):
        placeimg()
        win.update()
        win.update_idletasks()
        minimum=heurestic(spots[0])
        t=spots[0]
        y1=0
        for x1 in range(len(spots)):
            if heurestic(spots[x1]) < minimum:
                minimum=heurestic(spots[x1])
                t=spots[x1]
                y1=x1
        i1,j1=t
        f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
        if len(f[1][i1][j1])==1:
            if f[1][i1][j1][0]==0:
                f[0].putpixel((j1 + j1 + 1,i1 + i1),(0,255,0))
                i1=i1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
                spots[y1]=(i1,j1)
            elif f[1][i1][j1][0]==1:
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 2),(0,255,0))
                i1=i1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
                spots[y1]=(i1,j1)
            elif f[1][i1][j1][0]==2:
                f[0].putpixel((j1 + j1,i1 + i1 + 1),(0,255,0))
                j1=j1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
                spots[y1]=(i1,j1)
            elif f[1][i1][j1][0]==3:
                f[0].putpixel((j1 + j1 + 2,i1 + i1 + 1),(0,255,0))
                j1=j1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
                spots[y1]=(i1,j1)
            else:
                spots.pop(y1)
                lf.pop(y1)
        elif len(f[1][i1][j1])==2:
            l,m=i1,j1
            d=lf.pop(y1)
            tree[(i1,j1)]=d
            lf.append((i1,j1))
            lf.append((i1,j1))
            if f[1][i1][j1][0]==0:
                f[0].putpixel((m + m + 1, l + l), (0, 255, 0))
                l= l - 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            elif f[1][i1][j1][0]==1:
                f[0].putpixel((m + m + 1, l + l + 2), (0, 255, 0))
                l= l + 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            elif f[1][i1][j1][0]==2:
                f[0].putpixel((m + m, l + l + 1), (0, 255, 0))
                m=m - 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            else:
                f[0].putpixel((m + m + 2, l + l + 1), (0, 255, 0))
                m=m + 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            if f[1][i1][j1][1]==0:
                f[0].putpixel((j1 + j1 + 1,i1 + i1 ),(0,255,0))
                i1=i1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1 ),(0,255,0))
            elif f[1][i1][j1][1]==1:
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 2 ),(0,255,0))
                i1=i1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1 ),(0,255,0))
            elif f[1][i1][j1][1]==2:
                f[0].putpixel((j1 + j1,i1 + i1 + 1 ),(0,255,0))
                j1=j1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1 ),(0,255,0))
            else:
                f[0].putpixel((j1 + j1 + 2,i1 + i1 + 1 ),(0,255,0))
                j1=j1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1 ),(0,255,0))
            spots.pop(y1)
            spots.append((i1,j1))
            spots.append((l, m))
            if heurestic((l, m)) > heurestic((i1, j1)):
                pass
            else:
                i1,j1=l,m
            y1=-1
        else:
            l,m=i1,j1
            g,p=i1,j1
            d=lf.pop(y1)
            tree[(i1,j1)]=d
            lf.append((i1,j1))
            lf.append((i1,j1))
            lf.append((i1,j1))
            if f[1][i1][j1][0]==0:
                f[0].putpixel((m + m + 1, l + l), (0, 255, 0))
                l= l - 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            elif f[1][i1][j1][0]==1:
                f[0].putpixel((m + m + 1, l + l + 2), (0, 255, 0))
                l= l + 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            elif f[1][i1][j1][0]==2:
                f[0].putpixel((m + m, l + l + 1), (0, 255, 0))
                m=m - 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            else:
                f[0].putpixel((m + m + 2, l + l + 1), (0, 255, 0))
                m=m + 1
                f[0].putpixel((m + m + 1, l + l + 1), (0, 255, 0))
            if f[1][i1][j1][1]==0:
                f[0].putpixel((p + p + 1,g + g),(0,255,0))
                g=g - 1
                f[0].putpixel((p + p + 1,g + g + 1),(0,255,0))
            elif f[1][i1][j1][1]==1:
                f[0].putpixel((p + p + 1,g + g + 2),(0,255,0))
                g=g + 1
                f[0].putpixel((p + p + 1,g + g + 1),(0,255,0))
            elif f[1][i1][j1][1]==2:
                f[0].putpixel((p + p,g + g + 1),(0,255,0))
                p=p - 1
                f[0].putpixel((p + p + 1,g + g + 1),(0,255,0))
            else:
                f[0].putpixel((p + p + 2,g + g + 1),(0,255,0))
                p=p + 1
                f[0].putpixel((p + p + 1,g + g + 1),(0,255,0))
            if f[1][i1][j1][2]==0:
                f[0].putpixel((j1 + j1 + 1,i1 + i1),(0,255,0))
                i1=i1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
            elif f[1][i1][j1][2]==1:
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 2),(0,255,0))
                i1=i1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
            elif f[1][i1][j1][2]==2:
                f[0].putpixel((j1 + j1,i1 + i1 + 1),(0,255,0))
                j1=j1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
            else:
                f[0].putpixel((j1 + j1 + 2,i1 + i1 + 1),(0,255,0))
                j1=j1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(0,255,0))
            spots.pop(y1)
            spots.append((i1,j1))
            spots.append((l, m))
            spots.append((g,p))
            u=min([(heurestic((i1,j1)),(i1,j1)), (heurestic((l, m)), (l, m)), (heurestic((g, p)), (g, p))],
                  key=lambda r: r[0])
            i1,j1=u[1]
            y1=-1
    path=[lf[y1]]
    d=tree[lf[y1]]
    while True:
        path.append(d)
        if d == tree[d]:
            if len(f[1][0][0])>1:
                path.append(d)
            break
        d=tree[d]
    path=path[::-1]
    path=path[1:]
    actual=[]
    for x1 in range(len(path) - 1):
        d=traverse(path[x1])
        t=d.index(path[x1 + 1])
        actual.append(f[1][path[x1][0]][path[x1][1]][t])
    d=traverse(path[-1])
    t=d.index((len(f[1]) - 1,len(f[1]) - 1))
    actual.append(f[1][path[-1][0]][path[-1][1]][t])
    for i1 in range(1,n*2+1):
        for j1 in range(1,n*2+1):
            d=f[0].getpixel((i1,j1))
            if d==(0,255,0):
                f[0].putpixel((i1,j1),(255,255,255))
    i1=0
    j1=0
    while not (i1==len(f[1])-1 and j1==len(f[1])-1):
        f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
        if len(f[1][i1][j1])==1:
            if f[1][i1][j1][0]==0:
                f[0].putpixel((j1 + j1 + 1,i1 + i1),(255,0,0))
                i1=i1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            elif f[1][i1][j1][0]==1:
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 2),(255,0,0))
                i1=i1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            elif f[1][i1][j1][0]==3:
                f[0].putpixel((j1 + j1 + 2,i1 + i1 + 1),(255,0,0))
                j1=j1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            else:
                f[0].putpixel((j1 + j1,i1 + i1 + 1),(255,0,0))
                j1=j1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
        else:
            f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            if actual[0]==0:
                f[0].putpixel((j1 + j1 + 1,i1 + i1),(255,0,0))
                i1=i1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            elif actual[0]==1:
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 2),(255,0,0))
                i1=i1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            elif actual[0]==3:
                f[0].putpixel((j1 + j1 + 2,i1 + i1 + 1),(255,0,0))
                j1=j1 + 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            else:
                f[0].putpixel((j1 + j1,i1 + i1 + 1),(255,0,0))
                j1=j1 - 1
                f[0].putpixel((j1 + j1 + 1,i1 + i1 + 1),(255,0,0))
            actual.pop(0)
    for i1 in range(1,n*2+1):
        for j1 in range(1,n*2+1):
            d=f[0].getpixel((i1,j1))
            if d==(0,255,0) or d==(50,50,50):
                f[0].putpixel((i1,j1),(255,255,255))
    placeimg()
    win.update()
    win.update_idletasks()

def realtimebruteforce():
    i=0
    j=0
    forkprocessor=[]
    path=[]
    f[0].putpixel((1,1),(0,255,0))
    while not (i==len(f[1]) - 1 and j==len(f[1]) - 1):
        if f[1][i][j][0]==-2:
            i=forkprocessor[- 3]
            j=forkprocessor[- 2]
            f[0].putpixel((2*j+1,2*i+1),(50,50,50))
            while not (i==path[-3] and j==path[- 2]):
                path.pop()
                path.pop()
                path.pop()
            if forkprocessor[- 1]:
                path.pop()
                path.append(f[1][i][j][1])
                if len(f[1][i][j])==2:
                    forkprocessor.pop()
                    forkprocessor.pop()
                    forkprocessor.pop()
                else:
                    forkprocessor[- 1]=False
                if f[1][i][j][1]==0:
                    f[0].putpixel((2*j+1,2*i),(0,255,0))
                    i=i - 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
                elif f[1][i][j][1]==1:
                    f[0].putpixel((2*j+1,2*i+2),(0,255,0))
                    i=i + 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
                elif f[1][i][j][1]==3:
                    f[0].putpixel((2*j+2,2*i+1),(0,255,0))
                    j=j + 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
                else:
                    f[0].putpixel((2*j,2*i+1),(0,255,0))
                    j=j - 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            else:
                path.pop()
                path.append(f[1][i][j][2])
                forkprocessor.pop()
                forkprocessor.pop()
                forkprocessor.pop()
                if f[1][i][j][2]==0:
                    i=i - 1
                elif f[1][i][j][2]==1:
                    i=i + 1
                elif f[1][i][j][2]==3:
                    j=j + 1
                else:
                    j=j - 1
            continue
        if len(f[1][i][j])==1:
            if f[1][i][j][0]==0:
                f[0].putpixel((2*j+1,2*i),(0,255,0))
                i=i - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0]==1:
                f[0].putpixel((2*j+1,2*i+2),(0,255,0))
                i=i + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0]==3:
                f[0].putpixel((2*j+2,2*i+1),(0,255,0))
                j=j + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            else:
                f[0].putpixel((2*j,2*i+1),(0,255,0))
                j=j - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
        else:
            path.append(i)      
            path.append(j)
            path.append(f[1][i][j][0])
            forkprocessor.append(i)
            forkprocessor.append(j)
            forkprocessor.append(True)
            if f[1][i][j][0]==0:
                f[0].putpixel((2*j+1,2*i),(0,255,0))
                i=i - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0]==1:
                f[0].putpixel((2*j+1,2*i+2),(0,255,0))
                i=i + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0]==3:
                f[0].putpixel((2*j+2,2*i+1),(0,255,0))
                j=j + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            else:
                f[0].putpixel((2*j,2*i+1),(0,255,0))
                j=j - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
        placeimg()
        win.update()
        win.update_idletasks()
    for i in range(len(path) - 1,-1,-1):
        if not ((i + 1) % 3==0):
            path.pop(i)
    i=0
    j=0
    while not (i==len(f[1])-1 and j==len(f[1])-1):
        f[0].putpixel((j + j + 1,i + i + 1),(255,0,0))
        if len(f[1][i][j])==1:
            if f[1][i][j][0]==0:
                f[0].putpixel((j + j + 1,i + i),(255,0,0))
                i=i - 1
            elif f[1][i][j][0]==1:
                f[0].putpixel((j + j + 1,i + i + 2),(255,0,0))
                i=i + 1
            elif f[1][i][j][0]==3:
                f[0].putpixel((j + j + 2,i + i + 1),(255,0,0))
                j=j + 1
            else:
                f[0].putpixel((j + j,i + i + 1),(255,0,0))
                j=j - 1
        else:
            f[0].putpixel((j + j + 1,i + i + 1),(255,0,0))
            if path[0]==0:
                f[0].putpixel((j + j + 1,i + i),(255,0,0))
                i=i - 1
            elif path[0]==1:
                f[0].putpixel((j + j + 1,i + i + 2),(255,0,0))
                i=i + 1
            elif path[0]==3:
                f[0].putpixel((j + j + 2,i + i + 1),(255,0,0))
                j=j + 1
            else:
                f[0].putpixel((j + j,i + i + 1),(255,0,0))
                j=j - 1
            path.pop(0)
    for i in range(1,n*2+1):
        for j in range(1,n*2+1):
            d=f[0].getpixel((i,j))
            if d==(0,255,0) or d==(50,50,50):
                f[0].putpixel((i,j),(255,255,255))
    f[0].putpixel((n * 2 - 1,n * 2 - 1),(255,0,0))
    placeimg()
    win.update()
    win.update_idletasks()

def lockmaze():
    global lock,emazesize
    lock=True
    emazesize.configure(state='normal')
    
def resizeimage(event):
    global h,w,lmazepicl
    w=event.width
    h=event.height
    if w / h > 1:
        w=h
    else:
        h=w
    h,w=h-h//20,w-w//20
    if h <=0 or w <=0:
        h,w=1,1
    lmazepic.configure(size=(h,w))
    lmazepicl.configure(image=lmazepic)

def zoomimg():
    global x,y,f,ezoom
    try:
        zoomsize=int(ezoom.get())+1
    except:
        zoomsize=31
    imgw,imgh=f[0].size
    left=max(0,x - zoomsize)
    top=max(0,y - zoomsize)
    right=min(imgw,left + (zoomsize*2))
    bottom=min(imgh,top + (zoomsize*2))
    if right==imgw:
        left=max(0,imgw - (zoomsize*2))
    if bottom==imgh:
        top=max(0,imgh - (zoomsize*2))
    return f[0].crop((left,top,right,bottom))

def placeimg():
    global lmazepic,lmazepicl
    if zoommode.get()=='on':
        lmazepic=tk.CTkImage(dark_image=zoomimg().resize((1080,1080),Image.NEAREST),size=(h,w))
    else:
        lmazepic=tk.CTkImage(dark_image=f[0].resize((1080,1080),Image.NONE),size=(h,w))
    lmazepicl.configure(image=lmazepic)
    
def reset():
    fmazegame.grid_forget()
    win.focus_set()
    fwinnerbox.grid_forget()
    ftimer.grid_forget()
    lock=True

def realtimesolver():
    if f==[]:
        messagebox("Generate Maze First")
        return
    global zoommode
    if lock:
        return
    lockmaze()
    x=zoommode
    zoommode=tk.StringVar(value="off")
    if sbsolvealg.get()=='AStar':
        realtimeastar()
    else:
        realtimebruteforce()
    zoommode=x

def solvemaze():
    global zoommode
    if f==[]:
        messagebox("Generate Maze First")
        return
    f[0]=f[3].copy()
    x=zoommode
    zoommode=tk.StringVar(value="off")
    placeimg()
    zoommode=x
    lockmaze()

def genm():
    reset()
    pmazegame()
    global f,n,x,y,emazesize,lock,bgenmaze,moves
    moves=[]
    bgenmaze.configure(state="disabled")
    if emazesize.get()=='':
        emazesize.insert(0,'30')
    ltimer.configure(text='00:00:00')
    tt=ltimer.cget("text")
    lock=False
    x,y=1,1
    try:
        n=int(emazesize.get())
    except:
        emazesize.insert(0,'30')
        n=30
    if sbmazealg.get()=='DFS':
        f=mazegenerate(n)
    else:
        f=prim(n)
    f.append(f[0].copy())
    f.append(mazessolve(f[1],f[0]))
    f[0]=f[2].copy()
    global lmazepic
    lmazepicl.grid(row=0,column=0,padx=10,pady=10)
    placeimg()
    ptimer()
    def check():
        if tt==ltimer.cget("text"):
            timer()
    win.after(1000,check)
    win.after(1000,lambda: bgenmaze.configure(state="normal"))
    emazesize.configure(state="readonly")

def left(event):
    if lock:
        return
    global x,emazesize,moves
    x=x - 1
    r,g,b=f[0].getpixel((x,y))
    if x==n * 2 - 1 and y==n * 2 - 1:
        pwinnerbox()
        lockmaze()
        return
    if r==0 and g==0 and b==0:
        x=x + 1
        return
    if g==255:
        f[0].putpixel((x,y),(255,0,0))
    else:
        f[0].putpixel((x + 1,y),(255,255,255))
    moves.append('l')
    c1.play(mk.Sound(os.path.dirname(__file__)+"\\move.wav"))
    placeimg()

def right(event):
    if lock:
        return
    global x,emazesize,moves
    x=x + 1
    r,g,b=f[0].getpixel((x,y))
    if x==n * 2 - 1 and y==n * 2 - 1:
        pwinnerbox()
        lockmaze()
        return
    if r==0 and g==0 and b==0:
        x=x - 1
        return
    if g==255:
        f[0].putpixel((x,y),(255,0,0))
    else:
        f[0].putpixel((x - 1,y),(255,255,255))
    moves.append('r')
    c1.play(mk.Sound(os.path.dirname(__file__)+"\\move.wav"))
    placeimg()

def up(event):
    if lock:
        return
    global y,emazesize,moves
    y=y - 1
    if x==n * 2 - 1 and y==n * 2 - 1:
        pwinnerbox()
        lockmaze()
        return
    r,g,b=f[0].getpixel((x,y))
    if r==0 and g==0 and b==0:
        y=y + 1
        return
    if g==255:
        f[0].putpixel((x,y),(255,0,0))
    else:
        f[0].putpixel((x,y + 1),(255,255,255))
    moves.append('u')
    c1.play(mk.Sound(os.path.dirname(__file__)+"\\move.wav"))
    placeimg()

def down(event):
    if lock:
        return
    global y,emazesize,moves
    y=y + 1
    if x==n * 2 - 1 and y==n * 2 - 1:
        pwinnerbox()
        lockmaze()
        return
    r,g,b=f[0].getpixel((x,y))
    if r==0 and g==0 and b==0:
        y=y - 1
        return
    if g==255:
        f[0].putpixel((x,y),(255,0,0))
    else:
        f[0].putpixel((x,y - 1),(255,255,255))
    moves.append('d')
    c1.play(mk.Sound(os.path.dirname(__file__)+"\\move.wav"))
    placeimg()

def replay():
    global x,y,emazesize,f,lock,breplay
    breplay.configure(state="readonly")
    tt=ltimer.cget("text")
    if f==[]:
        breplay.configure(state="normal")
        messagebox("Generate Maze First")
        return
    if moves==[]:
        breplay.configure(state="normal")
        return
    fmazegame.lift()
    lock=True
    f[0]=f[2].copy()
    x,y=1,1
    for i in moves:
        ox,oy=x,y
        if i=='l': x-=1
        elif i=='r': x+=1
        elif i=='u': y-=1
        elif i=='d': y+=1
        c=f[0].getpixel((x,y))
        if c[2]==255:
            f[0].putpixel((x,y),(255,0,0))
        else:
            f[0].putpixel((ox, oy), (255,255,255))
        placeimg()
        win.update()
        win.after(10)
    lock=False
    def check():
        if tt==ltimer.cget("text"):
            timer()
    win.after(1000,check)
    breplay.configure(state="normal")

def clear():
    if lock:
        return
    if f==[]:
        messagebox("Generate Maze First")
        return
    global x,y,moves
    x,y,moves,f[0]=1,1,[],f[2].copy()
    placeimg()
    
#AUDIO AND TIMER FUNCTIONS

def music():
    if musicmode.get()=='on':
        c0.play(mk.Sound(os.path.dirname(__file__)+"\\"+vsong.get()+".mp3"),loops=-1)
    else:
        c0.stop()

def sfx():
    if sfxmode.get()=='on':
        c1.set_volume(slsfxvol.get())
    else:
        c1.set_volume(0.0)

def timer():
    if not lock:
        time=ltimer.cget("text")
        h,m,s=map(int,time.split(':'))
        s+=1
        if s==60:
            s=0
            m+=1
        if m==60:
            m=0
            h+=1
        time=f"{h:02d}:{m:02d}:{s:02d}"
        ltimer.configure(text=time)
        win.after(1000, timer)
    
#LOGIN AND SIGNUP PAGES LAYOUTS AND FUNCTIONS

def pname():
    global flogin
    flogin.grid_forget()
    fname.grid(row=0,column=0,padx=20,pady=20,columnspan=2,rowspan=5)
    llogo=tk.CTkLabel(fname,image=ilogo,text="")
    llogo.grid(row=0,column=0,padx=10,pady=10,sticky="n",columnspan=2)
    efirstname.grid(row=2,column=0,padx=20,pady=10,columnspan=2)
    elastname.grid(row=3,column=0,padx=20,pady=10,columnspan=2)
    bnext1.grid(row=4,column=0,columnspan=6,padx=20,pady=10,sticky="ew")

def sendemail():
    global otpcode,femail
    otpcode=str(otp(eemail.get()))
    femail.grid_forget()
    potp()

def pemail():
    global fname
    fname.grid_forget()
    femail.grid(row=0,column=0,padx=20,pady=20)
    llogo=tk.CTkLabel(femail,image=ilogo,text="")
    llogo.grid(row=0,column=0,padx=10,pady=10,sticky="n",columnspan=2)
    lemail.grid(row=1,column=0,padx=20,pady=10,columnspan=2,sticky="ew")
    eemail.grid(row=2,column=0,padx=20,pady=10,columnspan=2,sticky="ew")
    bnext2.grid(row=3,column=0,padx=20,pady=10,columnspan=2,sticky="ew")

def nextbox(event,currententry,nextentry):
    if event.keysym=="BackSpace":
        return
    while len(currententry.get()) > 1:
        currententry.delete(1)
    if len(currententry.get())==1:
        nextentry.focus_set()

def prevbox(event,currententry,previousentry):
    currententry.delete(0)
    if len(currententry.get())==0:
        previousentry.focus_set()

def checkotp():
    global fotp
    eotp=str(eotp1.get() + eotp2.get() + eotp3.get() + eotp4.get() + eotp5.get() + eotp6.get())
    if eotp==otpcode:
        messagebox("OTP Verified")
        fotp.grid_forget()
        ppassword()
    else:
        messagebox("Invalid OTP")

def potp():
    global otpcode,femail
    femail.grid_forget()
    fotp.grid(row=0,column=0,padx=20,pady=20,columnspan=10,rowspan=6)
    llogo=tk.CTkLabel(fotp,image=ilogo,text="")
    llogo.grid(row=0,column=0,padx=10,pady=10,sticky="n",columnspan=10)
    eotp1.grid(row=1,column=1,padx=10,pady=10,sticky="ew")
    eotp2.grid(row=1,column=2,padx=10,pady=10,sticky="ew")
    eotp3.grid(row=1,column=3,padx=10,pady=10,sticky="ew")
    eotp4.grid(row=1,column=4,padx=10,pady=10,sticky="ew")
    eotp5.grid(row=1,column=5,padx=10,pady=10,sticky="ew")
    eotp6.grid(row=1,column=6,padx=10,pady=10,sticky="ew")
    bback3.grid(row=2,column=1,columnspan=3,padx=10,pady=10,sticky="ew")
    bnext3.grid(row=2,column=4,columnspan=3,padx=10,pady=10,sticky="ew")

def ppassword():
    global fotp
    fotp.grid_forget()
    fpassword.grid(row=0,column=0,padx=20,pady=20)
    llogo=tk.CTkLabel(fpassword,image=ilogo,text="")
    llogo.grid(row=0,column=0,padx=10,pady=10,sticky="n",columnspan=10)
    ecreatepassword.grid(row=2,column=0,padx=20,pady=10,columnspan=2)
    econfirmpassword.grid(row=3,column=0,padx=20,pady=10,columnspan=2)
    bnext4.grid(row=11,column=0,columnspan=6,padx=10,pady=10,sticky="ew")

def dpassword():
    password=ecreatepassword.get()
    confirmpassword=econfirmpassword.get()
    cont=True
    if password !=confirmpassword:
        lmatch.grid(row=4,column=0,padx=10,pady=0,columnspan=6,sticky="w")
        cont=False
    else:
        try:
            lmatch.grid_forget()
        except:
            pass
    if len(password) <8:
        lminchar.grid(row=5,column=0,padx=10,pady=0,columnspan=6,sticky="w")
        cont=False
    else:
        try:
            lminchar.grid_forget()
        except:
            pass
    if any(i.isspace() for i in password):
        lspace.grid(row=6,column=0,padx=10,pady=0,columnspan=6,sticky="w")
        cont=False
    else:
        try:
            lspace.grid_forget()
        except:
            pass    
    if not any(i.islower() for i in password):
        llowercase.grid(row=7,column=0,padx=10,pady=0,columnspan=6,sticky="w")
        cont=False
    else:
        try:
            llowercase.grid_forget()
        except:
            pass
    if not any(i.isupper() for i in password):
        luppercase.grid(row=8,column=0,padx=10,pady=0,columnspan=6,sticky="w")
        cont=False
    else:
        try:
            luppercase.grid_forget()
        except:
            pass
    if not any(i.isdigit() for i in password):
        lnumber.grid(row=9,column=0,padx=10,pady=0,columnspan=6,sticky="w")
        cont=False
    else:
        try:
            lnumber.grid_forget()
        except:
            pass
    if password.isalnum():
        lspecialchar.grid(row=10,column=0,padx=10,pady=0,columnspan=6,sticky="w") 
        cont=False
    else:
        try:
            lspecialchar.grid_forget()
        except:
            pass
    if cont:
        pgamertag()

def pgamertag():
    global fpassword
    fpassword.grid_forget()
    fgamertag.grid(row=0,column=0,padx=20,pady=20)
    llogo=tk.CTkLabel(fgamertag,image=ilogo,text="")
    llogo.grid(row=0,column=0,padx=10,pady=10,sticky="n",columnspan=10)
    ecreateusername.grid(row=1,column=0,padx=20,pady=10,columnspan=2)
    bnext5.grid(row=2,column=0,columnspan=6,padx=10,pady=10,sticky="ew")

def dsignup():
    global efirstname,elastname,ecreatepassword,ecreateusername,eemail,fgamertag,account
    username=ecreateusername.get()
    password=ecreatepassword.get()
    firstname=efirstname.get()
    lastname=elastname.get()
    email=eemail.get()
    if signup(username,password,firstname,lastname,email):
        fgamertag.grid_forget()
        pmazecontrols()
        account=ecreateusername
        ecreateusername.delete(0,tk.END)
        ecreatepassword.delete(0,tk.END)
        econfirmpassword.delete(0,tk.END)
        efirstname.delete(0,tk.END)
        elastname.delete(0,tk.END)
        eemail.delete(0,tk.END)
    else:
        messagebox("Username already exists. Please choose a different username.")

def dlogin():
    global eusername,epassword,account
    username=eusername.get()
    password=epassword.get()
    if login(username,password):
        global flogin
        flogin.grid_forget() 
        messagebox("Successfully logged in")
        pmazecontrols()
        account=username
        eusername.delete(0,tk.END)
        epassword.delete(0,tk.END)
    else:
        messagebox("Invalid username or password")

def plogin():
    llogo=tk.CTkLabel(flogin,image=ilogo,text="")
    flogin.grid(row=0,column=0,padx=20,pady=20,columnspan=2,rowspan=5)
    llogo.grid(row=0,column=0,padx=10,pady=10,sticky="n",columnspan=2)
    llogintxt.grid(row=1,column=0,padx=20,pady=10,columnspan=2,sticky="n")
    eusername.grid(row=2,column=0,padx=20,pady=10,columnspan=2)
    epassword.grid(row=3,column=0,padx=20,pady=10,columnspan=2)
    blogin.grid(row=4,column=0,padx=20,pady=10,columnspan=2,sticky="ew")
    bsignup.grid(row=5,column=0,padx=7,pady=3,columnspan=2,sticky="w")

def logout():
    global fmazecontrols,fsettings,emazesize,lock,fmazegame,fwinnerbox,account
    fmazegame.grid_forget()
    fwinnerbox.grid_forget()
    fmazecontrols.grid_forget()
    fsettings.grid_forget()
    account="defaultacc"
    plogin()
    try:
        reset()
    except:
        pass

#OTHER PAGES LAYOUTS

def pmazegame():
    fmazegame.grid(row=0,column=0,padx=20,pady=20,columnspan=10,rowspan=15,sticky="nsew")
    fmazegame.grid_columnconfigure(0,weight=1)
    fmazegame.lift()

def pmazecontrols():
    fmazecontrols.grid(row=0,column=11,padx=20,pady=20,columnspan=10,rowspan=9,sticky="nsew")
    lsettings.grid(row=0,column=20,padx=20,pady=20,columnspan=1,rowspan=1,sticky="ne")
    lcontrolstxt.grid(row=0,column=11,padx=20,pady=10,columnspan=10,sticky="w")
    lgentxt.grid(row=1,column=11,padx=20,pady=10,columnspan=6,sticky="w")
    emazesize.grid(row=2,column=11,padx=20,pady=10,columnspan=10,sticky="ew")
    bgenmaze.grid(row=3,column=11,padx=20,pady=10,columnspan=10,sticky="ew")
    bclear.grid(row=4,column=11,padx=20,pady=10,columnspan=10,sticky="ew")
    lalgtxt.grid(row=5,column=11,padx=20,pady=10,columnspan=6,sticky="w")
    bsolamaze.grid(row=6,column=11,padx=20,pady=10,columnspan=5,sticky="w")
    bsolsmaze.grid(row=6,column=16,padx=20,pady=10,columnspan=5,sticky="e")
    breplay.grid(row=7,column=11,padx=20,pady=10,columnspan=10,sticky="ew")
    lsavefiletxt.grid(row=8,column=11,padx=20,pady=10,columnspan=6,sticky="w")
    bfilesave.grid(row=9,column=11,padx=20,pady=10,columnspan=10,sticky="ew")
    bsaveimg.grid(row=10,column=11,padx=20,pady=10,columnspan=10,sticky="ew")
    sbimgno.grid(row=11,column=11,padx=20,pady=10,columnspan=10,sticky="ew")
    fsettings.grid(row=0,column=11,padx=20,pady=(100,20),columnspan=10,rowspan=10,sticky="ne")
    psettings()
    fmazecontrols.lift()
    pwinnerboxload()

def ptimer():
    ftimer.grid(row=10,column=11,padx=20,pady=10,columnspan=10,sticky="nsew")
    ltime.grid(row=10,column=11,padx=10,pady=(10,0),sticky='w')
    ltimer.grid(row=11,column=11,padx=20,pady=(0,10),columnspan=10,sticky="ew")

def psettings():
    limgtypetxt.grid(row=0,column=11,padx=20,pady=0,columnspan=5,sticky="w")
    sbimgtype.grid(row=0,column=16,padx=20,pady=10,columnspan=5,sticky="w")
    lmazealg.grid(row=1,column=11,padx=20,pady=0,columnspan=5,sticky="w")
    sbmazealg.grid(row=1,column=16,padx=20,pady=10,columnspan=5,sticky="w")
    lsolvealg.grid(row=2,column=11,padx=20,pady=0,columnspan=5,sticky="w")
    sbsolvealg.grid(row=2,column=16,padx=20,pady=10,columnspan=5,sticky="w")
    lsong.grid(row=4,column=11,padx=20,pady=10,columnspan=5,sticky="w")
    osong.grid(row=4,column=16,padx=20,pady=10,columnspan=5,sticky="w")
    smusic.grid(row=5,column=11,padx=20,pady=10,columnspan=5,sticky="w")
    slmusvol.grid(row=5,column=16,padx=20,pady=10,columnspan=5,sticky="w")
    ssfx.grid(row=6,column=11,padx=20,pady=10,columnspan=5,sticky="w")
    slsfxvol.grid(row=6,column=16,padx=20,pady=10,columnspan=5,sticky="w")
    szoom.grid(row=7,column=11,padx=20,pady=10,columnspan=5,sticky="w")
    ezoom.grid(row=7,column=16,padx=20,pady=10,columnspan=5,sticky="w")
    blogout.grid(row=8,column=11,padx=20,pady=10,columnspan=10,sticky="ew")

def pfilemanager():
    global ffilemanager
    ffilemanager=tk.CTkFrame(master=win,corner_radius=20)
    lfilemanager=tk.CTkLabel(ffilemanager,text="File Manager:",font=tk.CTkFont(size=30,weight="bold"))
    lsave=tk.CTkLabel(ffilemanager,text="Save file:",font=tk.CTkFont(size=20,weight="bold"))
    global euploadname
    euploadname=tk.CTkEntry(ffilemanager,placeholder_text="file name",corner_radius=30,width=325)
    bsavelocal=tk.CTkButton(ffilemanager,corner_radius=30,text="download",width=155,command=savelocal)
    bsavecloud=tk.CTkButton(ffilemanager,corner_radius=30,text="save to cloud",width=155,command=savecloud)
    lgetcloud=tk.CTkLabel(ffilemanager,text="Get File From Cloud:",font=tk.CTkFont(size=20,weight="bold"))
    global vgetcloud
    vgetcloud=tk.StringVar()
    ogetcloud=tk.CTkOptionMenu(ffilemanager,values=savefile(account),width=155,variable=vgetcloud)
    bgetcloud=tk.CTkButton(ffilemanager,corner_radius=100,text="load save",width=155,command=opencloud)
    lgetlocal=tk.CTkLabel(ffilemanager,text="open save file from your drive:",font=tk.CTkFont(size=20,weight="bold"))
    bgetlocal=tk.CTkButton(ffilemanager,corner_radius=30,text="Open File",width=325,command=openlocal)
    bclosefilemanager=tk.CTkButton(ffilemanager,corner_radius=30,text="Close",width=155,command=lambda: ffilemanager.grid_forget())

    ffilemanager.grid(row=0,column=11,padx=20,pady=20,rowspan=10,columnspan=21,sticky="nsew")
    lfilemanager.grid(row=0,column=11,columnspan=10,padx=20,pady=20,sticky="nw")
    lsave.grid(row=1,column=11,columnspan=10,padx=20,pady=(20,5),sticky="w")
    euploadname.grid(row=2,column=11,columnspan=10,padx=20,pady=10,sticky="ew")
    bsavelocal.grid(row=3,column=11,columnspan=5,padx=20,pady=10,sticky="ew")
    bsavecloud.grid(row=3,column=16,columnspan=5,padx=20,pady=10,sticky="ew")
    lgetcloud.grid(row=4,column=11,columnspan=10,padx=20,pady=(20,5),sticky="w")
    ogetcloud.grid(row=5,column=11,columnspan=5,padx=20,pady=10,sticky="ew")
    bgetcloud.grid(row=5,column=16,columnspan=5,padx=20,pady=10,sticky="ew")
    lgetlocal.grid(row=6,column=11,columnspan=10,padx=20,pady=(20,5),sticky="w")
    bgetlocal.grid(row=7,column=11,columnspan=10,padx=20,pady=10,sticky="ew")
    bclosefilemanager.grid(row=8,column=16,padx=20,pady=(120,10),sticky="sew")

def pwinnerboxload():
    lwin.grid(row=0,column=0,padx=20,pady=20)
    ltrophy.grid(row=1,column=0,padx=0,pady=20)
    trophyupdate(0)

def pwinnerbox():
    fwinnerbox.grid(row=0,column=0,padx=20,pady=20)
    fwinnerbox.lift()
    c1.play(mk.Sound(os.path.dirname(__file__)+"\\victory.wav"))

def trophyupdate(frame):
    ltrophy.configure(image=trophyframes[frame])
    nextindex=(frame + 1) % len(trophyframes)
    win.after(duration,trophyupdate,nextindex)

#SAVE FILE FUNCTIONS

def makefile(maze,moves,time):
    file=str(maze)+"||||"+str(moves)+"||||"+time
    return file

def breakfile(file):
    global f,n,x,y,lock,lmazepic,ffilemanager,moves
    maze,moves,time=file.split("||||")
    maze=eval(maze)
    moves=eval(moves)
    n=(len(maze)*2)
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
    n=int(n/2)
    f=[image,maze]
    reset()
    pmazegame()
    bgenmaze.configure(state="disabled")
    if not lock:
        ltimer.configure(text='00:00:-1')
    else:
        ltimer.configure(text='00:00:00')
    lock=False
    x,y=1,1
    f.append(f[0].copy())
    f.append(mazessolve(f[1],f[0]))
    f[0]=f[2].copy()
    lmazepicl.grid(row=0,column=0,padx=10,pady=10)
    ffilemanager.grid_forget()
    replay()
    ltimer.configure(text=time)
    win.after(1000,lambda: bgenmaze.configure(state="normal"))
    emazesize.configure(state="readonly")

def savelocal():
    if f==[]:
        messagebox("Generate Maze First")
        return
    file=makefile(f[1],moves,ltimer.cget("text"))
    try:
        path=filedialog.asksaveasfilename(initialdir="/",title="Save File As",initialfile=euploadname.get(),defaultextension=".maze")
        if not path:
            return
        with open(path, "w") as txt:
            txt.write(file)
        messagebox(f"File successfully saved to:\n{path}")
    except:
        pass

def openlocal():
    try:
        with open(filedialog.askopenfilename(title="Select a File",initialdir="/",filetypes=(("maze files", "*.maze"),("All files", "*.*"))), 'r') as txt:
            file = txt.read()
        breakfile(file)
    except:
        pass

def savecloud():
    if f==[]:
        messagebox("Generate Maze First")
        return
    file=makefile(f[1],moves,ltimer.cget("text"))
    if exportsave(account, euploadname.get(), file):
        messagebox("File successfully saved to Cloud")
    else:
        messagebox("A File of The Given Name Already Exists\nSelect a Different Name")

def opencloud():
    file=importsave(account,vgetcloud.get())
    breakfile(file)

#SAVE IMAGE FUNCTION

def saveimg():
    if f==[]:
        messagebox("Generate Maze First")
        return
    imgno=sbimgno.get()
    if imgno=='Current':
        imgno=0
    elif imgno=='Unsolved':
        imgno=2
    else:
        imgno=3
    try:
        f[imgno].resize((1080,1080),Image.NONE).save(filedialog.asksaveasfilename(initialdir="/",title="Save File As",initialfile="output",defaultextension=sbimgtype.get()))
    except:
        pass

#MESSAGE BOX
   
def messagebox(text):
    wait=tk.IntVar(value=0)
    win.grid_rowconfigure(0,weight=1)
    win.grid_columnconfigure(0,weight=1)
    fmsgbox=tk.CTkFrame(master=win,corner_radius=20,bg_color="#000001",border_width=1.75)
    c1.play(mk.Sound(os.path.dirname(__file__)+"\\message.wav"))
    fmsgbox.grid(row=0,column=0,padx=20,pady=20,sticky="")
    pywinstyles.set_opacity(fmsgbox,color="#000001")
    lmsg=tk.CTkLabel(fmsgbox,text=text,font=tk.CTkFont(size=15,weight="bold"))
    lmsg.grid(row=0,column=0,padx=40,pady=(40,20))
    def ok():
        fmsgbox.grid_forget()
        wait.set(1)
    bmsgok=tk.CTkButton(fmsgbox,corner_radius=30,text="OK",command=ok)
    bmsgok.grid(row=1,column=0,padx=20,pady=(0,20))
    win.wait_variable(wait)

#MAIN WINDOW SETUP

moves,account,lock,n,x,y,f,h,w=[],"defaultacc",True,0,1,1,[],1,1
mk.pre_init(44100, -16, 2, 2048)
mk.init()
mk.set_num_channels(2)
c0=mk.Channel(0)
c1=mk.Channel(1)
win=tk.CTk()
win.title("Maze Game")
win.iconbitmap(os.path.dirname(__file__)+"\\icon.ico")
win.geometry(str(win.winfo_screenwidth()) + "x" + str(win.winfo_screenheight()))
tk.set_window_scaling(0.6)
tk.set_appearance_mode("dark")
tk.set_default_color_theme(os.path.dirname(__file__)+"\\orange.json") 
win.grid_columnconfigure(0,weight=1)
win.grid_rowconfigure(0,weight=1)

#LOGIN PAGE SETUP

flogin=tk.CTkFrame(master=win,corner_radius=20)
llogintxt=tk.CTkLabel(flogin,text="Log in OR Sign Up",font=tk.CTkFont(size=20,weight="bold"))
eusername=tk.CTkEntry(flogin,placeholder_text="Enter Username",width=325,corner_radius=30)
epassword=tk.CTkEntry(flogin,placeholder_text="Enter password",width=325,corner_radius=30,show='*')
bsignup=tk.CTkButton(flogin,corner_radius=30,fg_color='transparent',hover=False,text="don't have an account?",text_color="#67C1FD",command=pname)
blogin=tk.CTkButton(flogin,corner_radius=30,text="login",command=dlogin)
ilogo=tk.CTkImage(dark_image=Image.open(os.path.dirname(__file__)+"\\icon.png"),size=(300,300))

#MAZE WINDOW SETUP

fmazegame=tk.CTkFrame(master=win,corner_radius=20)
lmazepic=None
lmazepicl=tk.CTkLabel(fmazegame,image=lmazepic,text="")
lmazegametxt=tk.CTkLabel(fmazegame,text="Maze Game",font=tk.CTkFont(size=30,weight="bold"))
progressbar=tk.CTkProgressBar(fmazegame,orientation="horizontal",mode="indeterminate")

#MAZE CONTROLS SETUP

fmazecontrols=tk.CTkFrame(master=win,corner_radius=20,width=350)
lcontrolstxt=tk.CTkLabel(fmazecontrols,text="Controls:",font=tk.CTkFont(size=30,weight="bold"))
lgentxt=tk.CTkLabel(fmazecontrols,text="Configure and Generate:",font=tk.CTkFont(size=20,weight="bold"))
emazesize=tk.CTkEntry(fmazecontrols,placeholder_text="Enter Maze Size(1-x)",width=325,corner_radius=30)
bgenmaze=tk.CTkButton(fmazecontrols,corner_radius=30,text="generate maze",command=genm)
bclear=tk.CTkButton(fmazecontrols,corner_radius=30,text="clear",command=clear)
lalgtxt=tk.CTkLabel(fmazecontrols,text="Algoritmic solving:",font=tk.CTkFont(size=20,weight="bold"))
bsolamaze=tk.CTkButton(fmazecontrols,corner_radius=30,text="Solve fast",command=solvemaze,width=155)
bsolsmaze=tk.CTkButton(fmazecontrols,corner_radius=30,text="see the program",command=realtimesolver,width=155)
breplay=tk.CTkButton(fmazecontrols,corner_radius=30,text="replay your moves",command=replay,width=325)
lsavefiletxt=tk.CTkLabel(fmazecontrols,text="Saving and Exporting:",font=tk.CTkFont(size=20,weight="bold"))
bsaveimg=tk.CTkButton(fmazecontrols,corner_radius=30,text="export maze to image",command=saveimg)
sbimgno=tk.CTkSegmentedButton(fmazecontrols,values=["Current","Unsolved","Solved"],corner_radius=30)
sbimgno.set("Unsolved")
bfilesave=tk.CTkButton(fmazecontrols,corner_radius=30,text="Open File Manager",command=pfilemanager,width=155)
win.bind("<Left>",left)
win.bind("<Right>",right)
win.bind("<Up>",up)
win.bind("<Down>",down)

ftimer=tk.CTkFrame(master=win,corner_radius=20)
ltime=tk.CTkLabel(ftimer,text="Your Time:",font=tk.CTkFont(size=15,weight="bold"))
ltimer=tk.CTkLabel(ftimer,text="00:00:00",font=tk.CTkFont(size=90,weight="bold"))

#SETTINGS PAGE SETUP

isettings=tk.CTkImage(dark_image=Image.open(os.path.dirname(__file__)+"\\settings.png"),size=(50,50))
fsettings=tk.CTkFrame(master=win,corner_radius=20,width=300,bg_color="#000001",fg_color="#363636")
pywinstyles.set_opacity(fsettings,color="#000001")
lsettings=tk.CTkLabel(fmazecontrols,image=isettings,text="")
def focussettings(event):
    fsettings.lift()
    fsettings.focus_set()
lsettings.bind("<Enter>",lambda event: focussettings(event))
def lift():
    fmazecontrols.lift()
def checkhover():
    mouse_x=fsettings.winfo_pointerx() - fsettings.winfo_rootx()
    mouse_y=fsettings.winfo_pointery() - fsettings.winfo_rooty()
    return (0 <=mouse_x <=fsettings.winfo_width() and 0 <=mouse_y <=fsettings.winfo_height())
def leftsettings(event):
    win.after(100,verify)
def verify():
    if not checkhover():
        lift()
lsettings.bind("<Leave>",leftsettings)
fsettings.bind("<Leave>",leftsettings)
movemode=tk.StringVar(value="off")
musicmode=tk.StringVar(value="on")
sfxmode=tk.StringVar(value="on")
zoommode=tk.StringVar(value="on")
limgtypetxt=tk.CTkLabel(fsettings,text="Select Image Type:",font=tk.CTkFont(size=12))
sbimgtype=tk.CTkSegmentedButton(fsettings,values=[".jpg",".png",".webp"],corner_radius=30)
sbimgtype.set(".png")
lmazealg=tk.CTkLabel(fsettings,text="Select Maze Generator:",font=tk.CTkFont(size=12))
sbmazealg=tk.CTkSegmentedButton(fsettings,values=["Primz","DFS"],corner_radius=30)
sbmazealg.set("Primz")
lsolvealg=tk.CTkLabel(fsettings,text="Select Maze Solver:",font=tk.CTkFont(size=12))
sbsolvealg=tk.CTkSegmentedButton(fsettings,values=["AStar","Brute Force"],corner_radius=30)
sbsolvealg.set("AStar")
lsong=tk.CTkLabel(fsettings,text="Select Song:",font=tk.CTkFont(size=12))
vsong=tk.StringVar()
vsong.set("m23")
osong=tk.CTkOptionMenu(fsettings,values=["m22","m23","m24","m25","m26"],width=155,variable=vsong,command=lambda choice: music())
smusic=tk.CTkSwitch(fsettings,text="background music",variable=musicmode,command=music,onvalue="on",offvalue="off")
ssfx=tk.CTkSwitch(fsettings,text="sound effects",variable=sfxmode,command=sfx,onvalue="on",offvalue="off")
slmusvol=tk.CTkSlider(fsettings,from_=0,to=1,width=165,command=c0.set_volume,number_of_steps=100)
slmusvol.set(1)
slsfxvol=tk.CTkSlider(fsettings,from_=0,to=1,width=165,command=c1.set_volume,number_of_steps=100)
slsfxvol.set(1)
szoom=tk.CTkSwitch(fsettings,text="Zoom",variable=zoommode,onvalue="on",offvalue="off")
ezoom=tk.CTkEntry(fsettings,placeholder_text="Zoom Size",width=90,corner_radius=30)
blogout=tk.CTkButton(fsettings,corner_radius=30,text="Logout",command=logout)

#WINNER BOX SETUP

fwinnerbox=tk.CTkFrame(master=win,corner_radius=20,bg_color="#000001",fg_color="#414141")
pywinstyles.set_opacity(fwinnerbox,color="#000001")
lwin=tk.CTkLabel(fwinnerbox,text="¡ ¡ Congratulations on Completing the Maze ! !",font=tk.CTkFont(size=15,weight="bold"))
itrophy=Image.open(os.path.dirname(__file__)+"\\trophy.gif")
trophyframes=[]
for i in range(itrophy.n_frames):
    itrophy.seek(i)
    trophyframes.append(tk.CTkImage(light_image=itrophy.copy(),size=(250,250)))
duration=itrophy.info.get("duration",100)
ltrophy=tk.CTkLabel(fwinnerbox,text="",image=trophyframes[0])

#SIGNUP PAGES SETUP

fmazegame.bind("<Configure>",resizeimage)
bsignup.bind("<Enter>",lambda event: bsignup.cget("font").configure(underline=True))
bsignup.bind("<Leave>",lambda event: bsignup.cget("font").configure(underline=False))

fname=tk.CTkFrame(master=win,corner_radius=20)
efirstname=tk.CTkEntry(fname,placeholder_text="Enter your first name",width=325,corner_radius=30)
elastname=tk.CTkEntry(fname,placeholder_text="Enter your last name",width=325,corner_radius=30)
bnext1=tk.CTkButton(master=fname,text="Next",corner_radius=20,command=lambda: pemail() if efirstname.get() !="" and elastname.get() !="" else messagebox("Please fill in all fields"))

femail=tk.CTkFrame(master=win,corner_radius=20)
lemail=tk.CTkLabel(master=femail,text="Enter your email adress",font=tk.CTkFont(size=20,weight="bold"))
eemail=tk.CTkEntry(master=femail,placeholder_text="Enter your email",width=325,border_width=2,corner_radius=30)
bnext2=tk.CTkButton(master=femail,text="Next",corner_radius=20,command=lambda: sendemail() if eemail.get() !="" and "@" in eemail.get() else messagebox("Please enter your email adress"))

fotp=tk.CTkFrame(master=win,corner_radius=20)
eotp1=tk.CTkEntry(master=fotp,placeholder_text="x",width=40,height=60,border_width=2,corner_radius=10,justify='center',font=tk.CTkFont(size=24))
eotp2=tk.CTkEntry(master=fotp,placeholder_text="x",width=40,height=60,border_width=2,corner_radius=10,justify='center',font=tk.CTkFont(size=24))
eotp3=tk.CTkEntry(master=fotp,placeholder_text="x",width=40,height=60,border_width=2,corner_radius=10,justify='center',font=tk.CTkFont(size=24))
eotp4=tk.CTkEntry(master=fotp,placeholder_text="x",width=40,height=60,border_width=2,corner_radius=10,justify='center',font=tk.CTkFont(size=24))
eotp5=tk.CTkEntry(master=fotp,placeholder_text="x",width=40,height=60,border_width=2,corner_radius=10,justify='center',font=tk.CTkFont(size=24))
eotp6=tk.CTkEntry(master=fotp,placeholder_text="x",width=40,height=60,border_width=2,corner_radius=10,justify='center',font=tk.CTkFont(size=24))
bnext3=tk.CTkButton(master=fotp,text="Next",corner_radius=20,command=checkotp)
bback3=tk.CTkButton(master=fotp,text="Back",corner_radius=20,command=lambda: (pemail(),fotp.grid_forget()))

eotp1.bind("<KeyRelease>",lambda event: nextbox(event,eotp1,eotp2))
eotp2.bind("<KeyRelease>",lambda event: nextbox(event,eotp2,eotp3))
eotp3.bind("<KeyRelease>",lambda event: nextbox(event,eotp3,eotp4))
eotp4.bind("<KeyRelease>",lambda event: nextbox(event,eotp4,eotp5))
eotp5.bind("<KeyRelease>",lambda event: nextbox(event,eotp5,eotp6))
eotp2.bind("<BackSpace>",lambda event: prevbox(event,eotp2,eotp1))
eotp3.bind("<BackSpace>",lambda event: prevbox(event,eotp3,eotp2))
eotp4.bind("<BackSpace>",lambda event: prevbox(event,eotp4,eotp3))
eotp5.bind("<BackSpace>",lambda event: prevbox(event,eotp5,eotp4))
eotp6.bind("<BackSpace>",lambda event: prevbox(event,eotp6,eotp5))

fpassword=tk.CTkFrame(master=win,corner_radius=20)
ecreatepassword=tk.CTkEntry(fpassword,placeholder_text="Enter password",width=325,corner_radius=30,show='*')
econfirmpassword=tk.CTkEntry(fpassword,placeholder_text="Enter password again",width=325,corner_radius=30,show='*')
lminchar=tk.CTkLabel(fpassword,text="At least 8 characters",text_color='red',font=tk.CTkFont(size=12,weight="bold"))
luppercase=tk.CTkLabel(fpassword,text="At least one uppercase letter",text_color='red',font=tk.CTkFont(size=12,weight="bold"))
llowercase=tk.CTkLabel(fpassword,text="At least one lowercase letter",text_color='red',font=tk.CTkFont(size=12,weight="bold"))
lnumber=tk.CTkLabel(fpassword,text="At least one number",text_color='red',font=tk.CTkFont(size=12,weight="bold"))
lspecialchar=tk.CTkLabel(fpassword,text="At least one special character",text_color='red',font=tk.CTkFont(size=12,weight="bold"))
lspace=tk.CTkLabel(fpassword,text="No spaces",text_color='red',font=tk.CTkFont(size=12,weight="bold"))
lmatch=tk.CTkLabel(fpassword,text="Passwords must match",text_color='red',font=tk.CTkFont(size=12,weight="bold"))
bnext4=tk.CTkButton(master=fpassword,text="Next",corner_radius=20,command=dpassword)

#CHECK GAMERTAG FOR DUPLICATES
fgamertag=tk.CTkFrame(master=win,corner_radius=20)
ecreateusername=tk.CTkEntry(fgamertag,placeholder_text="Enter Gamertag",width=325,corner_radius=30)
bnext5=tk.CTkButton(master=fgamertag,text="Sign Up!",corner_radius=20,command=lambda: dsignup() if ecreateusername.get() !="" else messagebox("Please fill in all fields"))

#START THE PROGRAM

music()
plogin()
win.mainloop()
mk.quit()
