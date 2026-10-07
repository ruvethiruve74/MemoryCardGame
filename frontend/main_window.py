import tkinter as tk

from game import MemoryGame
from frontend.card_button import CardButton

class MainWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Memory Card Game")
        self.window.geometry("600x600")
        self.game = MemoryGame()
        self.buttons = []
        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for index, card in enumerate(self.game.cards):
            row = index // 4
            col = index % 4

            button = CardButton(
                self.window,
                card,
                lambda c=card: self.card_clicked(c)
            )

            button.grid(
                row=row,
                column=col,
                padx=10,
                pady=10
            )

            self.buttons.append(button)

    def card_clicked(self, card):

        print("Card clicked:", card.value)

        
