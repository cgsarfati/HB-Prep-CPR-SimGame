from time import sleep
import string
from string import whitespace


def print_storyline(scenario):
    """Prints unfolding scenario sentences with 2.5 sec delay

    Arguments:
        scenario - list of sentences from unfolding storyline"""

    #uses loop to print each item (sentence) in list (scenario) w/ 2.5 sec delay
    for sentence in scenario:
        print sentence
        sleep(2.5)


def display_introduction():
    """Prints introduction before main menu"""

    print "\nWelcome to the CPR Simulation Game!"


def simulation_introduction():
    """Prints scenario with user input of player name. Also uses time module
    with 2.5 second delay between statements"""

    print '\n ----- Welcome to the CPR Simulation game! -----'

    #prompt user input
    user_name = raw_input("\nWhat is your name? >>> ")

    introduction = [
        "\nHi " + user_name.capitalize() + ". It's very nice to meet y--",
        "\n*Someone screams in the distance*",
        "Stranger: HELP! HELP! HELP!",
        "*A stranger runs towards you*",
        "Stranger: Hey!! Hurry come with me, I found someone unconscious!!!",
        "*You follow the stranger*",
        "*You see an individual laying face down on the floor, unresponsive*",
        "Stranger: I'm going to call 911 right now.",
        "*You check the pulse for 10 seconds*",
        "*No pulse. No chest recoil or any noticeable breathing.\n"
        ]

    #uses 2.5 sec delay function to print list above
    print_storyline(introduction)


def simulation_actions_menu():
    """Prints menu choices and asks user for response"""

    print '\n - Actions -'
    print '   a. Check airway'
    print '   b. Initiate breathing'
    print '   c. Perform compressions'
    print '   d. Back to main menu'

    #ask user to choose from menu, returns choice to execute_simulation_actions() function
    user_choice = raw_input("\nWhat do you do? >>> ")
    return user_choice


def execute_simulation_actions():
    """Uses while loop to handle user input from main menu. All types of user
    input considered through nested conditionals. Uses T/F switch in user road
    map list to handle the correct order of responses"""

    #initial list for user input to serve as road map to handle already-picked
    #choices. starts all false. after user types correct input, item reassigned
    #to true. user completes game when all items reassigned to true
    user_map_simulation = ['False', 'False', 'False']

    #use road map below to follow logic behind nested conditionals
    # [C, A, B] -- correct user inputs in order
    # [F, F, F] -- 1st time menu shows. "Do C" as error message if input not C.
    # [T, F, F] -- 2nd time menu shows. c now complete. "Do A" if input not A.
    # [T, T, F] -- 3rd time menu shows. a now complete. "Do B" if input not B.
    # [T, T, T] -- menu will not show. b now complete. function done.

    #use in while loop as condition; reassign to False when user map [T, T, T]
    playing = 'True'

    while playing == 'True':

        #transfers return input from simulations_action_menu() to use in loop
        choice = simulation_actions_menu()
        #clean up user input: lowercase and remove spaces
        choice = choice.lower().translate(None, whitespace)

        #clean up user input: if all characters, continue. if number/symbol, print error
        if choice.isalpha():
            if choice == 'c' or choice == 'performcompressions':
            #c. perform compressions
                if user_map_simulation[0] == 'False':
                    perform_compressions_simulation()
                    user_map_simulation[0] = 'True'
                    #updated map = [T, F, F]
                elif user_map_simulation[0] == 'True' and user_map_simulation[1] == 'False':
                    print "You already performed compressions."
                elif user_map_simulation[1] == 'True' and user_map_simulation[2] == 'False':
                    print "You already performed compressions and checked the airway."

            if choice == 'a' or choice == 'checkairway':
            #a. check airway
                if user_map_simulation[0] == 'True' and user_map_simulation[1] == 'False':
                    check_airway_simulation()
                    user_map_simulation[1] = 'True'
                    #updated map = [T, T, F]
                elif user_map_simulation[0] == 'False':
                    print "Before checking the airway, let's get the blood flow moving first."
                elif user_map_simulation[1] == 'True' and user_map_simulation[2] == 'False':
                    print "You already did compressions and checked the airway. Person still not breathing."

            if choice == 'b' or choice == 'initiatebreathing':
            #b. initiate breathing
                if user_map_simulation[1] == 'True' and user_map_simulation[2] == 'False':
                    initiate_breathing_simulation()
                    user_map_simulation[2] = 'True'
                    #updated map = [T, T, T]
                elif user_map_simulation[0] == 'False':
                    print "Before giving rescue breathes, let's get the blood flow moving first."
                elif user_map_simulation[0] == 'True' and user_map_simulation[1] == 'False':
                    print "Before giving rescue breathes, let's check if the person is breathing."

            if choice == 'd':
            #d. back to main menu
                execute_repl_main_menu()

            if user_map_simulation == ['True', 'True', 'True']:
                #simulation finished, now goes to revival scenario text
                display_revival_scenario()
                #exit loop
                playing = 'False'
        else:
            print "Invalid. Make sure not to have any punctuation or numbers in your response!"


