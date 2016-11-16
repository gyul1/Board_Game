
import tkinter
from board import Board

DEFAULT_FONT = ('Helvetica', 14)
MAIN_FONT = ('Helvetica', 20)


class BoardSetupDialog:
    def __init__(self):
        """ Initializes the class"""
        self._dialog_window = tkinter.Toplevel()

        board_setup = tkinter.Label(
            master = self._dialog_window, text = 'BOARD SETUP',
            font = DEFAULT_FONT)

        board_setup.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_size = tkinter.Label(
            master = self._dialog_window, text = 'Number of Rows: ',
            font = DEFAULT_FONT)

        row_size.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)

        self._row_size_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._row_size_entry.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        col_size = tkinter.Label(
            master = self._dialog_window, text = 'Number of Columns: ',
            font = DEFAULT_FONT)

        col_size.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)

        self._col_size_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._col_size_entry.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)

        starting_turn = tkinter.Label(
            master = self._dialog_window, text = 'Starting Turn("B" or "W"): ',
            font = DEFAULT_FONT)

        starting_turn.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W  + tkinter.N )

        self._starting_turn_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._starting_turn_entry.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)

        top_left = tkinter.Label(
            master = self._dialog_window, text = 'Upper-left Piece ("B" or "W"): ',
            font = DEFAULT_FONT)

        top_left.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)

        self._top_left_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._top_left_entry.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)

        how_game_is_won = tkinter.Label(
            master = self._dialog_window, text = 'How game is won (">" or "<"): ',
            font = DEFAULT_FONT)

        how_game_is_won.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.N)

        self._how_game_is_won_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT_FONT)

        self._how_game_is_won_entry.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E + tkinter.N)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 6, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 6, column = 1, padx = 10, pady = 10)
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)
        self._dialog_window.rowconfigure(6, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)



        self._ok_clicked = False
        self._row_size = ''
        self._col_size = ''
        self._starting_turn = ''
        self._top_left = ''
        self._how_game_is_won = ''

    def show(self) -> None:

        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        """ Returns whether the ok button was clicked """
        return self._ok_clicked

    def get_row_size(self) -> str:
        """ Gets the row size. """
        return self._row_size

    def get_col_size(self) -> str:
        """ Gets the colomn size. """
        return self._col_size

    def get_starting_color(self)-> str:
        """ Gets the starting color. """
        return self._starting_turn

    def get_top_left(self)-> str:
        """ Gets the top left piece. """
        return self._top_left

    def get_how_game_is_won(self)-> str:
        """Gets how game is won. """
        return self._how_game_is_won

    def _check_row_size(self)->bool:
        """ Checks to see if the user inputed size is the correct type of input. """
        try:
            user_input = int(self._row_size_entry.get())
        except ValueError:
            return False
        else:
            return 4 <= user_input and user_input <= 16 and user_input%2 == 0

    def _check_col_size(self)->bool:
        """ Checks to see if the user inputed size is the correct type of input. """
        try:
            user_input = int(self._col_size_entry.get())
        except ValueError:
            return False
        else:
            return 4 <= user_input and user_input <= 16 and user_input%2 == 0

    def _check_starting_color(self)-> bool:
        """ Checks to see if the user inputed color is the correct type of input"""
        user_input = self._starting_turn_entry.get()
        return user_input == 'B' or user_input == 'W'

    def _check_upper_left_color(self)-> bool:
        """ Checks to see if the user inputed color is the correct type of input"""
        user_input = self._top_left_entry.get()
        return user_input == 'B' or user_input == 'W'

    def _check_how_game_is_won_input(self)->bool:
        """ Checks to see if the user input is the correct type of input"""
        user_input = self._how_game_is_won_entry.get()
        return user_input.upper() == '>' or user_input.upper() == '<'

    
    

    def _on_ok_button(self) -> None:
        """ When ok is clicked it checks all the input"""
        self._ok_clicked = True
        if self._check_row_size() == True:
            self._row_size = self._row_size_entry.get()
        if self._check_col_size() == True:
            self._col_size = self._col_size_entry.get()
        if self._check_starting_color() == True:
            self._starting_turn = self._starting_turn_entry.get()
        if self._check_upper_left_color() == True:
            self._top_left = self._top_left_entry.get()
        if self._check_how_game_is_won_input() == True:
            self._how_game_is_won = self._how_game_is_won_entry.get()
        
        self._dialog_window.destroy()
        

    def _on_cancel_button(self) -> None:
        """ Destroys the window when cancel is clicked """
        self._dialog_window.destroy()


