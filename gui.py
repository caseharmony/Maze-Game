from mazegenerator import mazegenerate
from mazesolver import mazessolve
import customtkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def lockmaze():
    global lock,emazesize
    lock=True
    emazesize.configure(state='normal')
    
def resizeimage(event):
    global h,w,lmazepicl
    w = event.width
    h = event.height
    if w / h > 1:
        w=h
    else:
        h=w
    h,w=h-h//20,w-w//20
    if h <=0 or w <=0:
        h,w=1,1
    lmazepic.configure(size=(h,w))
    lmazepicl.configure(image=lmazepic)

def placeimg():
    global lmazepic,lmazepicl
    lmazepic = tk.CTkImage(dark_image=f[0].resize((1080,1080),Image.NONE),size=(h, w))
    lmazepicl.configure(image=lmazepic)

def solvemaze():
    if lock:
        return
    f[0]=mazessolve(f[1],f[0])
    f.append(f[0].copy())
    placeimg()
    lockmaze()
    
def reset():
    global lock
    lock=False
    fmazegame.grid_forget()
    win.focus_set()

def left(event):
    if lock:
        return
    global x,emazesize
    x = x - 1
    r, g, b = f[0].getpixel((x, y))
    if x == n * 2 - 1 and y == n * 2 - 1:
        messagebox.showinfo("Congrats!", "Congrats on completing the maze!!")
        lockmaze()
        return
    if r == 0 and g == 0 and b == 0:
        x = x + 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x + 1, y), (255, 255, 255))
    placeimg()

def right(event):
    if lock:
        return
    global x,emazesize
    x = x + 1
    r, g, b = f[0].getpixel((x, y))
    if x == n * 2 - 1 and y == n * 2 - 1:
        messagebox.showinfo("Congrats!", "Congrats on completing the maze!!")
        lockmaze()
        return
    if r == 0 and g == 0 and b == 0:
        x = x - 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x - 1, y), (255, 255, 255))
    placeimg()

def up(event):
    if lock:
        return
    global y,emazesize
    y = y - 1
    if x == n * 2 - 1 and y == n * 2 - 1:
        messagebox.showinfo("Congrats!", "Congrats on completing the maze!!")
        lockmaze()
        return
    r, g, b = f[0].getpixel((x, y))
    if r == 0 and g == 0 and b == 0:
        y = y + 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x, y + 1), (255, 255, 255))
    placeimg()

def down(event):
    if lock:
        return
    global y,emazesize
    y = y + 1
    if x == n * 2 - 1 and y == n * 2 - 1:
        messagebox.showinfo("Congrats!", "Congrats on completing the maze!!")
        lockmaze()
        return
    r, g, b = f[0].getpixel((x, y))
    if r == 0 and g == 0 and b == 0:
        y = y - 1
        return
    if g == 255:
        f[0].putpixel((x, y), (255, 0, 0))
    else:
        f[0].putpixel((x, y - 1), (255, 255, 255))
    placeimg()

def genm():
    reset()
    pmazegame()
    global f,n,x,y,emazesize
    x,y=1,1
    n=int(emazesize.get())
    f=mazegenerate(n)
    f.append(f[0].copy())
    global lmazepic
    img = f[0].resize((win.winfo_screenheight() - 120, win.winfo_screenheight() - 120),Image.NONE)
    lmazepicl.grid(row=0, column=0, padx=10, pady=10)
    placeimg()
    emazesize.configure(state="readonly")

def dlogin():
    global flogin
    flogin.grid_forget() 
    messagebox.showinfo("ERROR", "404 Not Found")
    pmazecontrols()

def plogin():
    flogin.grid(row=0, column=0, padx=20, pady=20 ,columnspan=2, rowspan=5)
    llogintxt.grid(row=1, column=0, padx=20, pady=10, columnspan=2,sticky="n")
    eusermane.grid(row=2, column=0, padx=20, pady=10,columnspan=2)
    epassword.grid(row=3, column=0, padx=20, pady=10,columnspan=2)
    bsignup.grid(row=4, column=0, padx=10, pady=10)
    blogin.grid(row=4, column=1, padx=10, pady=10)
    llogo.grid(row=0, column=0, padx=10, pady=10, sticky="n",columnspan=2)

def pmazegame():
    fmazegame.grid(row=0, column=0, padx=20, pady=20 ,columnspan=10, rowspan=10,sticky="nsew")
    fmazegame.grid_columnconfigure(0, weight=1)
    #fmazegame.grid_rowconfigure(1, weight=1)
    #lmazegametxt.grid(row=0, column=0, padx=20, pady=10)
    #progressbar.grid(row=1, column=0, padx=20, pady=10,columnspan=10,sticky="ew")

