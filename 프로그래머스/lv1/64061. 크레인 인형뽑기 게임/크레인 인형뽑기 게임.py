def solution(board, moves):
    dolls = []
    res = 0
    for move in moves:
        for idx, floor in enumerate(board):
            item = floor[move-1]
            if item != 0:
                if dolls and dolls[-1] == item:
                    dolls.pop()
                    res += 2
                else:
                    dolls.append(item)
                board[idx][move-1] = 0
                break
            else:
                continue
    return res