def check_winner(board):
    board = sum(board, [])
    win_index_pattern_array = [
                        [0,1,2],
                        [3,4,5],
                        [6,7,8],
                        [0,3,6],
                        [1,4,7],
                        [2,5,8],
                        [0,4,8],
                        [6,4,2],
                    ]
    for win_index_pattern in win_index_pattern_array:
        # print(f"Checking pattern: {win_index_pattern}")
        figure = ""
        for index in win_index_pattern:
            # print(f"Checking index {index}: {board[index]}, figure: {figure}")
            if figure == "":
                figure = board[index]
            elif figure != board[index] or figure == "":
                break
        else:
            if figure != "":
                return figure
    return ""

if __name__ == "__main__":
    board = [
        ["X", "X", "X"],
        ["O", "O", ""],
        ["", "", ""],
    ]
    print(check_winner(board))
    assert check_winner(board) == "X"
    board = [
        ["X", "X", ""],
        ["O", "O", "O"],
        ["", "", ""],
    ]
    print(check_winner(board))    
    assert check_winner(board) == "O"
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]
    print(check_winner(board))    
    assert check_winner(board) == ""
    board = [
        ["X", "O", "O"],
        ["O", "O", "X"],
        ["O", "X", "O"],
    ]
    print(check_winner(board))    
    assert check_winner(board) == "O"
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"],
    ]
    print(check_winner(board))    
    assert check_winner(board) == "X"
    board = [
        ["X", "O", "X"],
        ["O", "X", "X"],
        ["O", "X", "X"],
    ]
    print(check_winner(board))    
    assert check_winner(board) == "X"   
