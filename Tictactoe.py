import numpy as np, random

#create board 3x3 matrix with zeroes
#3x3'lük 0'lardan oluşan bir matris
def create_board():
    board = np.zeros((3,3), dtype=int)
    return board
create_board()

#place player value to selected position
#seçilen pozisyona oyuncu numarasını ekler
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

board = create_board()
place(board, 1, (0, 0))


def possibilities(board):
    a = np.where(board == 0)
    return a

#place player value to random position
#rastgele seçilen bir noktayı işaretler
def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board

random_place(board, 2)

for i in range(3):
    for player in [1, 2]:
        random_place(board, player)

print(board)

#Satır olarak kazananı kontrol eder
def row_win(board, player):
    if np.any(np.all(board==player, axis=1)): # this checks if any row contains all positions equal to player.
        return True
    else:
        return False

row_win(board, 1) # Does Player 1 have a complete row?

#Sütun olarak kazananı kontrol eder
def col_win(board, player):
    if np.any(np.all(board==player, axis=0)): # this checks if any column contains all positions equal to player
        return True
    else:
        return False

col_win(board, 1) # Does Player 1 have a complete column?

#Çapraz olarak kazananı kontrol eder
def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False

diag_win(board, 2) # Does Player 2 have a complete diagonal?

#If one of them has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

results = [play_game() for i in range(1000)]
results.count(1)

#Player 1 always starts with the middle square, and otherwise both players place their markers randomly.
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

results = [play_strategic_game() for i in range(1000)]
results.count(1)








