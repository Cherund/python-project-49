from random import randint


def progression():
    step = randint(1, 20)
    numbers_list = [str(randint(1, 50)), ]

    for i in range(9):
        next_number = int(numbers_list[i]) + step
        numbers_list.append(str(next_number))

    removed_index = randint(0, 9)
    correct_answer = numbers_list[removed_index]
    numbers_list[removed_index] = ".."

    print(f'Question: {" ".join(numbers_list)}')
    return correct_answer
