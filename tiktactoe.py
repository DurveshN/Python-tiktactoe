def display_board(board):
    print("Current position of board \n\n")
    for i in range(0, 9):
        if i > 0 and i % 3 == 0:
            print("\n")
        if board[i] == 0:
                print("_", end=" ")
        elif board[i] == -1:
                print("O", end=" ")
        else:
                print("X", end=" ")
    print("\n\n")
    return 0

def analyse_board(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if (board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]] and board[cb[i][1]] == board[cb[i][2]]):
            return board[cb[i][0]]
    return 0


def minmax(board, player):
    x = analyse_board(board)
    if (x != 0):
        return (x*player)
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minmax(board, player*-1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value


def ai_turn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1


def user1(board):
    display_board(board)
    pos = 0
    pos = int(input("Enter which position you want to put O (1,2,3,...9) : "))
    if board[pos-1] == 1 or board[pos-1] == -1 :
        print("Wrong move")
        pos = int(input("Enter which position you want to put O (1,2,3,...9) : "))
        board[pos-1] = -1
    else:
        board[pos-1] = -1


def user2(board):
    display_board(board)
    pos = 0
    pos = int(input("Enter which position you want to put O (1,2,3,...9) : "))
    if board[pos-1] == 1 or board[pos-1] == -1 :
        print("Wrong move")
        pos = int(input("Enter which position you want to put O (1,2,3,...9) : "))
        board[pos-1] = 1
    else:
        board[pos-1] = 1


def main():
    choice = 0
    choice = int(input("Press 1 for Single player or 2 for Multiplayer :"))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if choice == 1:
        print("You are : O and computer is : X ")
        player = int(input("Enter to play 1st or 2nd : "))
        for i in range(0, 9):
            if analyse_board(board) != 0:
                break
            else:
                if ((i+player) % 2 != 0):
                    display_board(board)
                    pos = 0
                    pos = int(input("Enter which position you want to put O (1,2,3,...9) : "))
                    if board[pos-1] == 1 or board[pos-1] == -1 :
                        print("Wrong move")
                        pos = int(input("Enter which position you want to put O (1,2,3,...9) : "))
                        board[pos-1] = -1
                    else:
                        board[pos-1] = -1
                else:
                    ai_turn(board)
        if analyse_board(board) == -1:
            display_board(board)
            print("You won")
        elif analyse_board(board) == 1:
            display_board(board)
            print("Computer won")
        else:
            display_board(board)
            print("It is draw")
    else:
        print("User1 is : O and User2 is : X ")
        for i in range(0, 9):
            if analyse_board(board) != 0:
                    break
            else:
                if i % 2 == 0:
                    user1(board)
                else:
                    user2(board)
        if analyse_board(board) == -1:
            display_board(board)
            print("User1 won")
        elif analyse_board(board) == 1:
            display_board(board)
            print("user2 won")
        else:
            display_board(board)
            print("It is draw")
main()


