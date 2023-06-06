import tkinter
from tkinter import *

row_arg = 5
def table(rank_arg, player_arg, score_arg,root):
    """A function for displaying the leaderboard high scores"""
    global row_arg
    row_arg += 1
    rank_1 = Label(root, text=rank_arg, textvariable=rank_arg, bg="#002952", fg="white", font=('algerian', 20))
    rank_1.grid(row=row_arg, column="1", padx="70", pady="20")
    player_1 = Label(root, text=player_arg, textvariable=player_arg, bg="#002952", fg="white", font=('algerian', 20))
    player_1.grid(row=row_arg, column="2", padx="70", pady="20")
    score_1 = Label(root, text=score_arg, textvariable=score_arg, bg="#002952", fg="white", font=('algerian', 20))
    score_1.grid(row=row_arg, column="3", padx="70", pady="20")

# Creating Window








