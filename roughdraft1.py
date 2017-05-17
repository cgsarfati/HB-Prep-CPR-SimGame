def display_introduction():

    print "Welcome to the CPR Simulation Game!"


def start_simulation():

    print "\nWelcome to the CPR Simulation game!"
    user_name = raw_input("\nWhat is your name? ")
    print "\nHi " + user_name + ". It's very nice to meet y--"
    print "\n*someone screams in the distance*"
    print "\nstranger: HELP! HELP! HELP!"
    print "\n*a stranger runs towards you*"
    print "\nstranger: Hey!! Hurry come with me, I found someone unconscious!!!"
    print "\n*you follow the stranger*"
    print "\n*you see an individual laying face down on the floor, unresponsive*"
    print "\nstranger: I'm going to call 911 right now."
    print "\n*you check the person's pulse for 10 seconds. No pulse. No chest recoil or noticeable breathing."

    #print current condition of victim (e.g. no pulse, no breathing)


def get_CPR_tutorial_main_menu():
    """Prints CPR tutorial menu and asks user to make a choice"""

    print '\n   Let us go through CPR Procedure!'
    print '\n     a. Check airway review'
    print '     b. Initiate breathing review'
    print '     c. Perform compressions review'
    print '     d. Back to main menu \n'

    user_choice = raw_input("What would you like to do? ")

    #user_choice to be used in execute_repl_in_main_menu functio
    return user_choice


def execute_user_input_CPR_tutorial_menu():
    """Executes loop acccording to user input from main menu tutorial function"""

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
        choice = get_CPR_tutorial_main_menu()

        if choice == 'c':
        #c. perform compressions
            if user_map[0] == 'False':
                current_score = perform_compressions_review()
                user_map[0] = 'True'
                #updated map = [T, F, F]
            elif user_map[0] == 'True' and user_map[1] == 'False':
                print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Airway review now!"
            elif user_map[1] == 'True' and user_map[2] == 'False':
                print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Breathing review now!"

        if choice == 'a':
        #a. check airway
            if user_map[0] == 'True' and user_map[1] == 'False':
                current_score += check_airway_review()
                user_map[1] = 'True'
                #updated map = [T, T, F]
            elif user_map[0] == 'False':
                print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Compressions review now!"
            elif user_map[1] == 'True' and user_map[2] == 'False':
                print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Breathing review now!"

        if choice == 'b':
        #b. initiate breathing
            if user_map[1] == 'True' and user_map[2] == 'False':
                current_score += initiate_breathing_review()
                user_map[2] = 'True'
                #updated map = [T, T, T]
            elif user_map[0] == 'False':
                print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Compressions review now!"
            elif user_map[0] == 'True' and user_map[1] == 'False':
                print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Airway review now!"

        if choice == 'd':
            execute_repl_main_menu()

        if user_map == ['True', 'True', 'True']:
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
        else:
            print "Sorry, the right answer is " + ask['correct_answer'] + ")"

    #returns back to current_score variable in main menu function
    return score


def check_airway_review():
    """Chronologically displays airway questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    airway_questions = [
        {
            'question': 'What are signs of "normal breathing" on an unconscious person?',
            'correct_answer': str(3),
            'options': ["Presence of chest recoil", "Feeling the person's breath on your cheek and ear", "Both 1 and 2"],
            'try_again': "customizable try again message"},
        {
            'question': 'Is gasping considered "normal breathing"?',
            'correct_answer': str(2),
            'options': ['Yes', 'No'],
            'try_again': "customizable try again message2"}
        ]

    airway_score = ask_question_CPR_tutorial(airway_questions)
    return airway_score


def initiate_breathing_review():
    """Chronologically displays breathing questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    breathing_questions = [
        {
            'question': "What is the proper technique of opening a person's airway during rescue breathing",
            'correct_answer': str(1),
            'options': ['Head-tilt, chin-lift maneuver', 'Head-tilt, chin-down maneuver', 'It does not matter', "Do not change the position of the person's neck"],
            'try_again': "customizable try again message"},
        {
            'question': 'How many rescue breathes per 30 compressions do you give during CPR',
            'correct_answer': str(2),
            'options': ['1', '2', '3', '4'],
            'try_again': "customizable try again message2"},
        {
            'question': 'How do you know if you successfully executed a rescue breath',
            'correct_answer': str(3),
            'options': ['Presence of pulse', 'If person becomes conscious', 'Presence of chest recoil', 'None of the above'],
            'try_again': "customizable try again message2"}
        ]

    breathing_score = ask_question_CPR_tutorial(breathing_questions)
    return breathing_score


def perform_compressions_review():
    """Chronologically displays compression questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    compressions_questions = [
        {
            'question': 'How many compressions per 2 rescue breathes do you initiate on an adult if you are alone',
            'correct_answer': str(3),
            'options': ['10', '20', '30', '40'],
            'try_again': "customizable try again message"},
        {
            'question': "How deep do you push down on an individual's chest during adult CPR",
            'correct_answer': str(3),
            'options': ['As hard as you can', 'Until you hear a crack', 'At least 2 inches but not more than 2.4', 'At most 1 inch'],
            'try_again': "customizable try again message2"},
        {
            'question': 'What is the proper hand placement during compressions for adult CPR',
            'correct_answer': str(2),
            'options': ['Right below the neck between the clavicles', '2 hands on the lower half of the sternum', 'Right on top of the belly button', "1 hand on the chest and 1 hand supporting the person's neck"],
            'try_again': "customizable try again message2"}
        ]

    compressions_score = ask_question_CPR_tutorial(compressions_questions)
    return compressions_score


def display_revival_scenario():
    """Prints inevitable successful revival scenario of victim"""

    #print that 911 has arrived and victim is revived successfully
    print "WOP conclusion text"


def CPR_tutorial_tracking_score():
    """Display user's total score with numerical ranges that indicate how
    well user did in game"""

    final_score = execute_user_input_CPR_tutorial_menu()

    if final_score <= 2:
        #0-2/8 correct
        print "Oof. I'd recommend going through this tutorial again!"
    elif final_score > 2 and final_score <= 5:
        #3-5/8 correct
        print "I sensed you struggled a bit. I recommend going through this tutorial one more time!"
    elif final_score > 6:
        #6-8/8 correct
        print "Excellent! Looks like you're ready!"


def get_main_menu():
    """Prints introductory main menu and asks user to make a choice"""

    print "\n   - Main Menu -\n"

    print '     a. Start game'
    print '     b. CPR tutorial'
    print '     c. Exit game \n'

    choice = raw_input('Choose from the menu options: ')
    return choice


def execute_repl_main_menu():

    playing = 'True'

    while playing == 'True':

        user_choice = get_main_menu()

        if user_choice == 'a':
            start_simulation()
            playing = 'False'

        elif user_choice == 'b':
            CPR_tutorial_tracking_score()

        elif user_choice == 'c':
            exit()

display_introduction()

execute_repl_main_menu()
