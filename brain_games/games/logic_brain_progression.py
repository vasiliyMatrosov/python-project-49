import random


MIN1 = 0
MAX1 = 20
MIN2 = 5
MAX2 = 10
STEP_MIN = 1
STEP_MAX = 10

MESSAGE = 'What number is missing in the progression?'


def get_question_and_correct_answer():

    list_of_progression = []
    FIRST_NUMBER = random.randint(MIN1, MAX1)
    STEP_OF_PROGRESSION = random.randint(STEP_MIN, STEP_MAX)
    LENGHT_OF_PROGRESSION = random.randint(MIN2, MAX2)

    for _ in range(LENGHT_OF_PROGRESSION):
        FIRST_NUMBER += STEP_OF_PROGRESSION
        list_of_progression.append(FIRST_NUMBER)

    random_index = random.randint(0, LENGHT_OF_PROGRESSION - 1)
    missed_element = str(list_of_progression[random_index])

    list_of_progression[random_index] = '..'
    list_of_progression = " ".join(map(str, list_of_progression))

    return list_of_progression, missed_element
