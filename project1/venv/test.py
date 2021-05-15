from Question import Question

questions_prompt = [
                    "color of apple? \n a yellow \n b green \n c red \n",
                    "color of orange? \n a orange \n b green \n c black \n",
                    "color of grape? \n a green \n b red \n c violet \n"
                    ]

Questions1 = [
               Question(questions_prompt[0], "c"),
               Question(questions_prompt[1], "a"),
               Question(questions_prompt[2], "a"),
              ]
def runtest(Questions1):
    score = 0
    for question in Questions1:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(score)


runtest(Questions1)

