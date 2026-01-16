import tkinter as tk

class EasyGridPacker:
    def __init__(self):
        self.root = None

    def setup_window(self, title, size):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)

    def add_input(self, text, padx=10, pady=5):
        frame = tk.Frame(master=self.root)
        tk.Label(master=frame, text=text).pack(size="left")
        entry = tk.Entry(frame)
        entry.pack(side="right",  fill="x", expand=True)
        frame.pack(fill="x", padx=padx, pady=pady)
        return entry
    
    def add_button(self, btn_text, command):
        btn = tk.Button(self.root, text=btn_text, command=command)
        btn.pack(pady=10)
        return btn
    
    def add_frame(self, side=tk.TOP, border=3):
        frame = tk.Frame(self.root, border=border)
        frame.pack(side=side)
        return frame
    
    def add_label(self, frame, text="",  c=0, r=0, padx=0, pady=0, relief=tk.SUNKEN, bg="#FFFFFF"):
        label = tk.Label(frame, text=text, padx=padx, pady=pady, relief=relief, bg=bg)
        label.grid(column = c, row = r)
        return label

# egp = EasyGridPacker()