import random

MIN = 0
MAX = 100

MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer():

    QUESTION_OF_GAME = random.randint(MIN, MAX)
    correct_answer = QUESTION_OF_GAME % 2 == 0 and 'yes' or 'no'

    return QUESTION_OF_GAME, correct_answer
