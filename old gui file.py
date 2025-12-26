from mazegenerator import mazegenerate
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from something_copy import solvemaze
import time

gg = False
n = 0
f = []  #Unessary overhead... but also necessary
y = 1
x = 1  #j in image
#y = 1  #i in image


#also add protection for when home screen is clicked when maze is being solved - Done
#Add mazesolver button

def left(event):
    del event
    #edit image and display(update)
    global x
    x = x - 1
    r, g, b = f[0].getpixel((x, y))
    #also add check to see if pixel is black, cant have the pointer overriding walls
    #dont need to check if user has won, can never win with left
    if r == 0 and g == 0 and b == 0:
        x = x + 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x + 1, y), (255, 255, 255))
    global image_label1
    new_image = ImageTk.PhotoImage(
        f[0].resize((root.winfo_screenheight() - 90, root.winfo_screenheight() - 90), Image.NEAREST))
    image_label1.config(image=new_image)  #config doesnt exist?
    image_label1.image = new_image


def right(event):
    del event
    global x
    x = x + 1
    if x == n * 2 - 1 and y == n * 2 - 1:
        messagebox.showinfo("Congrats!", "Congrats on completing the maze!!")
        root.focus_set()
        return
    r, g, b = f[0].getpixel((x, y))
    if r == 0 and g == 0 and b == 0:
        x = x - 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x - 1, y), (255, 255, 255))
    global image_label1
    new_image = ImageTk.PhotoImage(
        f[0].resize((root.winfo_screenheight() - 90, root.winfo_screenheight() - 90), Image.NEAREST))
    image_label1.config(image=new_image)  # config doesnt exist?
    image_label1.image = new_image


def up(event):
    del event
    global y
    y = y - 1
    #no need to check if user has won, cant go up to winning square, ever
    r, g, b = f[0].getpixel((x, y))
    if r == 0 and g == 0 and b == 0:
        y = y + 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x, y + 1), (255, 255, 255))
    global image_label1
    new_image = ImageTk.PhotoImage(
        f[0].resize((root.winfo_screenheight() - 90, root.winfo_screenheight() - 90), Image.NEAREST))
    image_label1.config(image=new_image)  # config doesnt exist?
    image_label1.image = new_image


def down(event):
    del event
    global y
    y = y + 1
    if x == n * 2 - 1 and y == n * 2 - 1:
        messagebox.showinfo("Congrats!", "Congrats on completing the maze!!")
        root.focus_set()
        return
    r, g, b = f[0].getpixel((x, y))
    if r == 0 and g == 0 and b == 0:
        y = y - 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x, y - 1), (255, 255, 255))
    global image_label1
    new_image = ImageTk.PhotoImage(
        f[0].resize((root.winfo_screenheight() - 90, root.winfo_screenheight() - 90), Image.NEAREST))
    image_label1.config(image=new_image)  # config doesnt exist?
    image_label1.image = new_image


def sample():
    global n
    if n == 0:
        messagebox.showerror("Input First",
                             "Before trying to generate a maze, enter the dimensions of the square maze in the textbox above")
        return
    generatorframe.focus_set()
    mazesolver1.config(command=solvemaze1)
    mazesolver2.config(command=solvemaze2)
    stop.config(command=placeholder)
    global f
    f = mazegenerate(n)  #unadultrated image
    #f[0].show()
    #for p in range(40):  # make number larger for more prescision
    #   entryframe.grid_rowconfigure(p, weight=1)
    #for p in range(40):
    #   entryframe.grid_columnconfigure(p, weight=1)
    global image_label1
    new_image = ImageTk.PhotoImage(
        f[0].resize((root.winfo_screenheight() - 90, root.winfo_screenheight() - 90), Image.NEAREST))
    image_label1 = tk.Label(generatorframe, image=new_image)
    image_label1.image = new_image  #this thing fixed the code
    del new_image
    image_label1.grid(row=0, column=0, padx=1, pady=1)
    entryframe.grid_forget()
    generatorframe.grid(row=0, column=0, sticky="nsew") #row configuration and all must be done here

