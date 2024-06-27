'''Домашнее задание №13: Обработка исключений. Собственные
исключения'''

class ChessBoardException(Exception):
    """Base class for chess board exceptions"""
    pass


class InvalidMoveException(ChessBoardException):
    """Exception raised for invalid moves"""
    def __str__(self):
        return "Invalid move for the chess piece."


def is_valid_position(position):
    """Check if the given position is valid on the chess board"""
    if len(position) != 2 or not position[0].isalpha() or not position[1].isdigit():
        return False
    col, row = position[0].lower(), int(position[1])
    return 'a' <= col <= 'h' and 1 <= row <= 8


def queen_move(start, end):
    """Check if the queen can move from start to end position in one move"""
    if not (is_valid_position(start) and is_valid_position(end)):
        raise ChessBoardException("Invalid position(s) provided.")
    col1, row1 = ord(start[0].lower()), int(start[1])
    col2, row2 = ord(end[0].lower()), int(end[1])
    return col1 == col2 or row1 == row2 or abs(col1 - col2) == abs(row1 - row2)


def knight_move(start, end):
    """Check if the knight can move from start to end position in one move"""
    if not (is_valid_position(start) and is_valid_position(end)):
        raise ChessBoardException("Invalid position(s) provided.")
    col1, row1 = ord(start[0].lower()), int(start[1])
    col2, row2 = ord(end[0].lower()), int(end[1])
    return (abs(col1 - col2) == 2 and abs(row1 - row2) == 1) or (abs(col1 - col2) == 1 and abs(row1 - row2) == 2)


if __name__ == "__main__":
    try:
        START_POSITION = input("Enter the starting position (e.g., e2): ")
        END_POSITION = input("Enter the ending position (e.g., e4): ")

        if queen_move(START_POSITION, END_POSITION):
            print("The queen can move from", START_POSITION, "to", END_POSITION, "in one move.")
        else:
            print("The queen cannot move from", START_POSITION, "to", END_POSITION, "in one move.")

        if knight_move(START_POSITION, END_POSITION):
            print("The knight can move from", START_POSITION, "to", END_POSITION, "in one move.")
        else:
            print("The knight cannot move from", START_POSITION, "to", END_POSITION, "in one move.")

    except ChessBoardException as ex:
        print(ex)
    except Exception as ex:
        print("An unexpected error occurred:", ex)
