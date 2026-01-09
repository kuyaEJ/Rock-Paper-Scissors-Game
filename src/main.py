from components.rpsgame import GameLogic
from components.rpswindow import Window as rpswindow

print("Launching", __name__)
# __main__ is the interactive environment
# main is the command line environment
if __name__ == "__main__" or __name__ == "main":
    logic = GameLogic()
    app = rpswindow(logic)
    app.Window.mainloop()
    print("Launched main python")