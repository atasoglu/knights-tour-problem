from knight import Knight

knight = Knight(
    (0, 0), # initial square (row, columnm) 
    board_size=8 # number of square per axis
    )
print(knight.solve_backtracking()) # solving with backtracking
# print(knight.solve_warndsdorff()) # solving with warndsdorff
# print(knight.solve_greedy()) # actually, it's not a 'solving'. it's wrote just for test.