def ask_question_simulation(actionlist):
    """Formats simulation questions from dictionary and iterates through them

    arguments:
        action list: placeholder for list of dictionaries containing C/A/B questions"""

    #loops over each item in list of dictionaries
    for ask in actionlist:

        #while loop used so if invalid input, repeats question. if wrong/right intended answer, continues to next q.
        while True:

            print ask['question'] + "?"

            #formats question: e.g. 1) "Question"; iterates over each 'options' value
            n = 0
            for option in ask['options']:
                print "   " + str(string.lowercase[n]) + ". " + option
                n = n + 1

            #prompts user input
            response = raw_input(">>> ")
            response = response.lower().translate(None, whitespace)

            #taps into keys from list of dictionaries for corresponding values
            if response.isalpha() and len(response) == 1:
                if response == ask['correct_answer']:
                    print ask['successful_message']
                    break
                else:
                    print ask['try_again']
                    break
            else:
                print "Invalid response. Please type corresponding letter without punctuation or numbers."


def print_grid_introduction():
    """Prints description and navigation instructions of game"""

    print " \n--- Welcome to the CPR Simulation Mini Game #1: 2D Compression Grid ---\n\n "

    sleep(2)

    print """Description: Below is a 2D grid of the victim's chest. Type in the
    letter that corresponds to the correct hand placement of compressions when
    performing CPR. You are allowed as many attempts as possible. \n"""

    print """Navigation controls: Make sure to type an upper case letter. Do
    not type numbers, or include any punctuation. Otherwise, the prompt
    will give you an error message. \n\n\n"""


def print_grid_visual():
    """Prints 2D grid with legend"""

    print "        |   |                Legend: "
    print "        | E |                    A = Left clavicle"
    print "  __ __ __ __ __ __              B = Right clavicle"
    print " |                 |             C = Lower half of sternum"
    print " |   A    G   B    |             D = Under xiphoid process"
    print " |                 |             E = Lower half of neck"
    print " |        C   F    |             F = Heart"
    print " |                 |             G = Upper half of sternum"
    print " |                 | "
    print " |        D        | "
    print " |                 | "
    print " |                 | "
    print "  __ __ __ __ __ __  "


def execute_grid_user_command():
    """Uses nested conditionals for user input evaluation. Uses while loop for
    wrong or invalid user input, so user has infinite attempts until they get
    the correct answer"""

    playing = "True"

    #uses while loop so invalid/wrong responses allows user to try again until correct
    while playing == "True":

        user_choice = raw_input("\nWhat location will you pick for compressions? >>> ")
        #clean up code: converts user input to all lowercase and no spaces
        user_choice = user_choice.lower().translate(None, whitespace)

        if user_choice.isalpha():
            if user_choice == "c" or user_choice == "lowerhalfofsternum":
                print "Good job! That's right!"
                sleep(2)
                print "\n--- You completed CPR Simulation Mini-Game #1 ---\n"
                sleep(2)
                playing = "False"
            else:
                print "That does not seem right. Try again."
        else:
            print "Invalid. Make sure not to have any punctuation or numbers in your response!"


def perform_compressions_simulation():
    """Takes user to compressions scenario of CPR"""

    #calls compressions mini game
    print_grid_introduction()
    print_grid_visual()
    execute_grid_user_command()

    #continues to multiple choice scenario
    compressions_actions = [
        {
            'question': '\nYou now placed your hands on the correct chest location. How many compressions per 2 rescue breathes will you do',
            'correct_answer': 'c',
            'options': ['10', '20', '30', '40'],
            'successful_message': 'Good job, that makes sense!',
            'try_again': "That doesn't seem to be the right amount. Let's do 30 compressions instead."},
        {
            'question': "\nHow deep will you push down during your compressions",
            'correct_answer': 'c',
            'options': ['As hard as I can', 'Until I hear a crack', 'At least 2 inches but not more than 2.4', 'At most 1 inch'],
            'successful_message': 'Okay!',
            'try_again': "That doesn't sound safe. Let's do at least 2 inches in depth."}
        ]

    #use list above to put into question format function
    ask_question_simulation(compressions_actions)

    print '\nYou successfully performed 30 compressions.'


