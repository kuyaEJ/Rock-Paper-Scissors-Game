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
    
    def add_button(self, frame, command, text="", c=0, r=0, **kwargs):
        btn = tk.Button(frame, command=command, text=text, **kwargs)
        btn.grid(column=c, row=r)
        return btn
    
    def add_frame(self, side=tk.TOP, border=3, **kwargs):
        frame = tk.Frame(self.root, border=border, **kwargs)
        frame.pack(side=side)
        return frame
    
    def add_label(self, frame, text="",  c=0, r=0, padx=0, pady=0, relief=tk.FLAT, **kwargs):
        label = tk.Label(frame, text=text, padx=padx, pady=pady, relief=relief, **kwargs)
        label.grid(column = c, row = r)
        return label
    
    def add_text(self, frame,  c=0, r=0,height=24, width=80, **kwargs):
        text = tk.Text(frame, height=height, width=width, **kwargs)
        text.grid(column=c, row=r)
        return text

# egp = EasyGridPacker()