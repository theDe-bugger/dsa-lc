# Checkers Move Validator

# Question: Write a function to validate moves in a Checkers game. Include jumping over opponent pieces and king piece movement.
# Topics: Classes, enums, condition checks.

from enum import Enum

class piece_color(Enum):
    WHITE = "white"
    BLACK = "black"

class piece_type(Enum):
    NORMAL = 0
    QUEEN = 1
    
class piece():
    def __init__(self, color, type) -> None:
        self.type = type
        self.color = color

class position():
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
    def is_valid(self):
        return self.row in range(0,8) and self.col in range(0,8)
    
class checkers_board():
    def __init__(self):
        # showing state of board
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        
        # TODO: initalize the board with the correct pieces
            
    def is_valid_move(self, start_position, end_position):
        if not start_position.is_valid() or not end_position.is_valid():
            return False
        
        piece_to_move = self.board[start_position.row][start_position.col]
        
        if piece_to_move == " ":
            return False
        
        target_piece = self.board[end_position.row][end_position.col]
        if target_piece != " ":
            return False
        
        # check if its going to a valid spot
        correct_direction = 1 if piece_to_move.color == piece_color.WHITE else -1
        
        if piece_to_move.type == piece_type.NORMAL:
            valid_positions = [position(start_position.row + correct_direction, start_position.col + 1), position(start_position.row +correct_direction, start_position.col - 1)]
        else:
            valid_positions = [position(start_position.row + correct_direction, start_position.col + 1), position(start_position.row + correct_direction, start_position.col - 1),
                               position(start_position.row - correct_direction, start_position.col + 1), position(start_position.row - correct_direction, start_position.col -1)]
        
        if end_position in valid_positions: return True
        
        # it has to be a capture move
        if piece_to_move.type == piece_type.NORMAL:
            valid_capture_positions = [position(start_position.row + correct_direction*2, start_position.col + 2), position(start_position.row + correct_direction*2, start_position.col - 2)]
        else:
            valid_capture_positions = [position(start_position.row + correct_direction*2, start_position.col + 2), position(start_position.row + correct_direction*2, start_position.col - 2),
                                        position(start_position.row - correct_direction*2, start_position.col + 2), position(start_position.row - correct_direction*2, start_position.col - 2)]

        if end_position in valid_capture_positions:
            between_position = position((end_position.row + start_position.row) // 2, (end_position.col + start_position.col) // 2)
            piece_in_between = self.board[between_position.row][between_position.col]
            if piece_in_between == " " or piece_in_between.color == piece_to_move.color:
                return False
            return True
        
        # failsafe
        return False
    
    def apply_moves(self, moves):
        # moves is a list of (start_pos, end_pos)
        if not moves: return True
        
        starting_player_color = self.board[moves[0][0].row][moves[0][0].col].color
        
        for move in moves:
            start_position, end_position = move
            if not self.is_valid_move(start_position,end_position):
                return False
            curr_piece = self.board[start_position.row][start_position.col]
            if curr_piece.color != starting_player_color:
                return False
            end_row = 0 if curr_piece.color == piece_color.BLACK else 8
            
            if curr_piece.type == piece_type.NORMAL and end_position.row == end_row:
                curr_piece.type = piece_type.QUEEN
            
            self.board[start_position.row][start_position.col] = " "
            self.board[end_position.row][end_position.col] = curr_piece
            
            # empty in between square for captures
            if (abs(end_position.row - start_position.row) == 1 and abs(end_position.col - start_position.col) == 1):
                self.board[(start_position.row + end_position.row)//2][(start_position.col + end_position.col)//2] = " "
            