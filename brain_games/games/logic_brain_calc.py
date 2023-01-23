import random


def start_game():
    print('What is the result of the expression?')


def get_question_and_correct_answer():

    FIRST_NUMBER = random.choice(range(10, 20))
    OPERATOR_OF_CALC = random.choice(['+', '-', '*'])
    SECOND_NUMBER = random.choice(range(10))

    question = f'{FIRST_NUMBER} {OPERATOR_OF_CALC} {SECOND_NUMBER}'
    correct_answer = str(eval(question))

    return question, correct_answer
