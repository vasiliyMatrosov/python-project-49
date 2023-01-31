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
    first_number = random.randint(MIN1, MAX1)
    step_of_progression = random.randint(STEP_MIN, STEP_MAX)
    lenght_of_progression = random.randint(MIN2, MAX2)

    for _ in range(lenght_of_progression):
        first_number += step_of_progression
        list_of_progression.append(first_number)

    random_index = random.randint(0, lenght_of_progression - 1)
    missed_element = str(list_of_progression[random_index])

    list_of_progression[random_index] = '..'
    list_of_progression = " ".join(map(str, list_of_progression))

    return list_of_progression, missed_element
