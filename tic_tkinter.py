import tkinter as tk
from tkinter import messagebox

# ---------------- Game Setup ----------------
ps1 = "X"
ps2 = "O"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("360x420")
        self.root.resizable(False, False)

        self.matrix = [[-1]*3 for _ in range(3)]
        self.turn = ps1

        self.create_start_screen()

    # ---------------- Start Screen ----------------
    def create_start_screen(self):
        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack(pady=40)

        tk.Label(self.start_frame, text="Tic Tac Toe", font=("Arial", 20, "bold")).pack(pady=10)

        tk.Label(self.start_frame, text="Player 1 Name (X)").pack()
        self.p1_entry = tk.Entry(self.start_frame)
        self.p1_entry.pack(pady=5)

        tk.Label(self.start_frame, text="Player 2 Name (O)").pack()
        self.p2_entry = tk.Entry(self.start_frame)
        self.p2_entry.pack(pady=5)

        tk.Button(self.start_frame, text="Start Game", command=self.start_game).pack(pady=15)

    def start_game(self):
        self.pl1 = self.p1_entry.get() or "Player 1"
        self.pl2 = self.p2_entry.get() or "Player 2"
        self.start_frame.destroy()
        self.create_game_board()

    # ---------------- Game Board ----------------
    def create_game_board(self):
        self.status = tk.Label(self.root, text=f"{self.pl1}'s Turn (X)", font=("Arial", 12))
        self.status.pack(pady=10)

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.buttons = [[None]*3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Arial", 20, "bold"),
                    width=5,
                    height=2,
                    command=lambda r=i, c=j: self.place(r, c)
                )
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        tk.Button(self.root, text="Restart", command=self.reset_game).pack(pady=10)

    # ---------------- Game Logic ----------------
    def place(self, r, c):
        if self.matrix[r][c] != -1:
            return

        self.matrix[r][c] = self.turn
        self.buttons[r][c].config(text=self.turn)

        if self.won(self.turn):
            winner = self.pl1 if self.turn == ps1 else self.pl2
            messagebox.showinfo("Game Over", f"{winner} wins! 🎉")
            self.disable_board()
            return

        if self.is_draw():
            messagebox.showinfo("Game Over", "Draw!!!")
            return

        self.turn = ps2 if self.turn == ps1 else ps1
        player = self.pl1 if self.turn == ps1 else self.pl2
        self.status.config(text=f"{player}'s Turn ({self.turn})")

    def row(self, s):
        return any(all(self.matrix[i][j] == s for j in range(3)) for i in range(3))

    def col(self, s):
        return any(all(self.matrix[i][j] == s for i in range(3)) for j in range(3))

    def diag(self, s):
        return all(self.matrix[i][i] == s for i in range(3)) or \
               all(self.matrix[i][2-i] == s for i in range(3))

    def won(self, s):
        return self.row(s) or self.col(s) or self.diag(s)

    def is_draw(self):
        return all(self.matrix[i][j] != -1 for i in range(3) for j in range(3))

    def disable_board(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def reset_game(self):
        self.matrix = [[-1]*3 for _ in range(3)]
        self.turn = ps1
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state="normal")
        self.status.config(text=f"{self.pl1}'s Turn (X)")


# ---------------- Run App ----------------
if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()