def check_airway_simulation():
    """Takes user to airway scenario of CPR"""

    airway_actions = [
        {
            'question': "\nYou decided to check the person's airway. How will you do that",
            'correct_answer': 'a',
            'options': ["Check for chest recoil and feel for the person's breath", "Squeeze person's nostrils", "Shake person"],
            'successful_message': 'Good job, that makes sense!',
            'try_again': "That doesn't seem right. Let's check for chest recoil and feel for the person's breath instead."},
        {
            'question': '\nThere is no chest recoil or noticeable breathing. If the person was gasping, would that be normal breathing',
            'correct_answer': 'b',
            'options': ['Yes', 'No'],
            'successful_message': 'Yep, gasping is not normal breathing!',
            'try_again': "Gasping is actually not normal breathing."}
        ]

    #use list above to put into question format function
    ask_question_simulation(airway_actions)

    print '\nYou successfully checked the airway. You also checked for pulse. Still no signs of normal breathing or pulse present.'


def print_guess_the_number_introduction():
    """Prints mini game introduction with description and navigation controls"""

    print " \n--- Welcome to the CPR Simulation Mini Game #2: Guess the Number ---\n\n "

    sleep(2)

    print """Description: After completing 30 compressions, you now
    need to decide how many rescue breathes to initiate. You have 5 tries to
    type the correct number. After 5 tries, the game restarts.\n"""

    print """Navigation controls: Make sure to only type a number. Do
    not type letters, or include any punctuation. It is considered 1 try if
    you type an invalid response. \n"""


def execute_guess_the_number_user_command():
    """Handles user input of guess the number mini game"""

    attempts = 1
    correct_number = 2
    guess = " "

    #uses while loop so player can have 5 attempts before game over
    while correct_number != guess and attempts < 6:

        guess = raw_input('\nHow many rescue breathes will you do? >>> ')

        #clean up code: if any characters/punctuation, error message
        if guess.isdigit():
            #convert str to int to use arithmetic conditional
            guess = int(guess)
            if guess < correct_number:
                print('Higher...')
                #adds attempt in while loop; after 5 tries, breaks
                attempts += 1
            elif guess > correct_number:
                print('Lower...')
                attempts += 1
        else:
            print "Oh no, you typed something other than a number!"
            attempts += 1

    if attempts == 6:
        print '\nSorry you reached the maximum number of tries'
        print '\nThe correct number was', correct_number
        #replay game since user failed
        print_guess_the_number_introduction()
        execute_guess_the_number_user_command()
    else:
        print 'You guessed it! The correct number was', correct_number
        #clean up code: attempt for 1, attempts for 2+
        if attempts == 1:
            print 'You guessed it in', attempts, 'attempt\n'
            sleep(2)
            print "\n--- You completed CPR Simulation Mini-Game #1 ---\n"
            sleep(2)
        elif attempts > 1:
            print 'You guessed it in', attempts, 'attempts\n'
            sleep(2)
            print "\n--- You completed CPR Simulation Mini-Game #1 ---\n"
            sleep(2)


def initiate_breathing_simulation():
    """Takes user to breathing scenario of CPR"""

    #calls rescue breathes mini game
    print_guess_the_number_introduction()
    execute_guess_the_number_user_command()

    breathing_actions = [
        {
            'question': "\nYou now decide to open the person's airway before giving rescue breathes. How",
            'correct_answer': 'a',
            'options': ['Head-tilt, chin-lift maneuver', 'Head-tilt, chin-down maneuver'],
            'successful_message': 'Perfect!',
            'try_again': "Actually, we need to lift the chin to straighten the airway."},
        {
            'question': '\nHow do you know if you successfully performed a rescue breath',
            'correct_answer': 'c',
            'options': ['Presence of pulse', 'If you do not meet resistance', 'Presence of chest recoil'],
            'successful_message': 'Yes, simultaneously check for chest recoil. If it rises, you are doing it right!',
            'try_again': "A successful rescue breath actually involves the presence of chest recoil."}
        ]

    #use list above to put into question format functio
    ask_question_simulation(breathing_actions)

    print '\nYou successfully performed 2 rescue breathes.'


