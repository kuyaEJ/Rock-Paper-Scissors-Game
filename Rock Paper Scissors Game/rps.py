# Gui Project Group 10
import random
import tkinter as tk
import os

window = tk.Tk()
window.title("RPS Game")

userscore = 0
compscore = 0
uc = ""
cc = "" 

def cton(chosen):
    r = {'rock':0,'paper':1,'scissor':2}
    return r[chosen]
def ntoc(num):
    r={0:'rock',1:'paper',2:'scissor'}
    return r[num]

def randomcomp():
    return random.choice(['rock','paper','scissor'])

def result(userc,cc, ui, ci):
    global userscore
    global compscore
    userinput=cton(userc)
    comp=cton(cc)
    if(userinput==comp):
        print("Tie")
    elif((userinput-comp)%3==1):
        print("You win")
        userscore+=1
    else:
        print("Comp wins")
        compscore+=1
    text_area = tk.Text(master=botFrame,height=12,width=30,bg="#FFDAC1")
    text_area.grid(column=1,row=1)
    answer = "Your chosen: {uc} \nComputer's chosen : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=uc,cc=cc,u=userscore,c=compscore)
    text_area.insert(tk.END,answer)
    Label_User.configure(image=ui)# User Image
    Label_Computer.configure(image=ci)# Computer Image

def rock():
    global uc
    global cc
    global ui
    global ci
    uc='rock'
    cc=randomcomp()
    ui=im2Rock
    ci = tk.PhotoImage(file=(cc + ".png")).subsample(2)
    result(uc,cc, ui, ci)
def paper():
    global uc
    global cc
    global ui
    global ci
    uc='paper'
    cc=randomcomp()
    ui=im2Paper
    ci = tk.PhotoImage(file=(cc + ".png")).subsample(2)
    result(uc,cc, ui, ci)
def scissor():
    global uc
    global cc
    global ui
    global ci
    uc='scissor'
    cc=randomcomp()
    ui=im2Scissors
    ci = tk.PhotoImage(file=(cc + ".png")).subsample(2)
    result(uc,cc, ui, ci)

# Get directory of the file executed and changes the current directory to where the Python file is at
directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(directory)

# Images
imROCK = tk.PhotoImage(file="rock.png")
im2Rock = imROCK.subsample(2)
imPAPER = tk.PhotoImage(file="paper.png")
im2Paper = imPAPER.subsample(2)
imSCISSORS = tk.PhotoImage(file="scissor.png")
im2Scissors = imSCISSORS.subsample(2)


# Top Frame
mainframe = tk.Frame(window, border=3)


# Top Frame Descendants
label = tk.Label(mainframe, text="Try to win against the Computer")
rockBUTTON = tk.Button(mainframe, image=im2Rock, padx=20, pady=10, relief=tk.RAISED, command=rock)
scissorsBUTTON = tk.Button(mainframe, image=im2Scissors, padx=20, pady=10, relief=tk.RAISED, command=scissor)
paperBUTTON = tk.Button(mainframe, image=im2Paper, padx=20, pady=10, relief=tk.RAISED, command=paper)

# Bottom Frame
botFrame = tk.Frame(window, border=3 )

# Bottom Frame Descendants
Label_User = tk.Label(botFrame, padx=60, pady=60, relief=tk.SUNKEN, bg="#221FFE")
Label_Computer = tk.Label(botFrame, padx=60, pady=60, relief=tk.SUNKEN, bg="#FE1F34")

# Grid/Pack/Main Loop
mainframe.pack(side=tk.TOP)
label.grid(column=2, row=0)
rockBUTTON.grid(column=1, row=1, padx=10, pady=10, rowspan=2, sticky=tk.E)
paperBUTTON.grid(column=2, row=1, padx=10, pady=10, rowspan=2, sticky=tk.N)
scissorsBUTTON.grid(column=3, row=1, padx=10, pady=10, rowspan=2, sticky=tk.W)
botFrame.pack(side=tk.BOTTOM)
Label_User.grid(column = 0, row = 1, sticky=tk.E)
Label_Computer.grid(column = 2, row = 1, sticky=tk.W)


mainframe.grid_columnconfigure(1, weight=1)
window.mainloop()