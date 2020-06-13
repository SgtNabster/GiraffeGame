import sys
import time
pain = 0
# Define restart function
def restart():
    # Requests if user wants to start again or not
    response = input("Would you like to try again? [Y/N]: ")
    if response.upper() == "Y":
        # starts game
        start_game()
    elif response.upper() == "N":
        print("Goodbye")
        # Closes program
        sys.exit()
    else:
        # Restarts this function till either Y or N entered
        print("Please enter either Y or N")
        restart()
# Define game over function
def game_over():
    # print game over art
    time.sleep(3)
    print(r"""
               ('-.     _   .-')       ('-.                           (`-.      ('-.  _  .-')   
              ( OO ).-.( '.( OO )_   _(  OO)                        _(OO  )_  _(  OO)( \( -O )  
  ,----.      / . --. / ,--.   ,--.)(,------.       .-'),-----. ,--(_/   ,. \(,------.,------.  
 '  .-./-')   | \-.  \  |   `.'   |  |  .---'      ( OO'  .-.  '\   \   /(__/ |  .---'|   /`. ' 
 |  |_( O- ).-'-'  |  | |         |  |  |          /   |  | |  | \   \ /   /  |  |    |  /  | | 
 |  | .--, \ \| |_.'  | |  |'.'|  | (|  '--.       \_) |  |\|  |  \   '   /, (|  '--. |  |_.' | 
(|  | '. (_/  |  .-.  | |  |   |  |  |  .--'         \ |  | |  |   \     /__) |  .--' |  .  '.' 
 |  '--'  |   |  | |  | |  |   |  |  |  `---.         `'  '-'  '    \   /     |  `---.|  |\  \  
  `------'    `--' `--' `--'   `--'  `------'           `-----'      `-'      `------'`--' '--' 
    
    
    """)
    # Call restart function
    time.sleep(1)
    restart()
# Define check pain function
def check_pain():
    global pain
    time.sleep(1)
    # hurts you (adds pain)
    pain +=1
    if pain <= 2 :
        # If you have only been hurt once
        print(r"""
                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /
            """)      
        print("It hurt but you will live")
        time.sleep(2)
    elif pain >= 3:
        # If you have been hurt twice
        print("It hurt a little too much.")
        time.sleep(1)
        print("Hurting yourself for this pear is not worth it.")
        time.sleep(1)
        print("You will just have to settle for grass, but you are still hangry")
        time.sleep(1)
        # Call game over function
        game_over()
# tells you that you've won, asks if you want to restart
def win_game():
    print("All that hard work has finally paid off!")
    time.sleep(1)
    print("The prickly pear tastes just as amazing as you thought it would")
    time.sleep(1)
    print("You sit down and smile, the hangriness has finally gone.")
    time.sleep(1)
    print("""
           A--A
       .-./   #\.-.
      '--;d    b;--'
         \# \/  /
          \\'--'/
           |==|
           | #|
           |# |
          /   #\\
         ;   #  ;
         | #    |
        /|  ,, #|\\
       /#|  ||  | \\
   .-.'  |# ||  |# '.-.
  (.=.),'|  ||# |',(.=.)
   '-'  /  #)(   \  '-'
        `""`  `""`
    """)
    print("YOU WIN!")
    restart()
def ask_about_escape():
    # asks the question
    response = input("A - Climb out / B - Wrap neck around branch and pull > ")
    # if user answers a hurt them and continue story
    if response.upper() == "A":
        print("Oh no while climbing out you broke a nail!")
        # check pain
        check_pain()
        print("You wrap your neck around the branch and pull yourself out")
        win_game()
        #win game!
    elif response.upper() == "B":
        print("You wrap your neck around the branch and pull yourself out")
        time.sleep(1)
        #win game!
        win_game()
    else:
        #repeat until a or b answered
        print("please enter either A or B")
        ask_about_escape()
def escape_pit():
    #prints the story
    print("")
    print("After failing the riddle three times a pit opens up below you and you fall in OUCH")
    time.sleep (2)
    print("You see a tree branch overhead")
    time.sleep(1)
    print("should you A - Climb out using your hooves or B - Wrap your neck around the branch and pull yourself out?")
    #starts user input
    ask_about_escape()
