import copy

inf = 99999999

next_board = None


def alpha_beta_search(board, player):
    if player == 'max':
        v = max_value(board, -inf, +inf, True)
    else:
        v = min_value(board, -inf, +inf, True)

    return v


def max_value(board, alpha, beta, first_move):
    test_terminal_board = is_terminal_board(board)

    if test_terminal_board['status']:
        return test_terminal_board

    global next_board

    v = {
        'status': False,
        'winner': None,
        'utility': -inf,
        'board': board
    }

    successors = Node_movement(board, 'max')

    for s in successors:
        result = min_value(s, alpha, beta, False)

        if result['utility'] > v['utility']:
            if first_move:
                next_board = s

            v = result

        if v['utility'] >= beta:
            return v

        alpha = max(alpha, v['utility'])

    return v


def min_value(board, alpha, beta, first_move):
    test_terminal_board = is_terminal_board(board)

    if test_terminal_board['status']:
        return test_terminal_board

    global next_board

    v = {
        'status': False,
        'winner': None,
        'utility': inf,
        'board': board
    }
    successors = Node_movement(board, 'min')

    for s in successors:
        result = max_value(s, alpha, beta, False)

        if result['utility'] < v['utility']:
            if first_move:
                next_board = s

            v = result

        if v['utility'] <= alpha:
            return v

        beta = min(beta, v['utility'])

    return v


def Node_movement(board, player):
    next_board = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                new_board = copy.deepcopy(board)
                if player == 'max':
                    new_board[i][j] = 'x'
                else:
                    new_board[i][j] = 'o'
                next_board.append(new_board)

    return next_board


def is_terminal_board(board):
    result = {
        'status': False,
        'winner': None,
        'utility': None,
        'state': board
    }

    for i in range(3):
        if board[0][i] != '_' and board[0][i] == board[1][i] == board[2][i]:
            result['status'] = True
            result['winner'] = board[0][i]
            if board[0][i] == 'x':
                result['utility'] = 1
            else:
                result['utility'] = -1

            return result
        if board[i] == ['x', 'x', 'x'] or board[i] == ['o', 'o', 'o']:
            result['status'] = True
            result['winner'] = board[0][0]
            if board[0][0] == 'x':
                result['utility'] = 1
            else:
                result['utility'] = -1

            return result

    if board[0][0] != '_' and board[0][0] == board[1][1] == board[2][2]:
        result['status'] = True
        result['winner'] = board[0][0]
        if board[0][0] == 'x':
            result['utility'] = 1
        else:
            result['utility'] = -1

        return result
    if board[0][2] != '_' and board[0][2] == board[1][1] == board[2][0]:
        result['status'] = True
        result['winner'] = board[0][2]

        if board[0][2] == 'x':
            result['utility'] = 1
        else:
            result['utility'] = -1

        return result

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return result

    result['status'] = True
    result['winner'] = '_'
    result['utility'] = 0
    return result


if __name__ == "__main__":
    print('Board=')
    board = []
    for i in range(0, 3):
        temp = input().split(' ')
        board.append(temp)

    player = str(input('Player = ')).lower()

    result = alpha_beta_search(board, player)

    if result['utility'] == 0:
        print('Draw')
    elif result['utility'] == 1:
        print('Winner is Max')
    else:
        print('Winner is Min')

    if result['utility'] != 0:
        print('Next board can be,')
        for i in next_board:
            for j in i:
                print(f'{j} ', end='')
            print()
