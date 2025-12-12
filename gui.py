from mazegenerator import mazegenerate
from mazesolver import mazessolve
from login import login,signup
import customtkinter as tk
from tkinter import messagebox,filedialog
from PIL import Image, ImageTk
from sendemail import otp

def realtimesolver():
    i = 0
    j = 0
    forkprocessor = []
    path = []
    f[0].putpixel((1,1),(0,255,0))
    while not (i == len(f[1]) - 1 and j == len(
            f[1]) - 1): #stops when it reaches goal
        if f[1][i][j][0] == -2: #Goes back to last fork if it reaches a dead end
            i = forkprocessor[- 3]
            j = forkprocessor[- 2]
            f[0].putpixel((2*j+1,2*i+1),(50,50,50)) #Marks the fork as visited more than once
            while not (i == path[-3] and j == path[- 2]): #Removes forks from the path till it goes back the fork we are on now
                path.pop()
                path.pop()
                path.pop()
            if forkprocessor[- 1]: #Visiting fork second time
                path.pop()
                path.append(f[1][i][j][1])
                if len(f[1][i][j]) == 2: #Removing this fork if it's not a triplet fork
                    forkprocessor.pop()
                    forkprocessor.pop()
                    forkprocessor.pop()
                else:
                    forkprocessor[- 1] = False #Marking it as visited twice
                if f[1][i][j][1] == 0:
                    f[0].putpixel((2*j+1,2*i),(0,255,0))
                    i = i - 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
                elif f[1][i][j][1] == 1:
                    f[0].putpixel((2*j+1,2*i+2),(0,255,0))
                    i = i + 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
                elif f[1][i][j][1] == 3:
                    f[0].putpixel((2*j+2,2*i+1),(0,255,0))
                    j = j + 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
                else:
                    f[0].putpixel((2*j,2*i+1),(0,255,0))
                    j = j - 1
                    f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            else: #Visiting fork third time
                path.pop()
                path.append(f[1][i][j][2])
                forkprocessor.pop()
                forkprocessor.pop()
                forkprocessor.pop()
                if f[1][i][j][2] == 0:
                    i = i - 1
                elif f[1][i][j][2] == 1:
                    i = i + 1
                elif f[1][i][j][2] == 3:
                    j = j + 1
                else:
                    j = j - 1
            continue
        if len(f[1][i][j]) == 1:
            if f[1][i][j][0] == 0:
                f[0].putpixel((2*j+1,2*i),(0,255,0))
                i = i - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0] == 1:
                f[0].putpixel((2*j+1,2*i+2),(0,255,0))
                i = i + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0] == 3:
                f[0].putpixel((2*j+2,2*i+1),(0,255,0))
                j = j + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            else:
                f[0].putpixel((2*j,2*i+1),(0,255,0))
                j = j - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
        else:
            #Append current coordinates plus current path taken (the first path)
            path.append(i)      
            path.append(j)
            path.append(f[1][i][j][0])
            forkprocessor.append(i)
            forkprocessor.append(j)
            forkprocessor.append(True)
            if f[1][i][j][0] == 0:
                f[0].putpixel((2*j+1,2*i),(0,255,0))
                i = i - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0] == 1:
                f[0].putpixel((2*j+1,2*i+2),(0,255,0))
                i = i + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            elif f[1][i][j][0] == 3:
                f[0].putpixel((2*j+2,2*i+1),(0,255,0))
                j = j + 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
            else:
                f[0].putpixel((2*j,2*i+1),(0,255,0))
                j = j - 1
                f[0].putpixel((2*j+1,2*i+1),(0,255,0))
        placeimg()
        win.update()
        win.update_idletasks()
    for i in range(len(path) - 1, -1, -1):
        if not ((i + 1) % 3 == 0):
            path.pop(i)
    i = 0
    j = 0
    while not (i==len(f[1])-1 and j==len(f[1])-1):
        f[0].putpixel((j + j + 1, i + i + 1), (255, 0, 0))
        if len(f[1][i][j]) == 1:
            if f[1][i][j][0] == 0:
                f[0].putpixel((j + j + 1, i + i), (255, 0, 0))
                i = i - 1
            elif f[1][i][j][0] == 1:
                f[0].putpixel((j + j + 1, i + i + 2), (255, 0, 0))
                i = i + 1
            elif f[1][i][j][0] == 3:
                f[0].putpixel((j + j + 2, i + i + 1), (255, 0, 0))
                j = j + 1
            else:
                f[0].putpixel((j + j, i + i + 1), (255, 0, 0))
                j = j - 1
        else:
            f[0].putpixel((j + j + 1, i + i + 1), (255, 0, 0))
            if path[0] == 0:
                f[0].putpixel((j + j + 1, i + i), (255, 0, 0))
                i = i - 1
            elif path[0] == 1:
                f[0].putpixel((j + j + 1, i + i + 2), (255, 0, 0))
                i = i + 1
            elif path[0] == 3:
                f[0].putpixel((j + j + 2, i + i + 1), (255, 0, 0))
                j = j + 1
            else:
                f[0].putpixel((j + j, i + i + 1), (255, 0, 0))
                j = j - 1
            path.pop(0)
    for i in range(1,n*2+1):
        for j in range(1,n*2+1):
            d = f[0].getpixel((i,j))
            if d==(0,255,0) or d==(50,50,50):
                f[0].putpixel((i,j),(255,255,255))
    placeimg()
    win.update()
    win.update_idletasks()

