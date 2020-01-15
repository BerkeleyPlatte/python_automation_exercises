# Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all 
# pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to 
# represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted 
# in an improper chess board.


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)

def cd_validator(board):
    keys = []
    values = []
    checks = 0
    for each in board.keys():
        keys.append(each)
    for each in board.values():
        values.append(each)
    if values.count('bking') == 1 and values.count('wking') == 1:
        checks += 1
    invalidator = []
    for each in keys:
        if int(each[0]) in range(1, 9):
            invalidator.append(0)
        else:
            invalidator.append(1)
        if each[1] in char_range('a', 'h'):
            invalidator.append(0)
        else:
            invalidator.append(1)
    if sum(invalidator) == 0:
        checks += 1
    b_pieces = []
    w_pieces = []
    for each in values:
        if each[0] == 'b':
            b_pieces.append(each)
        else:
            w_pieces.append(each)
    if len(b_pieces) < 17 and len(w_pieces) < 17:
        checks += 1
    bp_count = 0
    for each in b_pieces:
        if "pawn" in each:
            bp_count += 1
    wp_count = 0
    for each in w_pieces:
        if "pawn" in each:
            wp_count += 1
    if bp_count < 9 and wp_count < 9:
        checks += 1
        
    print(checks == 4)

cd_validator({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'})