from question import Question

question_prompts = [
    "What color are apples?\n(a) Red \n(b) Blue \n(c)Grey \n",
    "What color are bananas?\n(a) Black \n(b) Orange \n(c)Green \n",
    "What color are your faces?\n(a) Black \n(b) Orange \n(c)Green \n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

def Quest (questions):
    score = 0
    for quest in questions:
        answer = input(quest.prompt)
        if answer == quest.answer:
            score+=1
    print('You got '+ str(score) +" questions right")

Quest(questions)    