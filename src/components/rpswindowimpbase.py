import tkinter as tk
from random import choice
from components.basewindow import Window
from components.easygp import EasyGridPacker as egp

class Window(Window):
    def setup_window(self, window_title):
        self.packer = egp(title=window_title)

    def setup_layout(self):
        self.mainframe = self.packer.add_frame(tk.TOP)
        self.packer.add_label(self.mainframe, text="Try to win against the Computer")
        self.botframe = self.packer.add_frame(tk.BOTTOM)
        self.labelusergrid = self.packer.add_label(self.botframe, 0, 1, "")
        self.labelusergrid.configure(padx=60, pady=60, relief=tk.SUNKEN, bg="#221FFE")
        self.labelcomputergrid = self.packer.add_label(self.botframe, 2, 1, "")
        self.labelcomputergrid.configure(padx=60, pady=60, relief=tk.SUNKEN, bg="#FE1F34")

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

        self.labelusergrid.configure(image=assets['images'][user_choice])
        self.labelcomputergrid.configure(image=assets['images'][computer_choice])

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