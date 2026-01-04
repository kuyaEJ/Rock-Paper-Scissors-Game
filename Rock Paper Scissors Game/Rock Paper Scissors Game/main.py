from RPSLogic import GameLogic
from RPSWindow import Window

if __name__ == "main":
    logic = GameLogic()
    app = Window(logic)
    app.window.mainloop()