op_4 ="A"
op_5= "B"
op_6= "C"
def ask_about_queue ():
    what_answer = input ("A - herd, B - tower C - gang > ") 
    #if user enters herd
    if what_answer.upper() == op_4:
        print (" If you are meaning that we are all buffalos, then yes. But no, we are not a herd. Wrong answer")
        print (" You Cant be a giraffe!, Your not one of us!")
        #calls game over
        game_over()
    # if user enters tower
    elif what_answer.upper() == op_5:
        print ("YOU ARE A GENIUS. YOU WIN!")
        #calls win game
        win_game()
    # if user enters gang
    elif what_answer.upper() == op_6:
        print ("It may look like it, but no, we aren't definitely a gang.")
        print (" You Cant be a giraffe!, Your not one of us!")
        #calls game over
        game_over()
    else:
        #restarts this function till correct word entered
        print ("please enter herd/tower/gang")
        ask_about_queue()
def queue():
    #prints story
    print("")
    print ("You passed the challenge with flying colours and are one neck closer to the prickly pear")
    time.sleep(1)
    print ("... But oh no! There is a queue just to get there. After all, all giraffes must be hungry too!!")
    time.sleep(1)
    print (" Now you think about it, do you know the name of a group of giraffes?")
    time.sleep(1)
    #calls input function
    ask_about_queue()
# declares riddle attempts
attempts = 0
def riddle_question_again():
    #adds one attempt
    global attempts
    attempts +=1
    response = input ("Please enter a number > ")
    #if correct answer
    if response == "8":
        print ("Excellent, continue to winners path")
        queue()
    #if incorrect answer 3 times
    elif attempts == 3:
        print("You have failed too many times!")
        escape_pit()
    # incorrect answer starts function again
    elif response !="8":
        print("Attempt: {} - incorrect!".format(attempts))
        riddle_question_again() 
def riddle():
# asks riddle
    print("")
    print ("Finally, the food at the end of the savannah.  But first, you must solve the riddle made by the Wise Monkey")
    time.sleep(1)
    print("")
    time.sleep(1)
    print ("so, you walk into a room and see a bed.") 
    print ("On the bed, there are 2 hyenas, 4 leopards, a giraffe, 5 buffalos, and a flamingo. There are also 3 marabous flying above the bed. How many legs are on the floor?")
    riddle_question_again()
op_1 ="A"
op_2= "B"
op_3= "C"
def ask_about_poachers():
    response = input ("A - headbutt, B - run, C - roar > ") 
    # if user enters headbutt
    if response.upper() == op_1:
        print ("A very unfair battle.")
        game_over()
    #if user enters run
    elif response.upper() == op_2:
        print ("You can run, but you can't hide. They shot you!")
        check_pain()
        # go to lost a life option
        riddle()
    #if user enters roar
    elif response.upper() == op_3:
        print ("The entire savannah heard it. The poacher got so scared, he ran away. Nice one.")
      # move forward to next level in the game
        riddle()
    # if incorrect word enter
    else: 
        print ("please enter A - headbutt B, - run, C - roar")
        ask_about_poachers ()
def poachers ():
    # prints story
    print("")
    print ("After a wonderful 20 minute nap, you wake up.")
    time.sleep (1)
    print ("OMG- there's a poacher right in front of you, ready to take you down.")
    time.sleep (1)
    print("What do you do?")
    time.sleep (1)
    # calls user input
    ask_about_poachers ()
# Asks the question
def ask_about_sleep():
    # Declares response variable which is passed the user input
    response = input("A = 20min nap B - 1 hour sleep > ")
    # if user enters 20 go to challenge 3
    if response.upper() == "A":
        print("You fall asleep...")
        time.sleep(1)
        print("zzz")
        time.sleep(1)
        poachers()
    # else if the user enters long go to game over screen
    elif response.upper() == "B":
        print("You fall asleep...")
        time.sleep(1)
        print("zzz")
        time.sleep(1)
        print("You wake up and OMG its dark, all the prickly pears will be gone!")
        time.sleep(1)
        print("You will just have settle for grass, but you are still hangry")
        # go to game over
        game_over()
    # otherwise repeat this method
    else:
        print("Please enter either A - 20min nap or B - 1 hour sleep")
        ask_about_sleep()
# Starts introduction
def sleepy_time():
    print("")
    print("After the experience with the lion, You are starting to feel quite sleepy")
    time.sleep(1)
    print("The problem is, a short nap will still leave you feeling a little tired")
    time.sleep(1)
    print("Should you sleep for 20 mins or longer?")
    time.sleep(1)
    # Starts user input
    ask_about_sleep()
