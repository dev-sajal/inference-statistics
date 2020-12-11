import dill
Quiz = dill.load(open('question/QuizClass.pik', 'rb'))
quiz = dill.load(open('question/Quiz.pik', 'rb'))

try:
    print(quiz.score())
except KeyError:
    print(0)