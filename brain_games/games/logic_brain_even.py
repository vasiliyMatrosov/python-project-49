from random import randint

MIN = 0
MAX = 100

MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_parity_check(number):
    return number % 2 == 0 and 'yes' or 'no'


def get_question_and_correct_answer():

    question_of_game = randint(MIN, MAX)
    correct_answer = get_parity_check(question_of_game)

    return question_of_game, correct_answer
