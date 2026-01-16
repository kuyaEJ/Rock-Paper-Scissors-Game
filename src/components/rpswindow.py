import random
import tkinter as tk
import os
from pathlib import Path
from contextlib import contextmanager

class Window:
    def __init__(self, title, size):
        self.title = title
        self.size = size
    
    def launch(self, logic):
        self.logic = logic
        self.setup_window()
        self.setup_layout()
        self.load_resources()
        self.create_widgets()
        self.grid()
        self.window.mainloop()



    def setup_window(self):
        self.window = tk.Tk()
        self.window.geometry(self.size)
        self.window.title(self.title)


    def setup_layout(self):
        # Top Frame
        self.mainframe = tk.Frame(self.window, border=3)
        self.mainframe.pack(side=tk.TOP)

        # Display Label
        self.label = tk.Label(self.mainframe, text="Try to win against the Computer")
        
        # Bottom Frame
        self.botFrame = tk.Frame(self.window, border=3)
        self.botFrame.pack(side=tk.BOTTOM)
        # Computer And User Labels
        self.labeluser = tk.Label(self.botFrame, padx=60, pady=60, relief=tk.SUNKEN, bg="#221FFE")
        self.labelcomputer = tk.Label(self.botFrame, padx=60, pady=60, relief=tk.SUNKEN, bg="#FE1F34")



    def load_resources(self):
        # Defining Assets and States
        # IMPORTANT: Do not change the order of items since are dependent tables
        # TO-DO: Find solution of tables being dependent since it is risky
        self.assets = {
            'images': [
                tk.PhotoImage(file="src/assets/rock.png").subsample(2),
                tk.PhotoImage(file="src/assets/paper.png").subsample(2),
                tk.PhotoImage(file="src/assets/scissor.png").subsample(2)
            ],
            'names': ['rock', 'paper', 'scissor']
        }

        self.ui = {}




    def play(self, user_choice):

        # Shorten variables
        assets = self.assets
        computer_choice = random.choice([0,1,2])
        
        # Update scores and let the computer choose a random choice
        result_text, winner = self.logic.get_result(user_choice, computer_choice)
        
        # Create local variables to shorten syntax in reference
        us = self.logic.user_score
        cs = self.logic.computer_score
        
        # Considering logging in a different way with decorator functions
        print(result_text, "Winner:", winner)

        self.labeluser.configure(image=assets['images'][user_choice])
        self.labelcomputer.configure(image=self.assets['images'][computer_choice])

        # Clear result display then insert new score and display feed
        self.result_display.delete('1.0', tk.END)
        self.result_display.insert(
            tk.END, 
            f"Round {self.logic.round} \n" +
            f"Your chosen: {assets['names'][user_choice]} \n" + 
            f"Computer's chosen: {assets['names'][computer_choice]} \n" +
            f"Your Score: {us} \n Computer Score: {cs}\n\n"
        )




    def create_widgets(self):

        # Create and Grid the Results Display
        self.result_display = tk.Text(master=self.botFrame, height=12, width=30, bg="#FFDAC1")
        self.result_display.grid(column=1, row=1)

        # Create buttons and place them in table
        for i, name in enumerate(self.assets['names']):
            self.ui[f'btn_{name}'] = tk.Button(
                self.mainframe,
                image=self.assets['images'][i],
                command=lambda x=i: self.play(x)
            )
            self.ui[f'btn_{name}'].grid(column=i+1, row=0)




    def grid(self):

        # Grid Top Frame
        self.mainframe.pack(side=tk.TOP)
        self.label.grid(column=2, row=0)

        # Grid Buttons
        for i, name in enumerate(self.ui):
            self.ui[name].grid(column=i+1, row=1)

        # Grid User and Computer Labels
        self.botFrame.pack(side=tk.BOTTOM)
        self.labeluser.grid(column = 0, row = 1)
        self.labelcomputer.grid(column = 2, row = 1)
       
        # Grid MainFrame and Create Main Application Loop 
        self.mainframe.grid_columnconfigure(1, weight=1)