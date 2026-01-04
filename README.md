# Rock Paper Scissors Game – CS 1010 Final Project
## 📌 Project Overview
This is a classic **Rock Paper Scissors** game developed for my **CS 1010: Introduction to Higher Programming** course at **California State University, Los Angeles (CSULA)**.  The goal of the project was to practice basic programming logic by creating a functional game where a user can play against the computer. The project demonstrates fundamental programming concepts, including control flow, user input handling, and basic GUI/asset management.

## 🎮 How It Works
- **User Input**: The player selects Rock, Paper, or Scissors.
- **Computer Choice**: The computer randomly selects an option.
- **Logic**: The program uses basic `if/else` statements to determine the winner based on the choices made.
- **Score Tracking**: The game tracks wins and losses and updates the score after each round.
- **Display**: A simple textbox updates to show who won the round and the current score.

## 🛠️ Built With
- **Programming Language**: `Python`
- **Assets**: Simple image files for Rock, Paper, and Scissors sourced from Google Images. (rock.png, paper.png, scissors.png).

## 📂 File Structure
- `rock.png:`, `paper.png`, `scissor.png`: Visual assets for the game choices
- `README.md`: Project description and credits
- `rps.py`: Source code of the core game logic.
```python
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
```

## 🚀 How to Run
1. Download or clone the repository:

```Bash
git clone https://github.com/kuyaEJ/Rock-Paper-Scissors-Game.git
```

2. Open the project in your code editor or open a command line. Navigate to the folder:

```Bash
cd "Rock Paper Scissors Game"
```

3. Run the script with the command:
```Python
python main.py
```

For other languages the compilers use different commands such as: `javac Game.java` & `java Game`)

## 🎓 Academic Context
This project was completed as part of the CS 1010 curriculum at CSULA. It emphasizes:
- Using conditional statements for game rules.
- Managing and updating variables (scores).
- Linking simple UI elements (textboxes and images) to the code logic.

## Credits
Final Project from CS 1010 by Group 10: Kyle Chau, Micheal Buna, and Erick Vergara
