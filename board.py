# import pieces

class Board:

    def __init__(self):
        self.sentinel = object()
        self.make_starting_grid()

    def add_piece(self, piece, pos):
        

    def move_piece(self, turn_color, start_pos, end_pos):

        piece = self.rows[start_pos[1]][start_pos[0]]

        if piece.color != turn_color
            raise NameError("You must move your own piece")
        elif end_pos not in piece.moves
            raise NameError("Piece does not move like that")
        elif end_pos not in piece.valid_moves
            raise NameError("You cannot move into check!")

        #add functionality for rasiing errors when the end pos is invalid
        if not self.valid_pos(start_pos):
            raise NameError("The start position is invalid!")
        if not self.valid_pos(end_pos):
            raise NameError("The end position is invalid!")
        
        #if there is no piece at the start pos
        #change this None to self.sentinel
        if self.rows[start_pos[1]][start_pos[0]] == None:
            raise NameError("This spot is empty!")

        #if there are no errors then move the piece!
        self.rows[end_pos[1]][end_pos[0]] = piece
        self.rows[start_pos[1]][start_pos[0]] = self.sentinel 
        piece.pos = end_pos

    def make_starting_grid(self):
        self.rows = [[self.sentinel]*8]*8
        #populate white and black pieces

    def valid_pos(self, pos):
        return all((x >= 0 and x <= 7) for x in pos)

    

b = Board()
# print(b.rows)
b.move_piece((0,0),(1,1))