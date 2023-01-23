import random
import math


def start_game():
    print('Find the greatest common divisor of given numbers.')


def get_question_and_correct_answer():

    FIRST_NUMBER = random.choice(range(30))
    SECOND_NUMBER = random.choice(range(30))
    question = f'{FIRST_NUMBER} {SECOND_NUMBER}'
    correct_answer = str(math.gcd(FIRST_NUMBER, SECOND_NUMBER))

    return question, correct_answer
