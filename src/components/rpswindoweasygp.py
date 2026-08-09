import tkinter as tk
from random import choice
from components.easygp import EasyGridPacker
import os

class Window:
    def __init__(self, title, size):
        self.egp = EasyGridPacker()
        self.egp.setup_window(title, size)
    
    def launch(self, logic):
        self.logic = logic
        self.setup_layout()
        self.load_resources()
        self.create_widgets()
        self.mainframe.grid_columnconfigure(1, weight=1)
        self.egp.root.mainloop()


    def setup_layout(self):
        # Top Frame
        self.mainframe = self.egp.add_frame(border=3)

        # Display Label
        self.egp.add_label(self.mainframe, "Try to win against the Computer", 2, 0)

        # Bottom Frame
        self.botframe = self.egp.add_frame(tk.BOTTOM)
        self.botframe.grid_columnconfigure(1, weight=1)
        # User Label
        self.userlabel = self.egp.add_label(self.botframe, text="", c=0, r=1, padx=60, pady=60, relief=tk.SUNKEN, bg="#221FFE")
        # Create and Grid the Results Display
        self.result_display = self.egp.add_text(self.botframe, c=1, r=1, height=12, width=30, bg="#FFDAC1")
        # Computer Label
        self.computerlabel = self.egp.add_label(self.botframe, text="", c=2, r=1, padx=60, pady=60, relief=tk.SUNKEN, bg="#FE1F34")



    def load_resources(self):
        # Defining Assets and States
        # IMPORTANT: Do not change the order of items since are dependent tables
        # TO-DO: Find solution of tables being dependent since it is risky
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_script_dir)
        assets_path = os.path.join(project_root, "assets")

        self.assets = {
            'images': [
                tk.PhotoImage(file=os.path.join(assets_path, "rock.png"), master=self.egp.root).subsample(2),
                tk.PhotoImage(file=os.path.join(assets_path, "paper.png"), master=self.egp.root).subsample(2),
                tk.PhotoImage(file=os.path.join(assets_path, "scissor.png"), master=self.egp.root).subsample(2)
            ],
            'names': ['rock', 'paper', 'scissor']
        }

        self.buttons = {}




    def play(self, user_choice):

        # Shorten variables
        assets = self.assets
        computer_choice = choice([0,1,2])

        # Update scores and let the computer choose a random choice
        result_text, winner = self.logic.get_result(user_choice, computer_choice)

        # Create local variables to shorten syntax in reference
        us = self.logic.user_score
        cs = self.logic.computer_score

        # Consdering logging in a different way with decorator functions
        print(result_text, "Winner:", winner)

        self.userlabel.configure(image=assets['images'][user_choice])
        self.computerlabel.configure(image=assets['images'][computer_choice])
        
        # Clear result display then insert new score and display feed
        self.result_display.delete('1.0', tk.END)
        self.result_display.insert(
            tk.END,
            f"Round {self.logic.round} \n" +
            f"Your choice: {assets['names'][user_choice]} \n" +
            f"Computer's choice: {assets['names'][computer_choice]} \n" +
            f"Your Score: {us} \nComputer Score: {cs}\n\n"
        )




    def create_widgets(self):
        # Create, grid, and place buttons in self.ui table
        for i, name in enumerate(self.assets['names']):
            self.buttons[f'btn_{name}'] = self.egp.add_button(
                frame=self.mainframe, 
                command=lambda x=i: self.play(x),
                text="", 
                c=i+1,
                r=1,
                image=self.assets['images'][i],
            )

# Measured how many lines of code was reduced through modularization from the original file