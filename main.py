try:
    user = input('Enter data: ')
    print(f'Your data: {user}')

    alpha_count = 0
    num_count = 0

    for mes in user:
        if mes.isalpha():
            alpha_count += 1
    for mes in user:
        if mes.isnumeric():
            num_count += 1

    print(f'Number of digits: {num_count}')
    print(f'Number of letters: {alpha_count}')

except ValueError as e:
    print(f'Error: {e}')
    print('Invalid data')