def pmazecontrols():
    fmazecontrols.grid(row=0, column=11, padx=20, pady=20 ,columnspan=10, rowspan=10,sticky="nsew")
    lcontrolstxt.grid(row=0, column=11, padx=20, pady=10,columnspan=10,sticky="w")
    lgentxt.grid(row=1, column=11, padx=20, pady=10,columnspan=6,sticky="w")
    emazesize.grid(row=2, column=11, padx=20, pady=10,columnspan=10,sticky="ew")
    bgenmaze.grid(row=3, column=11, padx=20, pady=10,columnspan=10,sticky="ew")
    lalgtxt.grid(row=4, column=11, padx=20, pady=10,columnspan=6,sticky="w")
    bsolamaze.grid(row=5, column=11, padx=20, pady=10,columnspan=5,sticky="w")
    bsolsmaze.grid(row=5, column=16, padx=20, pady=10,columnspan=5,sticky="e")
    lsavefiletxt.grid(row=6, column=11, padx=20, pady=10,columnspan=6,sticky="w")
    bfilesave.grid(row=7, column=11, padx=20, pady=10,columnspan=5,sticky="w")
    bfileload.grid(row=7, column=16, padx=20, pady=10,columnspan=5,sticky="e")
    limgtypetxt.grid(row=8, column=11, padx=20, pady=10,columnspan=5,sticky="w")
    sbimgtype.set(".png")
    sbimgtype.grid(row=8, column=16, padx=20, pady=10,columnspan=5,sticky="e")
    bsaveimgs.grid(row=9, column=11, padx=20, pady=10,columnspan=10,sticky="ew")
    bsaveimguns.grid(row=10, column=11, padx=20, pady=10,columnspan=10,sticky="ew")

lock,n,x,y,f,h,w=False,0,1,1,[],1,1
win = tk.CTk()
win.title("Maze Game")
win.geometry(str(win.winfo_screenwidth()) + "x" + str(win.winfo_screenheight()))
tk.set_window_scaling(0.6)
tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
win.grid_columnconfigure(0, weight=1)
win.grid_rowconfigure(0, weight=1)
flogin = tk.CTkFrame(master=win, corner_radius=20)
llogintxt = tk.CTkLabel(flogin, text="Log in OR Sign Up", font=tk.CTkFont(size=20, weight="bold"))
eusermane = tk.CTkEntry(flogin, placeholder_text="Enter Username",width=325,corner_radius=30)
epassword = tk.CTkEntry(flogin, placeholder_text="Enter password",width=325,corner_radius=30, show='*')
bsignup = tk.CTkButton(flogin, corner_radius=30, text="Sign up", command=dlogin)
blogin = tk.CTkButton(flogin, corner_radius=30, text="login", command=dlogin)
try:
    llogo = tk.CTkImage(dark_image=Image.open("./im.png"),size=(300,300))
except:
    llogo = tk.CTkImage(dark_image=Image.new("RGB",(300,300),(0,0,0)),size=(300,300))
llogo = tk.CTkLabel(flogin, image=llogo, text="")
fmazegame = tk.CTkFrame(master=win, corner_radius=20)
lmazepic = None
lmazepicl = tk.CTkLabel(fmazegame, image=lmazepic, text="")
lmazegametxt = tk.CTkLabel(fmazegame, text="Maze Game", font=tk.CTkFont(size=30, weight="bold"))
progressbar = tk.CTkProgressBar(fmazegame,orientation="horizontal",mode="indeterminate")
fmazecontrols=tk.CTkFrame(master=win, corner_radius=20,width=350)
lcontrolstxt = tk.CTkLabel(fmazecontrols, text="Controls:", font=tk.CTkFont(size=30, weight="bold"))
lgentxt = tk.CTkLabel(fmazecontrols, text="Configure and Generate:", font=tk.CTkFont(size=20, weight="bold"))
emazesize = tk.CTkEntry(fmazecontrols, placeholder_text="Enter Maze Size(1-x)",width=350,corner_radius=30)
bgenmaze = tk.CTkButton(fmazecontrols, corner_radius=30, text="generate maze", command=genm)
lalgtxt = tk.CTkLabel(fmazecontrols, text="Algoritmic solving:", font=tk.CTkFont(size=20, weight="bold"))
bsolamaze = tk.CTkButton(fmazecontrols, corner_radius=30, text="Solve fast", command=solvemaze,width=155)
bsolsmaze = tk.CTkButton(fmazecontrols, corner_radius=30, text="see the program", command=lambda: progressbar.start(),width=155)
lsavefiletxt = tk.CTkLabel(fmazecontrols, text="Saving and Exporting:", font=tk.CTkFont(size=20, weight="bold"))
bfilesave = tk.CTkButton(fmazecontrols, corner_radius=30, text="Save File", command=lambda: progressbar.start(),width=155)
bfileload = tk.CTkButton(fmazecontrols, corner_radius=30, text="Load File", command=lambda: progressbar.start(),width=155)
limgtypetxt = tk.CTkLabel(fmazecontrols, text="Select Image Type:", font=tk.CTkFont(size=15, weight="bold"))
sbimgtype = tk.CTkSegmentedButton(fmazecontrols, values=[".jpg", ".png", ".svg"],corner_radius=30)
sbimgtype.set(".png")
bsaveimgs = tk.CTkButton(fmazecontrols, corner_radius=30, text="export unsoved maze to image", command=lambda: f[2].resize((1080,1080), Image.NONE).save(str("C:\\Users\\chotu\\downloads\\output"+sbimgtype.get())))
bsaveimguns = tk.CTkButton(fmazecontrols, corner_radius=30, text="export solved maze to image", command=lambda: f[3].resize((1080,1080), Image.NONE).save(str("C:\\Users\\chotu\\downloads\\output"+sbimgtype.get())))
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)
fmazegame.bind("<Configure>", resizeimage)
plogin()
win.mainloop()