import tkinter as tk

class EasyGridPacker:
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)

    def add_input(self, label_text):
        frame = tk.Frame(master=self.root)
        tk.Label(master=frame, text=label_text).pack(size="left")
        entry = tk.Entry(frame)
        entry.pack(side="right",  fill="x", expand=True)
        frame.pack(fill="x", padx=10, pady=5)
        return entry
    
    def add_button(self, text, command):
        btn = tk.Button(self.root, text=text, command=command)
        btn.pack(pady=10)
        return btn