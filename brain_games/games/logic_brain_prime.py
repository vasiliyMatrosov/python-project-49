from random import randint

MIN = 0
MAX = 50

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_prime(number):
    i = 2
    while number % i != 0:
        i += 1
    return i == number


def get_question_and_correct_answer():
    number = randint(MIN, MAX)
    if get_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question_of_game = number
    return question_of_game, correct_answer
