from question import Question

question_prompts = [
    "From where we get vitamin D ?\n(a) Sun\n(b) Fruits\n(c)Junk Food\n(d)Water\n\n",
    "What is orange called ?\n(a) Fruit\n(b) color\n(c) a & b both\n(d) vehicle\n\n",
    "Which vitamin does Leomen contains ?\n(a) vitamin A\n(b) vitamin C\n(c) vitamin D\n(d) none of the above\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
    print("You got : " + str(score) + "/" + str(len(questions)) + " Correct")
run_test(questions)