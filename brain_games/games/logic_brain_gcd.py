import random
import math

MIN = 1
MAX = 10

MESSAGE = 'Find the greatest common divisor of given numbers.'


def get_question_and_correct_answer():

    FIRST_NUMBER = random.choice(range(MIN, MAX))
    SECOND_NUMBER = random.choice(range(MIN, MAX))
    question = f'{FIRST_NUMBER} {SECOND_NUMBER}'
    correct_answer = str(math.gcd(FIRST_NUMBER, SECOND_NUMBER))

    return question, correct_answer