def get_CPR_tutorial_main_menu():
    """Prints CPR tutorial menu and asks user to make a choice"""

    print '\n   - CPR Procedures -'
    print '\n     a. Check airway'
    print '     b. Initiate breathing'
    print '     c. Perform compressions'
    print '     d. Back to main menu \n'

    #prompts user input
    user_choice = raw_input("What would you like to do? >>> ")

    #user_choice to be used in execute_repl_in_main_menu function
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
        #clean up user input: lowercase and remove spaces
        choice = choice.lower().translate(None, whitespace)

        #clean up user input: if all characters, continue. if number/symbol, print error
        if choice.isalpha():
            if choice == 'c' or choice == 'performcompressions':
            #c. perform compressions
                if user_map[0] == 'False':
                    current_score = perform_compressions_review()
                    user_map[0] = 'True'
                    #updated map = [T, F, F]
                elif user_map[0] == 'True' and user_map[1] == 'False':
                    print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Airway review now!"
                elif user_map[1] == 'True' and user_map[2] == 'False':
                    print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Breathing review now!"

            if choice == 'a' or choice == 'checkairway':
            #a. check airway
                if user_map[0] == 'True' and user_map[1] == 'False':
                    current_score += check_airway_review()
                    user_map[1] = 'True'
                    #updated map = [T, T, F]
                elif user_map[0] == 'False':
                    print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Compressions review now!"
                elif user_map[1] == 'True' and user_map[2] == 'False':
                    print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Breathing review now!"

            if choice == 'b' or choice == 'initiatebreathing':
            #b. initiate breathing
                if user_map[1] == 'True' and user_map[2] == 'False':
                    current_score += initiate_breathing_review()
                    user_map[2] = 'True'
                    #updated map = [T, T, T]
                elif user_map[0] == 'False':
                    print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Compressions review now!"
                elif user_map[0] == 'True' and user_map[1] == 'False':
                    print "The proper order of CPR is Compressions - Airway - Breathing. Let's do Airway review now!"

            if choice == 'd' or choice == 'backtomainmenu':
            #d. back to main menu
                execute_repl_main_menu()

            if user_map == ['True', 'True', 'True']:
                playing = 'False'
        else:
                print "Invalid. Make sure not to have any punctuation or numbers in your response!"

    #return cumulative score from 3 challenges back to tracking score function
    return current_score


def ask_question_CPR_tutorial(questionlist):
    """ Formats tutorial questions from dictionary and iterates through them

    arguments:
        questionlist: placeholder for list of dictionaries containing C/A/B questions"""

    #score starts at 0, will either +1 or stay at current score depending if
    #user inputs correct/wrong answer
    score = 0

    #dictionaries inside list below. default keys are 'question', 'correct_answer',
    #'options', and 'try_again' (will be used later as added feature).
    #values can be customized to allow for flexib0ilty.
    for ask in questionlist:

        #while loop used so if invalid input, repeats question. if wrong/right intended answer, continues to next q.
        while True:

            #prints question
            print ask['question'] + "?"

            #formats question: e.g. 1) "Question"; iterates over each 'options' value
            n = 0
            for option in ask['options']:
                print "   " + str(string.lowercase[n]) + ". " + option
                n = n + 1

            #prompts user input
            response = raw_input("\nWhat is your answer? >>> ")
            response = response.lower().translate(None, whitespace)

            if response.isalpha() and len(response) == 1:
            #if correct input, outputs current score; if not, outputs try again
            #message and moves on to next question. currently doesn't give user
            #a second chance to answer correctly
                if response == ask['correct_answer']:
                    print "Correct!"
                    score += 1
                    break
                else:
                    print "Sorry, the right answer is " + ask['correct_answer'] + "."
                    break
            else:
                print "Invalid response. Please type corresponding letter without punctuation or numbers."

    #returns back to current_score variable in main menu function
    return score


