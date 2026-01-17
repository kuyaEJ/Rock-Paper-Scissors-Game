from components.rpsgame import GameLogic
from components.rpswindoweasygp import Window as rpswindowv2

print("Launching", __name__)
# __main__ is the interactive environment
# main is the command line environment
if __name__ == "__main__" or __name__ == "main":
    appv2 = rpswindowv2("Rock Paper Scissors Game version: 2", "800x600")
    logic = GameLogic()
    appv2.launch(logic)
    print("Launched main python")