class StartDialog:
    def __init__(self):
        """ Initializes the class """
        self._root_window = tkinter.Tk()
        self.error_label = tkinter.StringVar()

        setup_button = tkinter.Button(
            master = self._root_window, text = 'Setup', font = DEFAULT_FONT,
            command = self._on_setup )

        setup_button.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.S + tkinter.N + tkinter.W + tkinter.E)

        self._setup_text = tkinter.StringVar()
        self._setup_text.set('No settings yet!')

        setup_label = tkinter.Label(
            master = self._root_window, textvariable = self._setup_text,
            font = DEFAULT_FONT)

        setup_label.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)

    def _on_setup(self):
        """ When setup is clicked it opens a new window where the user can input the settings"""
        dialog = BoardSetupDialog()
        dialog.show()
        if dialog.was_ok_clicked():
            self.row_size = dialog.get_row_size()
            self.col_size = dialog.get_col_size()
            self.starting_turn = dialog.get_starting_color()
            self.top_left = dialog.get_top_left()
            self.how_game_is_won = dialog.get_how_game_is_won()
                           
            self._setup_text.set('BOARD CONFIGURATIONS \n Rows: {0} \n'
                                 'Columns: {1} \n Starting Color: {2} \n'
                                 'Upper-left Piece: {3} \n'
                                 'How Game is Won: {4}'.format(self.row_size, self.col_size, self.starting_turn, self.top_left, self.how_game_is_won))
    
            self.user_input_list = [self.row_size, self.col_size, self.starting_turn, self.top_left, self.how_game_is_won]
            if '' in self.user_input_list:
                error_label = tkinter.Label( master = self._root_window, textvariable= self.error_label, font = DEFAULT_FONT)
                error_label.grid( row = 0, column = 0, padx = 10, pady= 10, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
                self.error_label.set(" There was INVALID input. \n Please enter VALID input.")
            elif '' not in self.user_input_list:
                self.error_label.set('You entered valid input! Confirm your settings.')
                confirm_button = tkinter.Button( master = self._root_window, text = 'CONFIRM', font = DEFAULT_FONT, command = self._confirm )
                confirm_button.grid( row = 1, column = 0, padx = 10, pady= 10, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

    def _confirm(self):
        """ When confirm is clicked it destroys the window and starts the game"""
        self._root_window.destroy()
        board = Board(int(self.row_size), int(self.col_size), self.starting_turn, self.top_left, self.how_game_is_won)
        OthelloApp(board).start()

        
    def start(self) -> None:
        """ Starts the loop"""
        self._root_window.mainloop()

class OthelloApp:
    def __init__(self, board):
        """ Initializes the class"""
        self.board = board
        self._root_window = tkinter.Tk()
        self._score = tkinter.StringVar()
        self._turn = tkinter.StringVar()
        self._winner = tkinter.StringVar()
        score_label = tkinter.Label(master = self._root_window, textvariable = self._score , font = MAIN_FONT)
        score_label.grid(row = 0, column = 0, columnspan = 16, padx = 10, pady = 10, sticky = tkinter.N)
        self._othello_canvas = tkinter.Canvas(master = self._root_window, width = 500, height = 500,  background = 'green')
        self._othello_canvas.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        turn_label = tkinter.Label(master = self._root_window, textvariable = self._turn , font = MAIN_FONT)
        turn_label.grid(row = 2, column = 0, columnspan = 16, padx = 10, pady = 10, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 3)
        self._root_window.rowconfigure(2, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)

        self._othello_canvas.bind('<Configure>', self._on_canvas_resized)
        self._othello_canvas.bind('<Button-1>', self._on_canvas_clicked)

    def draw_board(self):
        """ Draws the board when the board list is given."""
        self._othello_canvas.delete(tkinter.ALL)
        self._score.set('FULL \n B: {0}  W: {1}'.format(*self.board.count_number_of_pieces()))
        self._turn.set('TURN: {}'.format(self.board.current_player))
        canvas_width = self._othello_canvas.winfo_width()
        canvas_height = self._othello_canvas.winfo_height()
        for row in range(self.board.row_size):
            cell_height = canvas_height/self.board.row_size
            self._othello_canvas.create_line(0,cell_height*(row+1), canvas_width, cell_height*(row+1), fill = 'white')
            for column in range(self.board.column_size):
                cell_width = canvas_width/self.board.column_size
                self._othello_canvas.create_line(cell_width*(column+1), 0, cell_width*(column+1), canvas_height, fill = 'white')
                if self.board.board_state[row][column] == 'B':
                    self._othello_canvas.create_oval(column*cell_width, row*cell_height, (column+1)*cell_width, (row+1)*cell_height, fill = 'black')
                elif self.board.board_state[row][column] == 'W':
                     self._othello_canvas.create_oval(column*cell_width, row*cell_height, (column+1)*cell_width, (row+1)*cell_height, fill = 'white')
                else:
                    pass

    def add_to_board(self, x, y)->tuple:
        """  Adds to board  if the game is not over and its a valid move.
            When the game is over it prints the winner."""
        while not self.board.is_game_over():
            canvas_width = self._othello_canvas.winfo_width()
            canvas_height = self._othello_canvas.winfo_height()
            cell_height = canvas_height/(self.board.row_size)
            row = int(y/cell_height)
            cell_width = canvas_width/self.board.column_size
            col = int(x/cell_width)
            if not self.board.is_valid_move(row, col):
                break
            else:
                self.board.apply_move(row, col)
                break
        if self.board.is_game_over():
            winner = self.board.determine_winner()
            if winner is None:
                winner = 'NONE'
            winner_label = tkinter.Label(master = self._root_window, textvariable = self._winner , font = MAIN_FONT)
            winner_label.grid(row = 4, column = 0, columnspan = 16, padx = 10, pady = 10, sticky = tkinter.N)
            self._winner.set('THE WINNER IS: {0}'.format(winner))

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        """ When the canvas is clicked, it adds it to the list if it is a correct move """
        self.add_to_board(event.x,event.y)
        self.draw_board()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        """Handles the resizing of the board by drawing the board again."""
        self.draw_board()

    def start(self) -> None:
        """  Starts the Othello App."""
        self._root_window.mainloop()

if __name__ == '__main__':
    StartDialog().start()

