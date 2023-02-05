from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_banks = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_banks.append(new_question)

quiz = QuizBrain(question_banks)
print(quiz)