def display_introduction():
    """Prints introductory scenario that user is in"""

    print "\nWelcome to the CPR Simulation game!"
    user_name = raw_input("\nWhat is your name? ")
    print "\nHi " + user_name + ". Let's get started!"

    #WOP: figure out how to have lagtime b/w this function and the main menu;
    #maybe have a raw input asking if user wants to continue?


def start_simulation():

    print "simulation"

    #print initial scenario that user is in (finds victim on floor)

    #print current condition of victim (e.g. no pulse, no breathing)


def get_CPR_main_menu():
    """Prints CPR tutorial menu and asks user to make a choice"""

    print '\n   Let us go through CPR Procedure!'
    print '\n     a. Check airway review'
    print '     b. Initiate breathing review'
    print '     c. Perform compressions review'
    print '     d. Back to main menu \n'

    user_choice = raw_input("What would you like to do? ")

    #user_choice to be used in execute_repl_in_main_menu functio
    return user_choice


def execute_user_interaction_CPR_main_menu():
    """Executes loop acccording to user input from main menu function"""

    #initial list for user input to serve as road map to handle already-picked
    #choices. starts all false. after user types correct input, item reassigned
    #to true. user completes game when all items reassigned to true
    user_map = ['False', 'False', 'False']

    #use road map below to follow logic behind nested conditionals
    # [C, A, B] -- correct user inputs in order
    # [F, F, F] -- 1st time menu shows. "Do C" as error message if input not C.
    # [T, F, F] -- 2nd time menu shows. c now complete. "Do A" if input not A.
    # [T, T, F] -- 3rd time menu shows. a now complete. "Do B" if input not B.
    # [T, T, T] -- menu will not show. b now complete. function done.

    #use in while loop as condition; reassign to False when user map [T, T, T]
    playing = 'True'

    while playing == 'True':

        #transfers return input from get_main_menu function to use in loop
        choice = get_CPR_main_menu()

        if choice == 'c':
        #c. perform compressions
            if user_map[0] == 'False':
                current_score = perform_compressions_review()
                user_map[0] = 'True'
                #updated map = [T, F, F]
            elif user_map[0] == 'True' and user_map[1] == 'False':
                print "already did c, do a now and b later"
            elif user_map[1] == 'True' and user_map[2] == 'False':
                print "already did c and a, do b now"

        if choice == 'a':
        #a. check airway
            if user_map[0] == 'True' and user_map[1] == 'False':
                current_score += check_airway_review()
                user_map[1] = 'True'
                #updated map = [T, T, F]
            elif user_map[0] == 'False':
                print "do c first"
            elif user_map[1] == 'True' and user_map[2] == 'False':
                print "already did a and c, do b now"

        if choice == 'b':
        #b. initiate breathing
            if user_map[1] == 'True' and user_map[2] == 'False':
                current_score += initiate_breathing_review()
                user_map[2] = 'True'
                #updated map = [T, T, T]
            elif user_map[0] == 'False':
                print "do c first"
            elif user_map[0] == 'True' and user_map[1] == 'False':
                print "already did c#, do a now and b later"

        if choice == 'd':
            execute_repl_main_menu()

        if user_map == ['True', 'True', 'True']:
            display_revival_scenario()
            playing = 'False'

    #return cumulative score from 3 challenges back to tracking score function
    return current_score


def ask_question_CPR_tutorial(questionlist):

    #score starts at 0, will either +1 or stay at current score depending if
    #user inputs correct/wrong answer
    score = 0

    #dictionaries inside list below. default keys are 'question', 'correct_answer',
    #'options', and 'try_again' (will be used later as added feature).
    #values can be customized to allow for flexib0ilty.
    for ask in questionlist:

        #prints question
        print ask['question'] + "?"

        #formats question: e.g. 1) "Question"; iterates over each 'options' value
        n = 1
        for option in ask['options']:
            print "%d) %s" % (n, option)
            n = n + 1

        #prompts user input
        response = raw_input("What is your answer? ")

        #if correct input, outputs current score; if not, outputs try again
        #message and moves on to next question. currently doesn't give user
        #a second chance to answer correctly
        if response == ask['correct_answer']:
            print "Correct"
            score += 1
            print "Your current score is " + str(score) + " out of " + str(len(questionlist))
        else:
            print "Sorry, the right answer is " + ask['correct_answer'] + ")"

    #returns back to current_score variable in main menu function
    return score


def check_airway_review():
    """Chronologically displays airway questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

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

    airway_score = ask_question_CPR_tutorial(airway_questions)
    return airway_score


def initiate_breathing_review():
    """Chronologically displays breathing questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

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

    breathing_score = ask_question_CPR_tutorial(breathing_questions)
    return breathing_score


def perform_compressions_review():
    """Chronologically displays compression questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

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

    compressions_score = ask_question_CPR_tutorial(compressions_questions)
    return compressions_score


def display_revival_scenario():
    """Prints inevitable successful revival scenario of victim"""

    #print that 911 has arrived and victim is revived successfully
    print "WOP conclusion text"


def tracking_score():
    """Display user's total score with numerical ranges that indicate how
    well user did in game"""

    final_score = execute_user_interaction_CPR_main_menu()

    if final_score <= 2:
        print "0-2 range: Oof. I'd recommend going through this tutorial again!"
    elif final_score > 2 and final_score <= 5:
        print "3-5 range scenario: I sensed you struggled a bit. I'd recommend going through this tutorial one more time!"
    elif final_score > 6:
        print "6-8 range scenario; Excellent! Looks like you're ready!"


def get_main_menu():
    """Prints introductory main menu and asks user to make a choice"""

    print '\n   Main menu\n'
    print '     a. Start game'
    print '     b. CPR tutorial'
    print '     c. Exit game \n'

    choice = raw_input('Choose from the menu options: ')
    return choice


def execute_repl_main_menu():

    while True:

        user_choice = get_main_menu()

        if user_choice == 'a':
            start_simulation()

        elif user_choice == 'b':
            tracking_score()

        elif user_choice == 'c':
            exit()

display_introduction()

execute_repl_main_menu()
