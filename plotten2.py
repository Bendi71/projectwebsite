import matplotlib.pyplot as plt
import numpy as np

def plot_connect4(board, filename='Pics/connect4.png'):
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.set_aspect('equal')
    ax.set_xticks(np.arange(0.5, 7.5, 1))
    ax.set_yticks(np.arange(0.5, 6.5, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which='both', color='black', linestyle='-', linewidth=2)

    for row in range(6):
        for col in range(7):
            cell = board[row * 7 + col]
            if cell == 'X':
                color = 'red'
            elif cell == 'O':
                color = 'yellow'
            else:
                color = 'white'
            circle = plt.Circle((col, 5 - row), 0.4, color=color, ec='black', lw=2)
            ax.add_patch(circle)

    plt.xlim(-0.5, 6.5)
    plt.ylim(-0.5, 5.5)
    plt.gca()
    plt.savefig(filename)
    plt.close()

# Example usage
board = [
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', 'X', ' ', 'O', 'X', ' ', ' ',
    ' ', 'O', 'O', 'X', 'X', ' ', ' ',
    'X', 'O', 'X', 'O', 'X', 'O', ' '
]
plot_connect4(board)