def sendemail():
    global otpcode, femail
    otpcode=str(otp(eemail.get()))
    femail.grid_forget()
    potp()

def nextbox(event, current_entry, next_entry):
    if event.keysym == "BackSpace":
        return
    while len(current_entry.get()) > 1:
        current_entry.delete(1)
    if len(current_entry.get()) == 1:
        next_entry.focus_set()

def prevbox(event, current_entry, previous_entry):
    current_entry.delete(0)
    if len(current_entry.get()) == 0:
        previous_entry.focus_set()

def checkotp():
    global fotp
    eotp=str(eotp1.get() + eotp2.get() + eotp3.get() + eotp4.get() + eotp5.get() + eotp6.get())
    if eotp == otpcode:
        print("OTP Verified")
        fotp.grid_forget()
        pgamertag()
    else:
        print("Invalid OTP")

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
    f[0],x=mazessolve(f[1],f[0])
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
    lmazepicl.grid(row=0, column=0, padx=10, pady=10)
    placeimg()
    emazesize.configure(state="readonly")

#LOGIN AND SIGNUP
def pgamertag():
    fgamertag.grid(row=0, column=0, padx=20, pady=20 ,columnspan=2, rowspan=5)
    ecreateusermane.grid(row=1, column=0, padx=20, pady=10,columnspan=2)
    bnext3.grid(row=2, column=0, columnspan=6, padx=10, pady=10,sticky="ew")
#PLAYING MAZE
def pname():
    fgamertag.grid(row=0, column=0, padx=20, pady=20 ,columnspan=2, rowspan=5)
    efirstname.grid(row=2, column=0, padx=20, pady=10,columnspan=2)
    elastname.grid(row=3, column=0, padx=20, pady=10,columnspan=2)
    bnext4.grid(row=4, column=0, columnspan=6, padx=10, pady=10,sticky="ew")
def ppassword():
    fgamertag.grid(row=0, column=0, padx=20, pady=20 ,columnspan=2, rowspan=5)
    ecreatepassword.grid(row=2, column=0, padx=20, pady=10,columnspan=2)
    econfirmpassword.grid(row=3, column=0, padx=20, pady=10,columnspan=2)
    bnext5.grid(row=4, column=0, columnspan=6, padx=10, pady=10,sticky="ew")

def potp():
    global otpcode
    fotp.grid(row=0, column=0, padx=20, pady=20 ,columnspan=10, rowspan=10)
    eotp1.grid(row=0, column=1, padx=10, pady=10,sticky="ew")
    eotp2.grid(row=0, column=2, padx=10, pady=10,sticky="ew")
    eotp3.grid(row=0, column=3, padx=10, pady=10,sticky="ew")
    eotp4.grid(row=0, column=4, padx=10, pady=10,sticky="ew")
    eotp5.grid(row=0, column=5, padx=10, pady=10,sticky="ew")
    eotp6.grid(row=0, column=6, padx=10, pady=10,sticky="ew")
    bnext2.grid(row=1, column=1, columnspan=6, padx=10, pady=10,sticky="ew")

