import random


def start_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_question_and_correct_answer():
    QUESTION_OF_GAME = random.randint(2, 100)
    i = 2
    while QUESTION_OF_GAME % i != 0:
        i += 1

    correct_answer = i == QUESTION_OF_GAME and 'yes' or 'no'

    return QUESTION_OF_GAME, correct_answer
