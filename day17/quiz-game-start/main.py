from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

if __name__ == "__main__":
    question_bank = []

    for element in question_data:
        question_bank.append(Question(element["question"], element["correct_answer"]))

    quizzes = Quiz_Brain(question_bank)
    while quizzes.still_has_questions():
        quizzes.next_question()

    print(f"You've completed the quiz\n"
          f"Your final score was: {quizzes.score}")