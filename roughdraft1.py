def display_introduction():
    """Prints introductory scenario that user is in"""

    print "WOP display introduction text"

    #print initial scenario that user is in (finds victim on floor)

    #print current condition of victim (e.g. no pulse, no breathing)

    #WOP: figure out how to have lagtime b/w this function and the main menu;
    #maybe have a raw input asking if user wants to continue?


def get_main_menu():
    """Prints main menu and asks user to make a choice"""

    print '\n   Main menu that asks user to click options below'
    print '     a. Check airway'
    print '     b. Initiate breathing'
    print '     c. Perform compressions'
    print '     d. Exit game \n'

    user_choice = raw_input("What would you like to do? ")

    #user_choice to be used in execute_repl_in_main_menu functio
    return user_choice


def execute_user_interaction_in_main_menu():
    """Executes loop depending on what user decides to choose in
    main menu"""

    #list that contains correct order of user input
    correct_road_map = ['c', 'a', 'b']

    #initial list corresponding to each user input. all starts false; as user
    #types in correct input, item will be reassigned to true. user completes
    #game when items all reassigned to true
    user_map = ['False', 'False', 'False']

    playing = 'True'

    while playing == 'True':

        #transfers return input from get_main_menu function to use in loop
        choice = get_main_menu()

        if choice == 'c':
            questions_perform_compressions()
            user_map[0] == 'True'
            #updated map = [T, F, F]

        if choice == 'a':
            if user_map[0] == 'True':
                questions_check_airway()
                user_map[1] == 'True'
                #updated map = [T, T, F]
            else:
                print "Try again"

        if choice == 'b':
            if user_map[1] == 'True':
                questions_initiate_breathing()
                user_map[2] == 'True'
                #updated map = [T, T, T]

        if choice == 'd':
            #d. exit game

            #exit game
            break

        if user_map == ['True', 'True', 'True']:
            display_conclusion_with_final_score()


def questions_check_airway():
    """Chronologically displays airway questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    #score starts at 0, will either +1 or stay at current score depending if
    #user inputs correct/wrong answer

    airway_score = 0

    #dictionaries inside list below. default keys are 'question', 'correct_answer',
    #'options', and 'try_again' (will be used later as added feature).
    #values can be customized to allow for flexibilty.

    airway_questions = [
        {
            'question': 'is person breathing question 1',
            'correct_answer': str(4),
            'options': ['answer1', 'answer2', 'answer3', 'rightanswer4'],
            'try_again': "customizable try again message"},
        {
            'question': 'pulse question 2',
            'correct_answer': str(2),
            'options': ['answer1', 'rightanswer2', 'answer3', 'answer4'],
            'try_again': "customizable try again message2"}
        ]

    #for loop designed to iterate through each question using dictionary above
    #with raw input from user
    for ask in airway_questions:

        #prints question
        print ask['question'] + "?"

        #formats question: e.g. 1) "Question"; iterates over each 'options' value
        n = 1
        for options in ask['options']:
            print "%d) %s" % (n, options)
            n = n + 1

        #prompts user input
        response = raw_input("What is your answer? ")

        #if correct input, outputs current score; if not, outputs try again
        #message and moves on to next question. currently doesn't give user
        #a second chance to answer correctly
        if response == ask['correct_answer']:
            print "Correct"
            airway_score += 1
            print "Your current score is " + str(airway_score) + " out of 2"
        else:
            print "Sorry, the right answer is " + ask['correct_answer'] + ")"
            continue

    return airway_score


def questions_initiate_breathing():
    """Chronologically displays breathing questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    breathing_score = 0

    breathing_questions = [
        {
            'question': 'airway technique question 1',
            'correct_answer': str(4),
            'options': ['answer1', 'answer2', 'answer3', 'rightanswer4'],
            'try_again': "customizable try again message"},
        {
            'question': 'amount of breathes question 2',
            'correct_answer': str(2),
            'options': ['answer1', 'rightanswer2', 'answer3', 'answer4'],
            'try_again': "customizable try again message2"},
        {
            'question': 'amount of breathes question 2',
            'correct_answer': str(2),
            'options': ['answer1', 'rightanswer2', 'answer3', 'answer4'],
            'try_again': "customizable try again message2"}
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
            print "Your current score is " + str(breathing_score) + " out of 3"
        else:
            print "Sorry, the right answer is " + ask['correct_answer'] + ")"
            continue

    return breathing_score


def questions_perform_compressions():
    """Chronologically displays compression questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    compressions_score = 0

    compressions_questions = [
        {
            'question': 'rate question 1',
            'correct_answer': str(4),
            'options': ['answer1', 'answer2', 'answer3', 'rightanswer4'],
            'try_again': "customizable try again message"},
        {
            'question': 'depth question 2',
            'correct_answer': str(2),
            'options': ['answer1', 'rightanswer2', 'answer3', 'answer4'],
            'try_again': "customizable try again message2"},
        {
            'question': 'location question 3',
            'correct_answer': str(2),
            'options': ['answer1', 'rightanswer2', 'answer3', 'answer4'],
            'try_again': "customizable try again message2"}
        ]

    for ask in compressions_questions:

        print ask['question'] + "?"

        n = 1
        for options in ask['options']:
            print "%d) %s" % (n, options)
            n = n + 1

        response = raw_input("What is your answer? ")

        if response == ask['correct_answer']:
            print "CORRECT"
            compressions_score += 1
            print "Your current score is " + str(compressions_score) + " out of 3"
        else:
            print "Sorry, the right answer is " + ask['correct_answer'] + ")"
            continue

    return compressions_score


def display_conclusion_with_final_score():
    """Prints successful revival scenario of victim display's user's total score
    with numerical ranges that indicate how well user did in game"""

    #print that 911 has arrived and victim is revived successfully
    print "WOP conclusion text"

    #print final_score through returns of functions that include airway_score +
    #breathing_score + compressions_score

    #WOP: you want return scores to be an int so you can add it together at the
    #end

    #print gives range of values e.g. (0-3: bad, 4-6: ok, 6-8: good job)
    print "WOP final score text"

display_introduction()

execute_user_interaction_in_main_menu()
