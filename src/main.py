class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def get_answer():
    """
    Asks the user for an answer
    :return: String
    """
    user_answer = input("Answer: ")
    return user_answer


def loop_through_questions(questions_list):
    """
    Prints every prompt of the questions inside the questions_list and asks the user for an answer.
    Then counts how many answers were correct and returns it.

    :param questions_list: Argument must be of type Question.
    :returns Integer.
    """
    points = 0
    for item in questions_list:
        print(f"\n{item.prompt}")
        user_answer = get_answer()
        if user_answer == item.answer:
            points += 1
        else:
            points = points

    return points


def main():
    questions = [Question("How many fingers do humans have on each hand?", "5"),
                 Question("What is the color of the sky?", "blue"),
                 Question("What is the color of a white horse?", "white")]

    looping = loop_through_questions(questions)
    print(f"You got a total of {looping}/{len(questions)} questions right.")


main()
# help(loop_through_questions)
