import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.window, text=" ", font=("Arial", 40),
                    width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.buttons
        for i in range(3):
            # Check rows and columns
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] != " ":
                return True
            if b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] != " ":
                return True

        # Check diagonals
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != " ":
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != " ":
            return True

        return False

    def is_full(self):
        return all(self.buttons[row][col]["text"] != " " for row in range(3) for col in range(3))

    def reset_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = " "
        self.current_player = "X"

if __name__ == "__main__":
    TicTacToe()
