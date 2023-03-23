import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.turn = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[0]*3 for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.master,
                                                   text="",
                                                   font=("Helvetica", 40),
                                                   width=3,
                                                   height=1,
                                                   command=lambda row=row, col=col: self.button_click(row, col))
                self.buttons[row][col].grid(row=row, column=col)

        self.restart_button = tk.Button(self.master,
                                        text="Restart",
                                        font=("Helvetica", 16),
                                        width=6,
                                        command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3)

        self.turn_label = tk.Label(self.master,
                                   text=f"Turn: {self.turn}",
                                   font=("Helvetica", 16))
        self.turn_label.grid(row=4, column=0, columnspan=3)

    def button_click(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)
            self.check_winner()
            self.change_turn()

    def check_winner(self):
        # Check for horizontal matches
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                self.declare_winner(self.board[row][0])
                return
        
        # Check for vertical matches
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                self.declare_winner(self.board[0][col])
                return
        
        # Check for diagonal matches
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.declare_winner(self.board[0][0])
            return
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.declare_winner(self.board[0][2])
            return
        
        # No winner yet
        if all([all(row) for row in self.board]):
            self.declare_winner(None)
            return

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        self.turn_label.config(text=f"Turn: {self.turn}")

    def restart_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
                self.board[row][col] = ''
        self.turn = 'X'
        self.turn_label.config(text=f"Turn: {self.turn}")

    def declare_winner(self, winner):
        if winner:
            messagebox.showinfo("Winner!", f"{winner} has won the game!")
        else:
            messagebox.showinfo("Draw!", "The game is a draw.")
        self.restart_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