def dlogin():
    username=eusermane.get()
    password=epassword.get()
    if login(username,password):
        global flogin
        flogin.grid_forget() 
        messagebox.showinfo("Logged In", "Successfully logged in")
        pmazecontrols()
    else:
        messagebox.showerror("Error", "Invalid username or password")
        
def dsignup():
    username=eusermane.get()
    password=epassword.get()
    try:
        signup(username,password)
        messagebox.showinfo("Signed Up", "Successfully signed up, you can now log in")
    except:
        messagebox.showerror("Error", "An error occurred during login/signup")

#LAYOUT FUNCTIONS
def pemail():
    global flogin
    flogin.grid_forget()
    femail.grid(row=0, column=0, padx=20, pady=20)
    lemail.grid(row=0, column=0, padx=20, pady=10, columnspan=2,sticky="ew")
    eemail.grid(row=1, column=0, padx=20, pady=10, columnspan=2,sticky="ew")
    bnext1.grid(row=2, column=0, padx=20, pady=10, columnspan=2,sticky="ew")

def plogin():
    flogin.grid(row=0, column=0, padx=20, pady=20 ,columnspan=2, rowspan=5)
    llogo.grid(row=0, column=0, padx=10, pady=10, sticky="n",columnspan=2)
    llogintxt.grid(row=1, column=0, padx=20, pady=10, columnspan=2,sticky="n")
    eusermane.grid(row=2, column=0, padx=20, pady=10,columnspan=2)
    epassword.grid(row=3, column=0, padx=20, pady=10,columnspan=2)
    blogin.grid(row=4, column=0, padx=20, pady=10,columnspan=2, sticky="ew")
    bsignup.grid(row=5, column=0, padx=7, pady=3,columnspan=2, sticky="w")

def pmazegame():
    fmazegame.grid(row=0, column=0, padx=20, pady=20 ,columnspan=10, rowspan=10,sticky="nsew")
    fmazegame.grid_columnconfigure(0, weight=1)

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
    sbimgtype.grid(row=8, column=16, padx=20, pady=10,columnspan=5,sticky="e")
    bsaveimgs.grid(row=9, column=11, padx=20, pady=10,columnspan=10,sticky="ew")
    bsaveimguns.grid(row=10, column=11, padx=20, pady=10,columnspan=10,sticky="ew")

#MAIN WINDOW SETUP

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
bsignup = tk.CTkButton(flogin, corner_radius=30,fg_color='transparent', hover=False, text="don't have an account?", text_color="#67C1FD", command=pemail)
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
emazesize = tk.CTkEntry(fmazecontrols, placeholder_text="Enter Maze Size(1-x)",width=325,corner_radius=30)
bgenmaze = tk.CTkButton(fmazecontrols, corner_radius=30, text="generate maze", command=genm)
lalgtxt = tk.CTkLabel(fmazecontrols, text="Algoritmic solving:", font=tk.CTkFont(size=20, weight="bold"))
bsolamaze = tk.CTkButton(fmazecontrols, corner_radius=30, text="Solve fast", command=solvemaze,width=155)
bsolsmaze = tk.CTkButton(fmazecontrols, corner_radius=30, text="see the program", command=realtimesolver,width=155)
lsavefiletxt = tk.CTkLabel(fmazecontrols, text="Saving and Exporting:", font=tk.CTkFont(size=20, weight="bold"))
bfilesave = tk.CTkButton(fmazecontrols, corner_radius=30, text="Save File", command=lambda: progressbar.start(),width=155)
bfileload = tk.CTkButton(fmazecontrols, corner_radius=30, text="Load File", command=lambda: progressbar.start(),width=155)
limgtypetxt = tk.CTkLabel(fmazecontrols, text="Select Image Type:", font=tk.CTkFont(size=15, weight="bold"))
sbimgtype = tk.CTkSegmentedButton(fmazecontrols, values=[".jpg", ".png", ".webp"],corner_radius=30)
sbimgtype.set(".png")
bsaveimgs = tk.CTkButton(fmazecontrols, corner_radius=30, text="export unsoved maze to image", command=lambda: f[2].resize((1080,1080), Image.NONE).save(filedialog.asksaveasfilename(initialdir="/",title="Save File As",initialfile="output",defaultextension=sbimgtype.get())))
bsaveimguns = tk.CTkButton(fmazecontrols, corner_radius=30, text="export solved maze to image", command=lambda: f[3].resize((1080,1080), Image.NONE).save(filedialog.asksaveasfilename(initialdir="/",title="Save File As",initialfile="output",defaultextension=sbimgtype.get())))
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)