def submitfunc():
    global n
    try:
        n = int(entry.get())
        if n < 3 or n > 120:  #maybe move the number check to sample, as would want to take in bigger numbers for mazesolver (random maze solution)
            messagebox.showerror("Invalid Input", "Please input a number in the range of 3 to 120 (inclusive)")
            n = 0
            entry.delete(0, tk.END)
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please input a number using only the number characters")
        n = 0
        entry.delete(0, tk.END)
        return
    entry.delete(0, tk.END)
    sample()


def Backgenerator():
    global x, y, gg
    x = 1
    y = 1
    if gg:
        gg = False
        time.sleep(0.4)
    generatorframe.grid_forget()
    entryframe.grid(sticky="nsew")
    #mazegeneratorbutton.grid(row=20, column=0, padx=0, pady=0)
    label.grid(row=19, column=0, padx=0, pady=0)
    entry.grid(row=19, column=1, padx=0, pady=0)
    global f
    f = []
    #have to stop it solving if it is... somehow


def stopsolve():
    global mazesolver1,mazesolver2,stop,x,y
    mazesolver1.config(command=solvemaze1)
    mazesolver2.config(command=solvemaze2)
    stop.config(command=placeholder)
    global gg
    gg = False
    time.sleep(0.4)
    gh = f[0].size[0]
    for p in range(0, gh):
        for y in range(0, gh):
            r,g= f[0].getpixel((y, p))[:2]
            if (g>0 and not(r==255) or (r==255 and g==0)) :#need to replace all green pixels with white, and also (100,100,100) and (150,150,150),(0,255,0),(255,0,0)
                f[0].putpixel((y, p), (255, 255, 255))
    f[0].putpixel((1,1),(255,0,0))
    f[0].putpixel((gh-2,gh-2),(0,255,0))
    update_image()
    root.update()
    root.update_idletasks()
    generatorframe.focus_set()
    x = 1
    y = 1
    


