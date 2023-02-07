from random import randint
from random import choice

MIN_OF_FIRST_NUMBER = 0
MAX_OF_FIRST_NUMBER = 20
MIN_OF_LENGHT_OF_PROGRESSION = 5
MAX_OF_LENGHT_OF_PROGRESSION = 10
STEP_MIN = 1
STEP_MAX = 10

MESSAGE = 'What number is missing in the progression?'


def is_progression():
    step_of_progression = randint(STEP_MIN, STEP_MAX)
    lenght_of_progression = randint(MIN_OF_LENGHT_OF_PROGRESSION,
                                    MAX_OF_LENGHT_OF_PROGRESSION)
    first_number = randint(MIN_OF_FIRST_NUMBER, MAX_OF_FIRST_NUMBER)
    progression = []
    progression.append(first_number)
    i = 0
    while i < lenght_of_progression:
        first_number += step_of_progression
        progression.append(first_number)
        i += 1
    return progression


def get_question_and_correct_answer():
    question = is_progression()
    correct_answer = choice(question)
    index = question.index(correct_answer)
    question[index] = '..'
    question = ' '.join(map(str, question))
    return question, str(correct_answer)
