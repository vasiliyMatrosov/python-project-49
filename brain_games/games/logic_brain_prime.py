import random

MIN = 0
MAX = 50

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_correct_answer():
    question_of_game = random.randint(MIN, MAX)
    i = 2
    while question_of_game % i != 0:
        i += 1

    correct_answer = i == question_of_game and 'yes' or 'no'

    return question_of_game, correct_answer