def solvemaze1():
    #solve maze in green
    global gg
    gg = True
    root.focus_set()
    #f[0] = solvemaze(f[1], f[0])  #maze,image
    #update_image()
    mazesolver1.config(command=placeholder)
    mazesolver2.config(command=placeholder)
    stop.config(command=stopsolve)
    i = 0
    j = 0
    forkprocessor = []
    path = []
    maze = f[1]
    f.pop()
    while not (i == len(maze) - 1 and j == len(
            maze) - 1):  # make while true loop and have condition in here to break; and to add to incomplete path
        # print(i, j)
        # print("path = ", path)
        # print(forkprocessor)
        # print(i,j)
        #time.sleep(0.025)
        if not gg:
            f.append(maze)
            del maze
            return
        f[0].putpixel((j + j + 1, i + i + 1), (0, 255, 0))
        update_image()
        root.update()
        root.update_idletasks()
        #time.sleep(0.5)
        if maze[i][j][0] == -2:
            i = forkprocessor[len(forkprocessor) - 3]
            j = forkprocessor[len(forkprocessor) - 2]
            # print("Reached dead end, coordinates of previous viable fork are", i, j)
            # print("This is path", path)
            while not (i == path[len(path) - 3] and j == path[
                len(path) - 2]):  # POPs path if i and j values are not equal; previous fork
                # print("Removing last fork from path as all paths from that one have been explored")
                path.pop()
                path.pop()
                path.pop()
            #  print("done,",path)
            if forkprocessor[len(forkprocessor) - 1]:  # ==True
                f[0].putpixel((j + j + 1, i + i + 1), (100, 100, 100))
                update_image()
                path.pop()
                path.append(maze[i][j][1])
                if len(maze[i][j]) == 2:
                    # print("Trying to POP forkprocessor",forkprocessor)
                    forkprocessor.pop()
                    forkprocessor.pop()
                    forkprocessor.pop()
                    # print("done?",forkprocessor)
                else:
                    forkprocessor[len(forkprocessor) - 1] = False
                if maze[i][j][1] == 0:
                    f[0].putpixel((j + j + 1, i + i), (0, 255, 0))
                    update_image()
                    i = i - 1
                elif maze[i][j][1] == 1:
                    f[0].putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                    update_image()
                    i = i + 1
                elif maze[i][j][1] == 3:
                    f[0].putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                    update_image()
                    j = j + 1
                else:
                    f[0].putpixel((j + j, i + i + 1), (0, 255, 0))
                    update_image()
                    j = j - 1
                root.update_idletasks()
                root.update()
            else:
                f[0].putpixel((j + j + 1, i + i + 1), (150, 150, 150))
                update_image()
                path.pop()
                path.append(maze[i][j][2])
                forkprocessor.pop()
                forkprocessor.pop()
                forkprocessor.pop()
                if maze[i][j][2] == 0:
                    f[0].putpixel((j + j + 1, i + i), (0, 255, 0))
                    update_image()
                    i = i - 1
                elif maze[i][j][2] == 1:
                    f[0].putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                    update_image()
                    i = i + 1
                elif maze[i][j][2] == 3:
                    f[0].putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                    update_image()
                    j = j + 1
                else:
                    f[0].putpixel((j + j, i + i + 1), (0, 255, 0))
                    update_image()
                    j = j - 1
                root.update_idletasks()
                root.update()
            continue

        if len(maze[i][j]) == 1:
            if maze[i][j][0] == 0:
                f[0].putpixel((j + j + 1, i + i), (0, 255, 0))
                update_image()
                i = i - 1
            elif maze[i][j][0] == 1:
                f[0].putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                update_image()
                i = i + 1
            elif maze[i][j][0] == 3:
                f[0].putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                update_image()
                j = j + 1
            else:
                f[0].putpixel((j + j, i + i + 1), (0, 255, 0))
                update_image()
                j = j - 1
            root.update_idletasks()
            root.update()

        else:
            # print("found fork at ", i, j)
            path.append(i)
            path.append(j)
            if (i==len(maze)-1 or j==len(maze)-1):
                for g in range(len(maze[i][j])):
                    if maze[i][j][g] == 0:
                        f[0].putpixel((j + j + 1, i + i), (0, 255, 0))
                        update_image()
                        i = i - 1
                        if i==len(maze)-1:
                            path.append(maze[i][j][g])
                            break
                    elif maze[i][j][g] == 1:
                        f[0].putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                        update_image()
                        i = i + 1
                        if i==len(maze)-1:
                            path.append(maze[i][j][g])
                            break
                    elif maze[i][j][g] == 3:
                        f[0].putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                        update_image()
                        j = j + 1
                        if j==len(maze)-1:
                            path.append(maze[i][j][g])
                            break
                    else:
                        f[0].putpixel((j + j, i + i + 1), (0, 255, 0))
                        update_image()
                        j = j - 1
                        if j==len(maze)-1:
                            path.append(maze[i][j][g])
                            break
            path.append(maze[i][j][0])
            # print("New path = ", path)
            forkprocessor.append(i)
            forkprocessor.append(j)
            forkprocessor.append(
                True)  # second path - true. then remove it based on the length. else third path, and remove it immediately
            if maze[i][j][0] == 0:
                f[0].putpixel((j + j + 1, i + i), (0, 255, 0))
                update_image()
                i = i - 1
            elif maze[i][j][0] == 1:
                f[0].putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                update_image()
                i = i + 1
            elif maze[i][j][0] == 3:
                f[0].putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                update_image()
                j = j + 1
            else:
                f[0].putpixel((j + j, i + i + 1), (0, 255, 0))
                update_image()
                j = j - 1
            root.update_idletasks()
            root.update()
    for i in range(len(path) - 1, -1, -1):
        if not ((i + 1) % 3 == 0):
            path.pop(i)

    #global n
    gh = f[0].size[0]
    for i in range(0, gh):
        for j in range(0, gh):
            r, g = f[0].getpixel((j, i))[:2]
            if r == 0 and (not g == 0):
                f[0].putpixel((j, i), (255, 255, 255))
    i = 0
    j = 0
    while not (i == len(maze) - 1 and j == len(maze) - 1):
        f[0].putpixel((j + j + 1, i + i + 1), (0, 255, 0))
        if len(maze[i][j]) == 1:
            if maze[i][j][0] == 0:
                f[0].putpixel((j + j + 1, i + i), (0, 255, 0))
                i = i - 1
            elif maze[i][j][0] == 1:
                f[0].putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                i = i + 1
            elif maze[i][j][0] == 3:
                f[0].putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                j = j + 1
            else:
                f[0].putpixel((j + j, i + i + 1), (0, 255, 0))
                j = j - 1
        else:
            f[0].putpixel((j + j + 1, i + i + 1), (0, 255, 0))
            if path[0] == 0:
                f[0].putpixel((j + j + 1, i + i), (0, 255, 0))
                i = i - 1
            elif path[0] == 1:
                f[0].putpixel((j + j + 1, i + i + 2), (0, 255, 0))
                i = i + 1
            elif path[0] == 3:
                f[0].putpixel((j + j + 2, i + i + 1), (0, 255, 0))
                j = j + 1
            else:
                f[0].putpixel((j + j, i + i + 1), (0, 255, 0))
                j = j - 1
            path.pop(0)
    f[0].putpixel((gh-2,gh-2),(0,255,0))
    update_image()
    gg = False
    stop.config(command=placeholder)


