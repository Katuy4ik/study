input_map = list(['1 3', '2 3', '3 3', '1 2', '2 2', '3 2', '1 1', '2 1', '3 1'])
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def print_field(stroka):
    print("---------")
    for i in range(0, 3):
        print("| " + " ".join(stroka[i * 3:(i + 1) * 3]) + " |")
    print("---------")

def validate_input(user_input):
    user_input_split = user_input.split(' ')

    if user_input_split[0].isdigit() != True or user_input_split[1].isdigit() != True:
        print('You should enter numbers!')
        return False

    if int(user_input_split[0]) < 1 or int(user_input_split[0]) > 3 or \
            int(user_input_split[1]) < 1 or int(user_input_split[1]) > 3:
        print('Coordinates should be from 1 to 3!')
        return False

    index_value = input_map.index(user_input)
    current_value = stroka[index_value]

    if current_value != ' ':
        print('This cell is occupied! Choose another one!')
        return False

    return True


def finish_criteria(stroka):

    #Check for impossible
    x_count = 0
    o_count = 0
    for i in range(0, len(stroka)):
        if stroka[i] == 'O':
            o_count += 1
        elif stroka[i] == 'X':
            x_count += 1

    x_win_count = 0
    o_win_count = 0
    for win in wins:
        if stroka[win[0]] == stroka[win[1]] and stroka[win[1]] == stroka[win[2]]:
            if stroka[win[0]] == 'X':
                x_win_count += 1
            elif stroka[win[0]] == 'O':
                o_win_count += 1

    if abs(x_count - o_count) > 1 or x_win_count == 1 and o_win_count == 1:
        print('Impossible')


    #Check for succes
    for i in range(0, len(wins)):
        win = wins[i]
        if stroka[win[0]] == stroka[win[1]] and stroka[win[1]] == stroka[win[2]] and stroka[win[0]] != ' ':
            return stroka[win[0]]

    for i in range(0, len(stroka)):
        if ' ' in stroka:
            continue
        else:
            return('Draw')




stroka = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print_field(stroka)
i = 0

while True:
    user_input = None
    valid_input = False
    while (valid_input == False):
        user_input = input('Enter the coordinates: ')
        valid_input = validate_input(user_input)

    index_value = input_map.index(user_input)
    if i % 2 == 0:
        stroka[index_value] = 'X'
    else:
        stroka[index_value] = 'O'
    i += 1

    print_field(stroka)

    if finish_criteria(stroka) == 'X' or finish_criteria(stroka) == 'O':
        print(finish_criteria(stroka), 'wins')
        break
    if finish_criteria(stroka) == 'Draw':
        print('Draw')
        break

