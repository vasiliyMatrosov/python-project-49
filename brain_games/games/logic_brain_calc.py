import random

MIN = 0
MAX = 100


MESSAGE = 'What is the result of the expression?'


def get_question_and_correct_answer():

    first_number = random.choice(range(MIN, MAX))
    operator_of_calc = random.choice(['+', '-', '*'])
    second_number = random.choice(range(MIN, MAX))

    question = f'{first_number} {operator_of_calc} {second_number}'
    correct_answer = str(eval(question))

    return question, correct_answer
