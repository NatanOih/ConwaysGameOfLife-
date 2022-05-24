# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.
from colorama import Fore, Back, Style
from board import Board

def main():
    user_rows = int(input('how manu rows?'))
    user_columns = int(input('how manu columns?'))
    print("note:  " + Fore.GREEN + "∎" + Style.RESET_ALL + " = alive\t " + Fore.BLACK + '∎' + Style.RESET_ALL +"= dead")
    game_of_life_board = Board(user_rows, user_columns) #creating a random board
    game_of_life_board.draw_board() #drawing the board
    user_action = ''

    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()

main()