fmazegame.bind("<Configure>", resizeimage)
bsignup.bind("<Enter>", lambda event: bsignup.cget("font").configure(underline=True))
bsignup.bind("<Leave>", lambda event: bsignup.cget("font").configure(underline=False))

femail = tk.CTkFrame(master=win, corner_radius=20)
lemail = tk.CTkLabel(master=femail, text="Enter your email adress", font=tk.CTkFont(size=20, weight="bold"))
eemail= tk.CTkEntry(master=femail, placeholder_text="Enter your email", width=300, border_width=2, corner_radius=30)
bnext1= tk.CTkButton(master=femail, text="Next", corner_radius=20, command=sendemail)
fotp = tk.CTkFrame(master=win, corner_radius=20)
eotp1= tk.CTkEntry(master=fotp, placeholder_text="x", width=40, height=60, border_width=2, corner_radius=10, justify='center',font=tk.CTkFont(size=24))
eotp2= tk.CTkEntry(master=fotp, placeholder_text="x", width=40, height=60, border_width=2, corner_radius=10, justify='center',font=tk.CTkFont(size=24))
eotp3= tk.CTkEntry(master=fotp, placeholder_text="x", width=40, height=60, border_width=2, corner_radius=10, justify='center',font=tk.CTkFont(size=24))
eotp4= tk.CTkEntry(master=fotp, placeholder_text="x", width=40, height=60, border_width=2, corner_radius=10, justify='center',font=tk.CTkFont(size=24))
eotp5= tk.CTkEntry(master=fotp, placeholder_text="x", width=40, height=60, border_width=2, corner_radius=10, justify='center',font=tk.CTkFont(size=24))
eotp6= tk.CTkEntry(master=fotp, placeholder_text="x", width=40, height=60, border_width=2, corner_radius=10, justify='center',font=tk.CTkFont(size=24))
bnext2= tk.CTkButton(master=fotp, text="Next", corner_radius=20,command=checkotp)
eotp1.bind("<KeyRelease>", lambda event: nextbox(event, eotp1, eotp2))
eotp2.bind("<KeyRelease>", lambda event: nextbox(event, eotp2, eotp3))
eotp3.bind("<KeyRelease>", lambda event: nextbox(event, eotp3, eotp4))
eotp4.bind("<KeyRelease>", lambda event: nextbox(event, eotp4, eotp5))
eotp5.bind("<KeyRelease>", lambda event: nextbox(event, eotp5, eotp6))
eotp2.bind("<BackSpace>", lambda event: prevbox(event, eotp2, eotp1))
eotp3.bind("<BackSpace>", lambda event: prevbox(event, eotp3, eotp2))
eotp4.bind("<BackSpace>", lambda event: prevbox(event, eotp4, eotp3))
eotp5.bind("<BackSpace>", lambda event: prevbox(event, eotp5, eotp4))
eotp6.bind("<BackSpace>", lambda event: prevbox(event, eotp6, eotp5))
fgamertag = tk.CTkFrame(master=win, corner_radius=20)
ecreateusermane = tk.CTkEntry(fgamertag, placeholder_text="Enter Username",width=325,corner_radius=30)
bnext3= tk.CTkButton(master=fgamertag, text="Next", corner_radius=20,command=pname)
fname = tk.CTkFrame(master=win, corner_radius=20)
efirstname = tk.CTkEntry(fname, placeholder_text="Enter Username",width=325,corner_radius=30)
elastname = tk.CTkEntry(fname, placeholder_text="Enter Username",width=325,corner_radius=30)
bnext4= tk.CTkButton(master=fname, text="Next", corner_radius=20,command=ppassword)
fpassword = tk.CTkFrame(master=win, corner_radius=20)
ecreatepassword = tk.CTkEntry(fpassword, placeholder_text="Enter password",width=325,corner_radius=30, show='*')
econfirmpassword = tk.CTkEntry(fpassword, placeholder_text="Enter password again",width=325,corner_radius=30, show='*')
bnext5= tk.CTkButton(master=fpassword, text="Next", corner_radius=20,command=plogin)

plogin()
win.mainloop()