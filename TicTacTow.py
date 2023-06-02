import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

def announceWinner(player):
    if player == 'Draw':
        message = "It's a draw!"
    else:
        message = f'Player {player} wins'
    messagebox.showinfo('Game Over', message)
    resetGame()

def resetGame():
    global game, currentPlayer
    game = [['', '', ''] for _ in range(3)]
    currentPlayer = 'X'
    for row in buttons:
        for button in row:
            button.configure(text='')

def makeMove(row, col):
    global currentPlayer

    if game[row][col] == '':
        game[row][col] = currentPlayer
        buttons[row][col].configure(text=currentPlayer)
        checkWinner()
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'

def checkWinner():
    winningComb = (game[0], game[1], game[2],
                   [game[i][0] for i in range(3)],
                   [game[i][1] for i in range(3)], 
                   [game[i][2] for i in range(3)],
                   [game[i][i] for i in range(3)],
                   [game[i][2 - i] for i in range(3)])
    for combination in winningComb:
        if combination[0] == combination[1] == combination[2] != '':
            announceWinner(combination[0])
    if all(game[i][j] != '' for i in range(3) for j in range(3)):
        announceWinner('Draw')

window = tk.Tk()
window.title("Tic Tac Toe")
style = Style(theme='darkly')

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = ttk.Button(window, text='', width=5, command=lambda i=i, j=j: makeMove(i,j))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

game = [['', '', ''] for _ in range(3)]
currentPlayer = 'X'

window.mainloop()
