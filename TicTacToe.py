import random

boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
HUMAN = 'X'
COMPUTER = '0'
first_player = HUMAN
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]


def print_board(initial=False):
    print(('''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        ''').format(*([x for x in range(1, 10)] if initial else boxes)))


def take_turn(player, turn):

    while True:
        if player is COMPUTER:
            box = get_computer_move()
        else:
            box = input('Player %s, type a number from 1-9 to select a box: ' % player)

            try:
                box = int(box) - 1  # subtract 1 to sync with boxes[] index numbers
            except ValueError:
                # Not an integer
                print('That\'s not a valid number, try again.\n')
                continue

        if box < 0 or box > 8:
            print('That number is out of range, try again.\n')
            continue

        if boxes[box] == ' ':  # initial value
            boxes[box] = player  # set to value of current player
            break
        else:
            print('That box is already marked, try again.\n')


def get_computer_move():
    return random.randint(0, 8)


def switch_player(turn):
    current_player = COMPUTER if turn % 2 == 0 else HUMAN
    return current_player


def check_for_win(player, turn):
    if turn > 4:  # need at least 5 moves before a win is possible
        for combo in winning_combos:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'win'

        if turn == 9:
            return 'tie'


def play(player, turn):
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result == 'win':
            print('Game over. %s wins!\n' % player)
            break
        elif result == 'tie':
            print('Game over. It\'s a tie.\n')
            break
        turn += 1
        player = switch_player(turn)


# Begin the game:
print('\n\nWelcome to Tic Tac Toe for two humans!')
print_board(initial=True)
play(first_player, turn)