def placeholder():
    messagebox.showerror("Sorry", "This action is not possible at the moment")


def update_image():
    global image_label1
    new_image = ImageTk.PhotoImage(
        f[0].resize((root.winfo_screenheight() - 90, root.winfo_screenheight() - 90), Image.NEAREST))
    image_label1.config(image=new_image)  # config doesnt exist?
    image_label1.image = new_image

def solvemaze2():
    root.focus_set()
    mazesolver1.config(command=placeholder)
    mazesolver2.config(command=placeholder)
    f[0] = solvemaze(f[1],f[0])
    update_image()

root = tk.Tk()
root.configure(bg='black')
root.title("Maze generator and solver")
entryframe = tk.Frame(root, bg='black')
entryframe.grid(row=0, column=0, sticky="nsew")
for p in range(40):  #make number larger for more prescision
    entryframe.grid_rowconfigure(p, weight=1)
for p in range(40):
    entryframe.grid_columnconfigure(p, weight=1)
#mazegeneratorbutton = tk.Button(entryframe, text="Mazegenerator", command=sample, width=15, height=2)
#mazegeneratorbutton.grid(row=20, column=0, padx=0, pady=0)
label = tk.Label(entryframe, text="dimensions of the maze = ")
label.grid(row=19, column=0, padx=0, pady=0)
entry = tk.Entry(entryframe)
entry.grid(row=19, column=1, padx=0, pady=0)
submit = tk.Button(entryframe, text="Submit", command=submitfunc)
submit.grid(row=19, column=2, padx=0, pady=0)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
generatorframe = tk.Frame(root, bg="black")
image_label1: tk.Label  #just doing this so that its a global variabke
generatorframe.bind("<Left>", left)
generatorframe.bind("<Right>", right)
generatorframe.bind("<Up>", up)
generatorframe.bind("<Down>", down)
#row and column configuration of generatorframe used to be here
Back1 = tk.Button(generatorframe, text="Home screen", command=Backgenerator, width=15, height=3)
mazesolver1 = tk.Button(generatorframe, text="Solve the maze and see what the algorithm is doing",  width=40, height=4)
mazesolver2 = tk.Button(generatorframe, text="Solve the maze fast",width=15,height=3)  
stop = tk.Button(generatorframe,text="Stop solving",width=9,height=3)
Back1.grid(row=0, column=2, padx=10, pady=10)  # move this to sample
mazesolver1.grid(row=0, column=5, padx=10, pady=10)  # move this to sample
stop.grid(row=0,column=6,padx=8,pady=8)
mazesolver2.grid(row=0, column=7, padx=10, pady=10)  # move this to sample
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry(str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()))
root.mainloop()

