import tkinter as tk

class CardButton(tk.Button):

    def __init__(self, parent, card, command):
        super().__init__(
            parent,
            text="?",
            width=6,
            height=3,
            font=("Arial", 24),
            command=command
        )

        self.card = card

    def flip(self):
        self.config(text=self.card.value)