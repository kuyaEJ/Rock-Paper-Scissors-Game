from components.rpsgame import GameLogic
from components.rpswindoweasygp import Window as rpswindow

print("Launching", __name__)
# __main__ is the interactive environment
# main is the command line environment
if __name__ == "__main__" or __name__ == "main":
    app = rpswindow("Rock Paper Scissors Game", "800x600")
    logic = GameLogic()
    app.launch(logic)
    print("Launched main python")