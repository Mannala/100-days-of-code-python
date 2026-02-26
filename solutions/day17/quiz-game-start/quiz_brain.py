class Quiz_Brain:
    def __init__(self, question_list):
        self.score = None
        self.question_number = 0
        self.question_list = question_list
        self.score_points = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        actual_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {actual_question.text} (True/False)?: ")
        self.check_answer(answer, actual_question.answer)


    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got ir right!")
            self.score_points += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        self.score = f"{self.score_points}/{self.question_number}"
        print(f"Your current score is: {self.score}\n")