def ask_about_lion():
    time.sleep(1)
    response = input ("A = Tugs his mane, B = sits down with Roger, C = kicks him up the bum > ")
    #if user enters a
    if response.upper() == "A":
        print ("A fight takes place, you are injured, continue with chunk missing from leg")
        #hurts user
        check_pain()
        sleepy_time()
    #if user enters b
    elif response.upper() == "B":
        print("""
              \-._,, /"/
               "-/  l-'
                 \  /\_
                 | /\  \\
                (_/  \  %----.__
                      \/ ___    \\
                    ,'  /   '-.__|_
                    |   \'-.___    \\
                     \__ '/   _/\_  '-.
                        \/   /-.  \_   \\
                        /   |   \_  \   |
                       /   / \_   '-'   /
                      |    |   '-.___,-'
                    ,-'     \\
                   /         "-._
                   |             '-._
                    \                \\
                    | \               |-.
                    \  | /'-._,-|    /   \\
                     | \ |      \    |    $
                     \ | /       |  /
                      | /         \ |
                      |/           |/
        """)
        print ("Roger is a great liar, when you sit next to him, he ties your neck into a bow!")
        time.sleep(2)
        game_over()
    #if user enters c
    elif response.upper() == "C":
        print ("Roger Roars in anger, but runs away as his bum is hurting")
        sleepy_time()
    #repeats until a correct answer entered
    else:
        ask_about_lion()
def challenge_lion():
    print("""
     ,/^\'-~-`/^\,
    {(3)       (E)}
  ,(- __\     /__ -),
,{    =*.;   ;.*=    },
{   /   \  |  /   \   ),
` /      / | \      \  }
` /  -~~(.,Y,.)~~-  \  }
{  /     (^"^)     \  }'
`{,  /     ~     \  ,}'
 \`{\_/         \_/}'/
  >_ _`\,,/|\,,/'_ _<
 `(}(}(} `~-~' {){){)'
    """)
    #prints story
    print ("The King of the Savannah Roger Lion, was relaxing by the river when he heard a rustle in the grass.")
    time.sleep(1)
    print ("As Roger took a full body stretch he could not believe his eyes, a Hangry Giraffe was standing over him.  He decided to play it cool")
    time.sleep(3)
    name = input ("What is your name?  Asks Roger. > ")
    print("")
    print ("How lovely to meet you, {}".format (name))
    time.sleep(2)
    print ("Would you like to join me")
    #calls user input function
    ask_about_lion()
def introduction():
    #prints opening
    print("""
             _______  _        _______  _______             _______ _________ _______  _______  _______  _______  _______ 
   |\     /|(  ___  )( (    /|(  ____ \(  ____ )|\     /|  (  ____ \\__   __/(  ____ )(  ___  )(  ____ \(  ____ \(  ____  \\
   | )   ( || (   ) ||  \  ( || (    \/| (    )|( \   / )  | (    \/   ) (   | (    )|| (   ) || (    \/| (    \/| (    \/
   | (___) || (___) ||   \ | || |      | (____)| \ (_) /   | |         | |   | (____)|| (___) || (__    | (__    | (__    
   |  ___  ||  ___  || (\ \) || | ____ |     __)  \   /    | | ____    | |   |     __)|  ___  ||  __)   |  __)   |  __)   
   | (   ) || (   ) || | \   || | \_  )| (\ (      ) (     | | \_  )   | |   | (\ (   | (   ) || (      | (      | (      
   | )   ( || )   ( || )  \  || (___) || ) \ \__   | |     | (___) |___) (___| ) \ \__| )   ( || )      | )      | (____/\\
   |/     \||/     \||/    )_)(_______)|/   \__/   \_/     (_______)\_______/|/   \__/|/     \||/       |/       (_______/
""")
    print ("Once upon a time, in wild vast African savanna")
    time.sleep(1)
    print ("There was a Hangry Giraffe")
    time.sleep(1)
    print ("She was on a quest through the wild to get her favourite treat: a prickly pear.")
    time.sleep(1)
    
print ("")
def start_game():
    introduction()
    answer = input ("Would you like to start?[Y/N] > ")
    #if user says yes
    if answer.upper() == "Y":
        print(r"""
                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /
            """)   
        print("Great, let's start then")
        print("")
        #goes to first challenge
        challenge_lion()
    #if user says no
    elif answer.upper() == "N":
        print("So selfish...You are going to leave her hangrier.")
        #closes game
        sys.exit()
    #repeats until user enters yes/no
    else:
        print("Error. Giraffe not found")
        start_game()
#starts program
start_game()
