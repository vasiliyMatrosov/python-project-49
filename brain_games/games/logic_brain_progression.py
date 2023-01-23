import random


def start_game():
    print('What number is missing in the progression?')


def get_question_and_correct_answer():

    list_of_progression = []
    FIRST_NUMBER = random.randint(0, 20)
    STEP_OF_PROGRESSION = random.randint(1, 10)
    LENGHT_OF_PROGRESSION = random.randint(5, 10)

    for _ in range(LENGHT_OF_PROGRESSION):
        FIRST_NUMBER += STEP_OF_PROGRESSION
        list_of_progression.append(FIRST_NUMBER)

    random_index = random.randint(0, LENGHT_OF_PROGRESSION - 1)
    missed_element = str(list_of_progression[random_index])

    list_of_progression[random_index] = '..'
    list_of_progression = " ".join(map(str, list_of_progression))

    return list_of_progression, missed_element
