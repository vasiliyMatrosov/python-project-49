from random import randint
from random import choice

MIN = 0
MAX = 100


MESSAGE = 'What is the result of the expression?'


def is_calc(first_num, second_num, operator):
    if operator == '+':
        return first_num + second_num
    if operator == '-':
        return first_num - second_num
    if operator == '*':
        return first_num * second_num


def get_question_and_correct_answer():
    operator = ('+', '-', '*')
    first_num = randint(MIN, MAX)
    second_num = randint(MIN, MAX)
    operator = choice(operator)
    correct_answer = is_calc(first_num, second_num, operator)
    question = f'{first_num} {operator} {second_num}'

    return question, str(correct_answer)
