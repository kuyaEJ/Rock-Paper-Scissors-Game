import tkinter as tk
from random import choice
from components.easygp import EasyGridPacker

class Window:
    def __init__(self, title, size):
        egp = EasyGridPacker()
        egp.setup_window(title, size)
        self.egp = egp
    
    def launch(self, logic):
        self.logic = logic
        self.setup_layout()
        self.load_resources()
        self.create_widgets()
        self.grid()
        self.egp.root.mainloop()



    def setup_layout(self):
        # Local ref to EasyGridPacker instance
        egp = self.egp
        # Top Frame
        mainframe = egp.add_frame(tk.TOP)

        # Display Label
        egp.add_label(mainframe, "Try to win against the Computer", 2, 0)

        # Bottom Frame
        botframe = egp.add_frame(tk.BOTTOM)
        # Computer and User Labels
        self.userlabel = egp.add_label(botframe, "", 0, 1, 60, 60, tk.SUNKEN, "#221FFE")
        self.computerlabel = egp.add_label(botframe, "", 2, 1, 60, 60, tk.SUNKEN, "#FE1F34")



    def load_resources(self):
        # Defining Assets and States
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
        assets = self.assets
        computer_choice = choice([0,1,2])

        result_text, winner = self.logic.get_result(user_choice, computer_choice)

        us = self.logic.user_score
        cs = self.logic.computer_score

        print(result_text, "Winner:", winner)

        self.userlabel.configure(image=assets['images'][user_choice])
        self.computerlabel.configure(image=assets['images'][computer_choice])

        self.result_display.delete('1.0', tk.END)
        self.result_display.insert(
            tk.END,
            f"Round {self.logic.round} \n" +
            f"Your chosen: {assets['names'][user_choice]} \n" +
            f"Computer's chosen: {assets['names'][computer_choice]} \n" +
            f"Your Score: {us} \n Computer Score: {cs}\n\n"
        )


    def create_widgets(self):
        self

    def grid(self):
        self

# Measured how many lines of code was reduced through modularization from the original file