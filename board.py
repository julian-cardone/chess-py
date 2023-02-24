# import pieces

class Board:

    def __init__(self):
        self.sentinel = object()
        self.make_starting_grid()

    def move_piece(self, start_pos, end_pos):

        #add functionality for rasiing errors when the end pos is invalid
        if not self.valid_pos(start_pos):
            raise NameError("The start position is invalid!")
        if not self.valid_pos(end_pos):
            raise NameError("The end position is invalid!")
        
        #if there is no piece at the start pos
        if self.rows[start_pos[1]][start_pos[0]] == None:
            raise NameError("This spot is empty!")

        #if there are no errors then move the piece!
        self.rows[end_pos[1]][end_pos[0]] = self.rows[start_pos[1]][start_pos[0]]
        self.rows[start_pos[1]][start_pos[0]] = None

    def make_starting_grid(self):
        self.rows = [[self.sentinel]*8]*8
        #populate white and black pieces

    def valid_pos(self, pos):
        return all((x >= 0 and x <= 7) for x in pos)

    

b = Board()
# print(b.rows)
b.move_piece((0,0),(1,1))