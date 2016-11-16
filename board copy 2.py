
WHITE_PLAYER = 'W'
BLACK_PLAYER = 'B'
EMPTY_CELL = '.'

GAME_SCORING_MOST_PIECES = '>'
GAME_SCORING_LEAST_PIECES = '<'

DIRECTIONS = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1]
]


def get_opposite_player(player):
    """ Returns the opposite player."""
    if player == WHITE_PLAYER:
        return BLACK_PLAYER

    return WHITE_PLAYER


def create_initial_board_state(row_size, column_size, top_left)-> [[list]]:
    """ Creates the initial board state."""
    state = []
    for row in range(row_size):
        state.append([])
        for col in range(column_size):
            state[-1].append(EMPTY_CELL)

    state[int((row_size/2) - 1)][int((column_size/2) - 1)] = top_left
    state[int(row_size/2)][int((column_size/2) - 1)] = get_opposite_player(top_left)
    state[int((row_size/2) - 1)][int(column_size/2)] = get_opposite_player(top_left)
    state[int(row_size/2)][int(column_size/2)] = top_left

    return state


class Board(object):
    def __init__(self, row_size, column_size, player, top_left, game_scoring):
        """ Initialises the Class. """
        self.row_size = row_size
        self.column_size = column_size
        self.current_player = player
        self.top_left = top_left
        self.game_scoring = game_scoring
        self.board_state = create_initial_board_state(row_size, column_size, top_left)

    def count_number_of_pieces(self)-> tuple:
        """Counts the number of both black and white pieces. """
        black_pieces_count = 0
        white_pieces_count = 0
        for rows in self.board_state:
            for cell in rows:
                    if cell == BLACK_PLAYER:
                        black_pieces_count += 1
                    elif cell == WHITE_PLAYER:
                        white_pieces_count += 1
        return str(black_pieces_count), str(white_pieces_count)

    def determine_winner(self)-> str:
        """ Determines the winner based on how the user wanted the game to be won. """
        winner = None

        black, white = self.count_number_of_pieces()
        if self.game_scoring == GAME_SCORING_MOST_PIECES:
            if black > white:
                winner = BLACK_PLAYER
            elif white > black:
                winner = WHITE_PLAYER
        else:
            if white > black:
                winner = BLACK_PLAYER
            elif black > white:
                winner = WHITE_PLAYER

        return winner

    def is_cell_available(self, row: int, column: int)-> bool:
        """Checks to see if the given row and column combination is empty ot not. """
        return self.board_state[row][column] == EMPTY_CELL

    def is_valid_cell(self, row, column)-> bool:
        """Checks to see if the given row and column combination is on the board or not. """
        return -1 < row < self.row_size and -1 < column < self.column_size

    def is_game_over(self)->bool:
        """Checks to see if the game is over or not. """
        return (not self._has_valid_moves(self.current_player) and
                not self._has_valid_moves(get_opposite_player(self.current_player)))

    def is_valid_move(self, row, column):
        """Checks to see if the given move is valid or not. """
        return (self.is_valid_cell(row, column) and self.is_cell_available(row, column)
                and len(self.get_flipped_items(row, column, self.current_player)) > 0)

    def get_flipped_items(self, row, column, player)-> list:
        """ Gets items that need to flipped. """
        if not self.is_cell_available(row, column):
            return []
        opposite_player = get_opposite_player(player)
        flip_list = []

        for direction in DIRECTIONS:
            found_opponent_piece = False
            current_row = row + direction[0]
            current_column = column + direction[1]
            current_flip_list = []

            while self.is_valid_cell(current_row, current_column):
                if self.board_state[current_row][current_column] == opposite_player:
                    found_opponent_piece = True
                    current_flip_list.append([current_row, current_column])
                    current_row += direction[0]
                    current_column += direction[1]
                elif self.board_state[current_row][current_column] == player:
                    if found_opponent_piece:
                        flip_list.extend(current_flip_list)
                    break
                else:
                    break
        return flip_list

    def has_valid_moves(self)->bool:
        """Checks to see if there are valid moves. """
        return self._has_valid_moves(self.current_player)

    def _has_valid_moves(self, player)->bool:
        """ Checks to see if a given player has valid moves. """
        for row in range(self.row_size):
            for column in range(self.column_size):
                flip_list = self.get_flipped_items(row, column, player)
                if len(flip_list) > 0:
                    return True

        return False

    def flip_tiles(self, flip_list)-> list:
        """Flips the items that need to be flipped. """
        for element in flip_list:
            self.board_state[element[0]][element[1]] = self.current_player

    def apply_move(self, row, column):
        """Applies the move. """
        items = self.get_flipped_items(row, column, self.current_player)
        self.board_state[row][column] = self.current_player
        self.flip_tiles(items)

        opposite_player = get_opposite_player(self.current_player)
        if self._has_valid_moves(opposite_player):
            self.current_player = opposite_player
