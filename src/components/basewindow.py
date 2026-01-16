from abc import ABC, abstractmethod

class Window:
    def __init__(self, logic):
        self.logic = logic
        self.setup_window()
        self.setup_layout()
        self.load_resources()
        self.create_widgets()
        self.grid()

    
    @abstractmethod
    def setup_window(self):
        """All windows must define how it builds its root tk function"""
        pass

    @abstractmethod
    def setup_layout(self):
        """All windows must define how the frame layout is configured"""
        pass


    @abstractmethod
    def load_resources(self):
        """All windows must define how it loads its assets"""
        pass


    @abstractmethod
    def play(self, user_choice):
        """All windows must define logic when events occur"""
        pass

    @abstractmethod
    def create_widgets(self):
        """All windows must define how they build their widgets"""
        pass


    @abstractmethod
    def grid(self):
        """All windows must define how they grid their ui buttons, ui labels, and assets"""
        pass