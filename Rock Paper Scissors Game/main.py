from RPSLogic import GameLogic
from RPSWindow import Window

print("Launching", __name__)
# __main__ is the interactive environment
# main is the command line environment
if __name__ == "__main__" or __name__ == "main":
    logic = GameLogic()
    app = Window(logic)
    app.window.mainloop()
    print("Launched main python")