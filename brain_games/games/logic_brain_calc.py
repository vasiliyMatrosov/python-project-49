import random

MIN = 0
MAX = 100


MESSAGE = 'What is the result of the expression?'


def get_question_and_correct_answer():

    FIRST_NUMBER = random.choice(range(MIN, MAX))
    OPERATOR_OF_CALC = random.choice(['+', '-', '*'])
    SECOND_NUMBER = random.choice(range(MIN, MAX))

    question = f'{FIRST_NUMBER} {OPERATOR_OF_CALC} {SECOND_NUMBER}'
    correct_answer = str(eval(question))

    return question, correct_answer
