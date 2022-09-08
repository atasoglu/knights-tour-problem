from tabulate import tabulate

class Board:
    def __init__(self, **kwargs) -> None:
        self.__size: int = kwargs.get('board_size') if kwargs.get('board_size') else 8
        self.clear()

    @property
    def size(self) -> int:
        return self.__size
  
    def clear(self) -> None:
        dim: range = range(self.__size)
        self.__board: list[list[int]] = [[None for _ in dim] for __ in dim]

    def set_square(self, square: tuple[int], value: int) -> None:
        i, j = square
        self.__board[i][j] = value
    
    def is_on_board(self, square: tuple[int]) -> bool:
        row, col = square[0], square[1]
        return (row >= 0 and row < self.__size) and (col >= 0 and col < self.__size)

    def is_none(self, square: tuple[int]) -> bool:
        i, j = square
        return self.__board[i][j] == None

    def to_string(self) -> str:
        return tabulate([row for row in self.__board], tablefmt='grid')