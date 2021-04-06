import os


class TicTacGame:
    def start_game(self):
        self.crosses_move = True
        self.make_field()
        self.game_cycle()

    def end_game(self, winner):
        self.print_field()
        if winner == 'filled':
            print('\nDraw!')
        else:
            print(f"\n{'Crosses' if winner == 'X' else 'Zeros'} win!")
        print('\nenter any word...')
        input()

    def game_cycle(self):
        while True:
            # clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
            winner = self.check_winner()
            if winner is not None:
                self.end_game(winner)
                return
            self.print_field()

            print("Use two numbers (e.g. '1 2') to choose position\n")
            if self.crosses_move:
                print('\nCrosses move:')
            else:
                print('\nZeros move:')

            correct = False
            while not correct:
                inp = input()
                correct, *row_column = self.get_input(inp)
            row, column = row_column

            self.field[row][column] = 'X' if self.crosses_move else 'O'
            self.crosses_move = not self.crosses_move

    def get_input(self, inp):
        avail = ('0', '1', '2')

        inp = inp.split(' ')

        if len(inp) == 2 and inp[0] in avail and inp[1] in avail:
            row, column = map(int, inp)
            if self.field[row][column] == ' ':
                return (True, row, column)
            else:
                print('This position taken')
                return (False, )
        else:
            print("Use two numbers (e.g. '1 2') to choose position")
            return (False, )

    def check_winner(self):
        field = self.field
        for coord in range(3):
            # check rows
            if field[coord][0] == field[coord][1] == field[coord][2] \
                    and field[coord][coord] != ' ':
                return field[coord][coord]
            # check columns
            if field[0][coord] == field[1][coord] == field[2][coord] \
                    and field[coord][coord] != ' ':
                return field[coord][coord]

        # check diagonals
        if field[0][0] == field[1][1] == field[2][2] and field[1][1] != ' ':
            return field[1][1]
        if field[0][2] == field[1][1] == field[2][0] and field[1][1] != ' ':
            return field[1][1]

        res = 'filled'
        for row in field:
            for elem in row:
                if elem == ' ':
                    res = None

        return res

    def make_field(self):
        self.field = [[' '] * 3 for row in range(3)]

    def print_field(self):
        print('\n\n       0      1      2')
        for row in range(3):
            lines = ['     ',
                     '    ' + str(row),
                     '     ',
                     '     ______|______|______' if row < 2 else
                     '           |      |']

            for col in range(3):
                elem = self.field[row][col]
                if elem == 'O':
                    lines[0] += '  __  '
                    lines[1] += ' |  | '
                    lines[2] += ' |__| '
                elif elem == 'X':
                    lines[0] += '      '
                    lines[1] += r'  \/  '
                    lines[2] += r'  /\  '
                else:
                    for nmb in range(3):
                        lines[nmb] += '      '
                if col < 2:
                    for nmb in range(3):
                        lines[nmb] += '|'

            for line in lines:
                print(line)
        print('\n')


if __name__ == '__main__':
    game = TicTacGame()
    while True:
        game.start_game()
