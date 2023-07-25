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

    user = input('Enter your data: ')

    user_count = input('Enter data to search: ')

    result1 = len(user.split(user_count))
    result = result1 - 1
    print("There are " + str(result) + ' matches')

    user_text = input('Enter your data: ')

    print(user_text)

    user_search = input('Enter data to search: ')
    user_insert = input('Enter data to insert: ')

    user_text1 = user_text.replace(user_search, user_insert, 1)

    print(user_text1)


except ValueError as e:
    print(f'Error: {e}')
    print('Invalid data')