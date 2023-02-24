class Board:

    def __init__(self):
        self.board = [[0]*cols]*rows

    def move_piece(self, start_pos, end_pos):
        #if there is no piece at the start pos
        if self.board[start_pos[1]][start_pos[0]] == None:
            raise NameError("This spot is empty!")
        #add functionality for rasiing errors when the end pos is invalid
        if (end_pos[0] < 1 or > 8) or (end_pos[1] < 1 or > 8):
            raise NameError("The end position is invalid!")
        
        #if there are no errors then move the piece!
        self.board[end_pos[1]][end_pos[0]] = self.board[start_pos[1]][start_pos[0]]
        self.board[start_pos[1]][start_pos[0]] = None
