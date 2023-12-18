""" def Sum(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    return sum
print("Sum of integers from 1 to 10 is",Sum(1,10))
print("Sum of integers from 20 to 37 is",Sum(20,37))
print("Sum of integers from 35 to 49 is",Sum(35,49)) """
""" import math
def isValid(side1, side2, side3):
    if (side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1:
        return True
    else: return False
def area(side1, side2, side3):
    if(isValid==True):
        half_parameter=(side1+side2+side3)/2
        area=math.sqrt(half_parameter*(half_parameter-side1)*(half_parameter-side2)*(half_parameter-side3))
        print("The area of the triangle is",round(area,2))
    else:
        print("Inputs are invalid")

a,b,c=eval(input("Enter 3 side of triangle:"))
area(a,b,c) """
""" def rectangle(m,n):
    for i in range(m):
        for j in range(n):
            print("*",end="")
        print()
rectangle(2,4)
print() 
def triangle(rows):
    for i in range(rows): 
        print(" "*(rows-i)+"*"*(2*i+1),end="")
        print()
triangle(5) """
def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    # Kiểm tra hàng và cột
    for i in range(10):
        if all(board[i][j] == player for j in range(10)) or all(board[j][i] == player for j in range(10)):
            return True

    # Kiểm tra đường chéo chính
    if all(board[i][i] == player for i in range(10)):
        return True

    # Kiểm tra đường chéo phụ
    if all(board[i][9 - i] == player for i in range(10)):
        return True

    return False

def is_valid_move(board, row, col):
    return 0 <= row < 10 and 0 <= col < 10 and board[row][col] == ' '

def play_game():
    board = [[' ' for _ in range(10)] for _ in range(10)]
    players = ['O', 'X']
    current_player = 0

    while True:
        print_board(board)

        player_choice = input(f"Player {players[current_player]}, enter your move (row col): ")
        try:
            row, col = map(int, player_choice.split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if is_valid_move(board, row, col):
            board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            current_player = 1 - current_player  # Switch to the other player
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
