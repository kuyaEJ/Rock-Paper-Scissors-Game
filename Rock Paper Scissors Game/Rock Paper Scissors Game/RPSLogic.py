import random
import tkinter as tk
import os


class GameLogic:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.round = 0

    def get_result(self, user_choice, computer_choice):
        result_text = ""
        winner = "No one"

        if user_choice == computer_choice:
            result_text = "Tie"
            winner = "No one"
        elif (user_choice - computer_choice) % 3 == 1:
            result_text = "You win"
            winner = "User"
            self.user_score += 1
        else:
            result_text = "Comp wins"
            winner = "Computer"
            self.computer_score += 1

        self.round += 1
        return result_text, winner