from board import Board
class Knight(Board):
    def __init__(self, initial_square: tuple[int], **kwargs) -> None:
        super().__init__(**kwargs)
        self.__initial_square: tuple[int] = initial_square
        self.__offsets: list[tuple[int]] = [
                (-2, -1),   (-2, 1),
            (-1, -2),           (-1, 2),
            (1, -2),            (1, 2),
                (2, -1),    (2, 1)
        ]

    def __add_offset(self, square: tuple[int], offset: tuple[int]) -> tuple[int]:
        a, b = offset[0], offset[1]
        c, d = square[0], square[1]
        return (a + c, b + d)

    def __clear(self):
        super().clear()
        super().set_square(self.__initial_square, 0)
    
    def solve_greedy(self) -> str:
        self.__clear()
        curr_square: tuple[int] = self.__initial_square
        for i in range(1, super().size ** 2):
            end_of_way: bool = True
            for offset in self.__offsets:
                next_square: tuple[int] = self.__add_offset(curr_square, offset)
                if super().is_on_board(next_square) and super().is_none(next_square):
                    super().set_square(next_square, i)
                    curr_square = next_square
                    end_of_way = False
                    break
            if end_of_way:
                break
        return super().to_string()

    def __backtracking(self, curr_square: tuple[int], counter: int) -> bool:
        if counter == super().size ** 2:
            return True
        for offset in self.__offsets:
            next_square: tuple[int] = self.__add_offset(curr_square, offset)
            if super().is_on_board(next_square) and super().is_none(next_square):
                super().set_square(next_square, counter)
                if self.__backtracking(next_square, counter + 1):
                    return True
                super().set_square(next_square, None)
        return False 
    
    def solve_backtracking(self) -> str:
        self.__clear()
        if self.__backtracking(self.__initial_square, 1):
            return super().to_string()
        else:
            return 'No literal solution!'

    def __count_onward_score(self, square: tuple[int]) -> int:
        counter: int = 0
        for offset in self.__offsets:
            next_square: tuple[int] = self.__add_offset(square, offset)
            if super().is_on_board(next_square) and super().is_none(next_square):
                counter += 1
        return counter

    
    def solve_warndsdorff(self) -> str:
        self.__clear()
        curr_square: tuple[int] = self.__initial_square
        for i in range(1, super().size ** 2):
            end_of_way: bool = True
            min_score: int = 8
            best_square: tuple[int] = None
            for offset in self.__offsets:
                next_square: tuple[int] = self.__add_offset(curr_square, offset)
                if super().is_on_board(next_square) and super().is_none(next_square):
                    onward_score = self.__count_onward_score(next_square)
                    if onward_score < min_score:
                        min_score = onward_score
                        best_square = next_square
            if best_square:
                super().set_square(best_square, i)
                curr_square = best_square
                end_of_way = False

            if end_of_way:
                break
        return super().to_string()





