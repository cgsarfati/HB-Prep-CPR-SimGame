breathing_score = 0

breathing_questions = [
  {
  'question': 'CPR question 1',
  'correct_answer': str(4),
  'options': ['answer1', 'answer2', 'answer3', 'rightanswer4'],
  'try_again': "customizable try again message"},
  {
   'question': 'CPR question 2',
   'correct_answer': str(2),
   'options': ['answer1', 'rightanswer2', 'answer3', 'answer4'],
   'try_again': "customizable try again message2"},
  {
   'question': 'CPR question 3',
   'correct_answer': str(1),
   'options': ['answer1', 'answer2', 'rightanswer3', 'answer4'],
   'try again': "customizable try again message3"}
  ]

for ask in breathing_questions:

    print ask['question'] + "?"

    n = 1
    for options in ask['options']:
        print "%d) %s" % (n, options)
        n = n + 1

    response = raw_input("What is your answer? ")

    if response == ask['correct_answer']:
        print "CORRECT"
        breathing_score += 1
        print "Your current score is " + str(breathing_score) + " out of 10"
    else:
        print "Sorry, the right answer is " + ask['correct_answer'] + ") "
