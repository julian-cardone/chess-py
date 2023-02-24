# import pieces

class Board:

    def __init__(self):
        self.sentinel = object()
        self.make_starting_grid()

    def make_starting_grid(self):
        self.rows = [[self.sentinel]*8]*8
        #populate white and black pieces

    def move_piece(self, start_pos, end_pos):
        #if there is no piece at the start pos
        if self.board[start_pos[1]][start_pos[0]] == None:
            raise NameError("This spot is empty!")
        #add functionality for rasiing errors when the end pos is invalid
        if (end_pos[0] < 1 or end_pos[0] > 8) or (end_pos[1] < 1 or end_pos[0] > 8):
            raise NameError("The end position is invalid!")
        
        #if there are no errors then move the piece!
        self.board[end_pos[1]][end_pos[0]] = self.board[start_pos[1]][start_pos[0]]
        self.board[start_pos[1]][start_pos[0]] = None

b = Board()
print(b.rows)