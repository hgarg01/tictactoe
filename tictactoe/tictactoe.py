# write your code here
import random
import copy
#define matrix from user input
def define_matrix(board):
    board = [x if x != "_" else " " for x in board]
    i = 0
    matrix = []
    while i < 9:
        matrix.append([board[i], board[i+1], board[i+2]])
        i += 3
    return matrix

#print board with the given matrix
def print_matrix(matrix):
    print("-" * 9)
    for i in range(3):
        print("| {} {} {} |".format(matrix[i][0], matrix[i][1], matrix[i][2]))
    print("-" * 9)

#check if given moves are valid and within range
def check_moves(x_cord, y_cord, matrix):
    if not x_cord.isdigit() or not y_cord.isdigit():
        print("You should enter numbers!")
        return False
    x = int(x_cord)
    y = int(y_cord)
    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    if matrix[abs(y-3)][abs(x-1)] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    return True

#find which player's move is it next
def next_move(matrix):
    x_counts = sum(x.count("X") for x in matrix)
    o_counts = sum(x.count("O") for x in matrix)
    if x_counts > o_counts:
        return "O"
    else:
        return "X"

def next_next_move(matrix):
    x_counts = sum(x.count("X") for x in matrix)
    o_counts = sum(x.count("O") for x in matrix)
    if x_counts >= o_counts:
        return "X"
    else:
        return "O"


#check if 3 in a row
def row_check(matrix):
    for i in range(3):
        if matrix[i][0] == matrix[i][1]  == matrix[i][2] != " ":
            return matrix[i][0]

#check if 3 in column
def col_check(matrix):
    for j in range(3):
        if matrix[0][j] == matrix[1][j] == matrix[2][j] != " ":
            return matrix[0][j]

#check if win in diagonals
def diagonal_check(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != " ":
        return matrix[1][1]

def check_status(matrix):
    if row_check(matrix) :
        return True
    elif col_check(matrix):
        return True
    elif diagonal_check(matrix):
        return True
    else:
        return False

#check status of the game
def check_status_and_print(matrix):
    space_count = sum(x.count(" ") for x in matrix)
    #print(space_count)
    if row_check(matrix) :
        print("{} wins".format(row_check(matrix)))
        return True
    elif col_check(matrix):
        print("{} wins".format(col_check(matrix)))
        return True
    elif diagonal_check(matrix):
        print("{} wins".format(diagonal_check(matrix)))
        return True
    elif space_count == 0:
        print("Draw")
        return True
    else:
        return False

def computer_move_easy(matrix, str):
    global turn
    x = random.randint(1,3)
    y = random.randint(1,3)
    while matrix[abs(y-3)][abs(x-1)] != " ":
        x = random.randint(1,3)
        y = random.randint(1,3)
    print('Making move level "{}"'.format(str))
    matrix[abs(y-3)][abs(x-1)] = next_move(matrix)
    print_matrix(matrix)

def computer_move_medium(matrix):
    done = False
    #find 2 in a row
    for i in range(3):
        space_counts = sum(i.count(" ") for i in matrix[i])
        x_counts = sum(i.count("X") for i in matrix[i])
        o_counts = sum(i.count("O") for i in matrix[i])
        if space_counts == 1 and (x_counts  == 2 or o_counts == 2):
                place = matrix[i].index(" ")
                matrix[i][place] = next_move(matrix)
                print('Making move level "medium"')
                print_matrix(matrix)
                return
    #search 2 in column
    for i in range(3):
        col = [val[i] for val in matrix]
        space_counts = col.count(" ")
        x_counts = col.count("X")
        o_counts = col.count("O")
        if space_counts == 1 and (x_counts  == 2 or o_counts == 2):
                place = col.index(" ")
                matrix[place][i] = next_move(matrix)
                print('Making move level "medium"')
                print_matrix(matrix)
                return
    #search in diagonals[
    diagonal1 = [matrix[i][i] for i in range(3)]
    space_counts, x_counts, o_counts = diagonal1.count(" "), diagonal1.count("X"), diagonal1.count("O")
    if space_counts == 1 and (x_counts  == 2 or o_counts == 2):
                place = diagonal1.index(" ")
                matrix[place][place] = next_move(matrix)
                print('Making move level "medium"')
                print_matrix(matrix)
                return
    #search in diagonal 2
    diagonal2 = [matrix[i][2-i] for i in range(3)]
    space_counts, x_counts, o_counts = diagonal2.count(" "), diagonal2.count("X"), diagonal2.count("O")
    if space_counts == 1 and (x_counts  == 2 or o_counts == 2):
                place = diagonal2.index(" ")
                matrix[place][2-place] = next_move(matrix)
                print('Making move level "medium"')
                print_matrix(matrix)
                return
    computer_move_easy(matrix,"med")

def user_move(matrix):
    global turn
    valid  = False
    while not valid:
        print("Enter the coordinates")
        ip = input().split()
        if len(ip) != 2 or not all(x.isdigit() for x in ip):  #condition for checking 1 input by user instead of 2
            print("You should enter numbers!")
        else:
             x, y = ip[0], ip[1]
             valid = check_moves(x, y, matrix)

    x,y = int(x), int(y)
    #save value in matrix
    matrix[abs(y-3)][abs(x-1)] = next_move(matrix)
    print_matrix(matrix)
    #space_count = sum(x.count(" ") for x in matrix)
    #if space_count > 0:
    #    turn = "easy"

def print_main_menu():
    command = input("Input command:").split()
    print(command)
    #if command[0] == "exit":
     #   return "exit", None, None
    #else :
    while command[0] != "exit":
            if command[0].isdigit():
                print("Invalid command!")
                command = input("Input command:").split()
            elif len(command) != 3 :
                print("Bad parameters!")
                command = input("Input command:").split()
            elif (command[1] != "user" and command[1] != "easy" and command[1] != "medium") or (command[2] != "user" and command[2] != "easy" and command[2] != "medium") :
                print("Bad parameters!")
                command = input("Input command:").split()
            else:
                return "start", command[1], command[2]
    return "exit", None, None

#initialize the board
start_board = " " * 9
matrix = define_matrix(start_board)


command, first_player, second_player = print_main_menu()
while command != "exit":
    move = first_player
    turn = 1
    while not check_status_and_print(matrix):
        if move == "user":
            user_move(matrix)
        elif move == "easy":
            computer_move_easy(matrix, "easy")
        elif move == "medium":
            computer_move_medium(matrix)
        turn += 1
        if turn % 2 == 1 :
            move = first_player
        else:
            move = second_player
    command, first_player, second_player = print_main_menu()
    start_board = " " * 9
    matrix = define_matrix(start_board)