def check_airway_review():
    """Chronologically displays airway questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    airway_questions = [
        {
            'question': '\nWhat are signs of "normal breathing" on an unconscious person',
            'correct_answer': 'c',
            'options': ["Presence of chest recoil", "Feeling the person's breath on your cheek and ear", "Both 1 and 2"],
            'try_again': "customizable try again message"},
        {
            'question': '\nIs gasping considered "normal breathing"',
            'correct_answer': 'b',
            'options': ['Yes', 'No'],
            'try_again': "customizable try again message2"}
        ]

    #use list above to put into question format function
    airway_score = ask_question_CPR_tutorial(airway_questions)

    #return score back to execute_user_input_CPR_tutorial_menu()
    return airway_score


def initiate_breathing_review():
    """Chronologically displays breathing questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    breathing_questions = [
        {
            'question': "\nWhat is the proper technique of opening a person's airway during rescue breathing",
            'correct_answer': 'a',
            'options': ['Head-tilt, chin-lift maneuver', 'Head-tilt, chin-down maneuver', 'It does not matter', "Do not change the position of the person's neck"],
            'try_again': "customizable try again message"},
        {
            'question': '\nHow many rescue breathes per 30 compressions do you give during CPR',
            'correct_answer': 'b',
            'options': ['1', '2', '3', '4'],
            'try_again': "customizable try again message2"},
        {
            'question': '\nHow do you know if you successfully executed a rescue breath',
            'correct_answer': 'c',
            'options': ['Presence of pulse', 'If person becomes conscious', 'Presence of chest recoil', 'None of the above'],
            'try_again': "customizable try again message2"}
        ]

    #use list above to put into question format function
    breathing_score = ask_question_CPR_tutorial(breathing_questions)

    #return score back to execute_user_input_CPR_tutorial_menu()
    return breathing_score


def perform_compressions_review():
    """Chronologically displays compression questions with user input. Once all
    questions are completed, user will be brought back to main menu"""

    compressions_questions = [
        {
            'question': '\nHow many compressions per 2 rescue breathes do you initiate on an adult if you are alone',
            'correct_answer': 'c',
            'options': ['10', '20', '30', '40'],
            'try_again': "customizable try again message"},
        {
            'question': "\nHow deep do you push down on an individual's chest during adult CPR",
            'correct_answer': 'c',
            'options': ['As hard as you can', 'Until you hear a crack', 'At least 2 inches but not more than 2.4', 'At most 1 inch'],
            'try_again': "customizable try again message2"},
        {
            'question': '\nWhat is the proper hand placement during compressions for adult CPR',
            'correct_answer': 'b',
            'options': ['Right below the neck between the clavicles', '2 hands on the lower half of the sternum', 'Right on top of the belly button', "1 hand on the chest and 1 hand supporting the person's neck"],
            'try_again': "customizable try again message2"}
        ]

    #use list above to put into question format function
    compressions_score = ask_question_CPR_tutorial(compressions_questions)

    #return score back to execute_user_input_CPR_tutorial_menu()
    return compressions_score


def display_revival_scenario():
    """Prints inevitable successful revival scenario of victim using time module of 2.5 sec delay"""

    conclusion = [
        "\nThe person suddenly gasps for air and is successfully revived.",
        "The ambulance arrives.",
        "The person gets transported to the hospital.",
        "\nGood job!!! You completed the CPR simulation game!!!\n"
        ]

    #uses 2.5 sec delay function to print list above
    print_storyline(conclusion)


def CPR_tutorial_tracking_score():
    """Display user's total score with numerical ranges that indicate how
    well user did in game"""

    final_score = execute_user_input_CPR_tutorial_menu()

    if final_score <= 2:
        #0-2/8 correct
        print "\nOof. I'd recommend going through this tutorial again!"
    elif final_score > 2 and final_score <= 5:
        #3-5/8 correct
        print "\nI sensed you struggled a bit. I recommend going through this tutorial one more time!"
    elif final_score > 6:
        #6-8/8 correct
        print "\nExcellent! Looks like you're ready!"


def get_main_menu():
    """Prints introductory main menu and asks user to make a choice"""

    print "\n   - Main Menu -\n"
    print '     a. Start game'
    print '     b. CPR tutorial'
    print '     c. Exit game \n'

    #prompt user choice
    choice = raw_input('Choose from the menu options >>> ')

    #transfers raw input to execute_repl_main_menu()
    return choice


def execute_repl_main_menu():
    """Uses REPL loop to handle user input from main menu"""

    playing = 'True'

    while playing == 'True':

        #assigns variable to user input from get_main_menu()
        user_choice = get_main_menu()

        #clean up user input: lowercase and remove spaces
        user_choice = user_choice.lower().translate(None, whitespace)

        #clean up user input: if all characters, continue. if number/symbol, print error
        if user_choice.isalpha():
            if user_choice == 'a' or user_choice == 'startgame':
                simulation_introduction()
                execute_simulation_actions()

            elif user_choice == 'b' or user_choice == 'cprtutorial':
                CPR_tutorial_tracking_score()

            elif user_choice == 'c' or user_choice == 'exitgame':
                exit()
        else:
            print "Invalid. Make sure not to have any punctuation or numbers in your response!"

display_introduction()

execute_repl_main_menu()
