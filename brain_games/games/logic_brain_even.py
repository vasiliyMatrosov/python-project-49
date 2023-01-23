import random


def start_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_question_and_correct_answer():

    QUESTION_OF_GAME = random.randint(0, 100)
    correct_answer = QUESTION_OF_GAME % 2 == 0 and 'yes' or 'no'

    return QUESTION_OF_GAME, correct_answer
