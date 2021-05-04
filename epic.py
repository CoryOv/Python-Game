life = 3


import random
import time       

multiple_choice_1 = [["What is the capital of New Zealand? \nWellington, Christchurch, Auckland or Queenstown: ", "Wellington"], 
["What is the capital of Australia? \nPerth, Sydney, Canberra or Melbourne: ", "Canberra"], 
["Who is the Greek God of the forge? \nApollo, Hephaestus, Zeus or Hermes: ", "Hephaestus"], 
["Which of these is not an ocean? \nIndian, Arctic, Mediterranean or Pacific: ", "Mediterranean"], 
["Which player has scored the most Premier League goals? \nAlan shearer, Wayne rooney, Darren bent or Emile heskey: ", "Alan shearer"]
]

multiple_choice_2 = [["What is the capital of Germany? \nCologne, Berlin, Hamburg or Munich: ", "Berlin"],
["What is the capital of Spain? \nBarcelona, Madrid, Seville or Valencia: ", "Madrid"],
["Which of these is not an element? \nAmericium, Einsteinium, Unobtanium or Mendelevium: ", "Unobtanium"], 
["In the movie \"Blade Runner\", what is the term used for human-like androids? \nReplicants, Skinjobs, Cylons or Synthetics: ", "Replicants"],
["Which player has made the most Premier League appearances? \nRyan giggs, Gareth barry, Mark noble or Petr cech: ", "Gareth barry"]
]

multiple_choice_3 = [["What is the capital of Canada? \nVancouver, Toronto, Montreal or Ottawa: ", "Ottawa"],
["Which country won the first ever Football World Cup in 1930? \nBrazil, Uruguay, Spain or Portugal: ", "Uruguay"],
["The Space Needle is located in which city? \nLos angeles, San diego, Dallas or Seattle: ", "Seattle"], 
["Leonardo Di Caprio won his first Best Actor Oscar for his performance in which film? \nThe revenant, The wolf of wall street, Shutter island or Inception: ", "The revenant"], 
["According to legend, what item is most effective against werewolves? \nGold, Silver, Bronze or Platinum: ", "Silver"]
]

riddle1 = [["What is always in front of you but can’t be seen? \n My Nose, The Future or Horizon: ", "The future"],
[" What can you break, even if you never pick it up or touch it? \n Silence, Glass, Wind:", "Silence"],
[" I have branches, but no fruit, trunk or leaves. What am I? \n A Vine, A Bank or The Apple Store: ", "A bank"],
["What can you catch, but not throw? \n A Thief, An STI or A Cold: ", "A cold"],
["What has to be broken before you can use it?\n An Egg, Virginity or A Seal", "An egg"],
]

riddle2 = [["I'm tall when I'm young, and I'm short when I'm old. What am I? \nCandle, Tree or Curtains", "Candle"],
["what goes up but never comes down? \nBalloon, Age or Gravity", "Age"],
["The more of this there is, the less you see. What is it? \nCheese, Light or Darkness", "Darkness"],
["What can travel all around the world without leaving its corner? \nGlobe, Stamp or Bill Murray", "Stamp"],
["What question can you never answer yes to? \nAre you awake, Do you know the muffin man or Are you asleep", "Are you asleep"]]

riddle3 = [["What can you break, even if you never pick it up or touch it? \nYour mother's heart, A Promise or Wind: ", "A promise"],
["What has 13 hearts, but no other organs? \nA Deck of Cards, A Cabbage or The Hydra: ", "A deck of cards"],
["What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps? \nA River, Sirian Bath or Brush", "A river"],
["What can fill a room but takes up no space? \n A Soul, Light or a Memory", "A light"],
["What has one eye, but can’t see? \n An Orc, A Vulcan or a Needle: ", "Needle"],
]

lives = 3

def riddle_me_lis():
    lives = 3
    print("Please check all of your spelling!")
    chosen = int(input("Which set of questions would you like to try? 1, 2 or 3: "))
    while lives > 0:
        if chosen == 1:
            print(riddle2[0][0])
            if input().capitalize() in riddle2[0]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            print(riddle2[1][0])
            if input().capitalize() in riddle2[1]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            print(riddle2[2][0])
            if input().capitalize() in riddle2[2]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
            print(riddle2[3][0])
            if input().capitalize() in riddle2[3]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
            print(riddle2[4][0])
            if input().capitalize() in riddle2[4]:
                print("Well done you fucking cleverclogs")
                print("You have completed the test, you may continue through.")
                print("Shhhiiiiiitttttt! We never thought you would get here ... you took the onlyh path that dodges all bugs. Hang about for the sequal and we will eventually let you leave")
                print("Way to go little guy!")
                exit()
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                    exit()
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

        if chosen == 2:
            print(riddle3[0][0])
            if input().capitalize() in riddle3[0]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            print(riddle3[1][0])
            if input().capitalize() in riddle3[1]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            print(riddle3[2][0])
            if input().capitalize() in riddle3[2]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
            print(riddle3[3][0])
            if input().capitalize() in riddle3[3]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
            print(riddle3[4][0])
            if input().capitalize() in riddle3[4]:
                print("Well done you fucking cleverclogs")
                print("You have completed the test, you may continue through.")
                print("Shhhiiiiiitttttt! We never thought you would get here ... you took the onlyh path that dodges all bugs. Hang about for the sequal and we will eventually let you leave")
                print("Way to go little guy!")
                exit()
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                    exit()
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

        if chosen == 3:
            print(riddle1[0][0])
            if input().capitalize() in riddle1[0]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            print(riddle1[1][0])
            if input().capitalize() in riddle1[1]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            print(riddle1[2][0])
            if input().capitalize() in riddle1[2]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
            print(riddle1[3][0])
            if input().capitalize() in riddle1[3]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
            print(riddle1[4][0])
            if input().capitalize() in riddle1[4]:
                print("Well done you fucking cleverclogs")
                print("You have completed the test, you may continue through.")
                print("Shhhiiiiiitttttt! We never thought you would get here ... you took the onlyh path that dodges all bugs. Hang about for the sequal and we will eventually let you leave")
                print("Way to go little guy!")
                exit()
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                    exit()
            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    riddle_me_lis()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

def opening():

    # name = input("Please enter your name: ")
    name = input("Please enter your name: ")
    print(f"{name}... last night was strange, everything is a blur ..."),
    time.sleep(2)
    print("You clear your eyes and look around the room ... this is NOT your bedroom"),
    time.sleep(2)
    print("The place is dark and damp and smells almost like 'dog'"),
    time.sleep(2.5)
    print("There are three doors, one on the left and two doors on the right"),
    time.sleep(3)
    print("you open the door on the left ... "),
    time.sleep(2)
    print("GRRRRRRR roars through the corridor in front of you,coming from a frightening shadow"),
    time.sleep(3.5)
    print("GRRRRRRRRRRRRR it is coming straight for you you can "),
    print("1. Stay around and maybe do some Yoga. 2. Slam the door and head for the other two doors"),

    user = int(input("Choose 1 or 2: "))
    if user == 1:
        print("You start with Namaste ... If anything, ... , it seems angrier, you turn and bolt for the other doors")
    elif user == 2:
        print("You are on the ball, the door is slammed shut and you sprint in the opposite direction")
    else:
        print("Please Check your input, else we may have to leave you here for the Minotaur's pleasures")
        time.sleep(2)
        print("Still not safe you must now choose door number 1, or door number 2 ...")
        print(" You must choose door 1 or 2: ")
    user = int(input("Which will you choose? door 1 or door 2: "))
    if user == 1:
        print(f"There is a flash of light and a tall slim being with an elaborate green necklace, stares at you {name}...")
        print("You must answer five questions to pass ...")
        import tf_totty
        tf_totty.tru_fal()

    elif user == 2:
        print(f"There is a flash of light and a tall slim being with an elaborate green necklace, stares at you {name}...")
        print("You must answer five questions to pass ...")
        import quz_qus
        quz_qus.tru_fal_b()
    else:
        print(f"Whilst we acknowledge {name}, that you may have 'The Fear', we can only help if you choose 1 or 2. Your cooperation in this matter is appreciated. K.R - The Overlords")

opening()

print("You are breathing heavily but there os no time to dwell ...")
time.sleep(2.5)
print("The room you are in smells like the PE lost and found from your old school")
time.sleep(2)
print("The room has one door straight ahead and one to the right ... ")
time.sleep(1.5)
print("GRRRRRRRROOOOOAAAAAARRRRRRR ... the sound echos through you")
time.sleep(2)
print("You can almost feel the ground trembling")
time.sleep(2)
print("There is no time to dwell, you must pass through the door ... simple it seems or is there a floor?")
time.sleep(3)
print("You must answer 5 questions to pass ...")



def two_complete():
        print("You have arrived in a long hallway, it is unlike any of the other paths that you have seen so far ...")
        time.sleep(2)
        print("There is just one door at the end ...")
        time.sleep(2)
        print("But there is a haze around the door")
        time.sleep(3.5)
        print("You are trying to see through the haze ...")
        time.sleep(2.5)
        print("CRASH! The door behind you almost gives,") 
        print("The beast is no longer growling, it has stopped ...") 
        time.sleep(1.5)
        print("it is sniffing and ...")
        time.sleep(2)
        print("It almost sounds like it is sniggering at you ...")
        time.sleep(2.5)
        print("You hear footsteps fading ... it is moving away!")
        time.sleep(2)
        print("The steps are fading")
        time.sleep(2.75)
        print("Relief fills your body, you lean against the door and take a breath")
        time.sleep(3.25)
        print("Looking down the hall, the haze has now parted to reveal ...")
        time.sleep(3.75)
        print("PEOPLE! There appear to be people gathered here ... There may be hope yet!")
        time.sleep(4.5)
        print("But ... You rested a little too long ...")
        time.sleep(2)
        print("CRASH!")
        time.sleep(0.75)
        print("BANG!")
        time.sleep(0.75)
        print("WALLOP!!!")
        time.sleep(1)
        print("The Minotaur has crashed through the door sending you flying towards the gathering.")
        time.sleep(3.5)
        print("You look up and see the Minotaur almost in touching distance")
        time.sleep(3)
        print("Fortune is in your favour  ... his horns are stuck in a large portion of the door,")
        time.sleep(3)
        print("You quickly rise to your feet and sprint towards the people at the next door")
        time.sleep(5)
        print("You can see the figures clearly ... you have met two of them already")
        time.sleep(3)
        print("The man in the green necklase and the short stout man from the previous room")
        time.sleep(3)
        #### THE FINAL CHALLENGE OF THE GAME ####
        print("The tall man steps forward and the others follw suit ...")
        time.sleep(2)
        print("In unison they say... You have done well to get this far , but ")
        time.sleep(3)
        print("A final challenge is still to come, our riddles starting from 5 to 1")
        time.sleep(2.25)
        print("Answer all of them you must - else be a prisoner for always trust...")
        riddle_me_lis()
def start_game():
    lives = 3
    print("Please check all of your spelling!")
    chosen = int(input("Which set of questions would you like to try? 1, 2 or 3: "))
    while lives > 0:
        if chosen == 1:
            print(multiple_choice_1[0][0])
            if input().capitalize() in multiple_choice_1[0]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            print(multiple_choice_1[1][0])
            if input().capitalize() in multiple_choice_1[1]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            print(multiple_choice_1[2][0])
            if input().capitalize() in multiple_choice_1[2]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
            
            print(multiple_choice_1[3][0])
            if input().capitalize() in multiple_choice_1[3]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

            print(multiple_choice_1[4][0])
            if input().capitalize() in multiple_choice_1[4]:
                print("Well done you fucking cleverclogs")
                print("You have completed the test, you may continue through.")
                two_complete()
                exit()
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                    two_complete()
                    exit()

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

        elif chosen == 2:
            print(multiple_choice_2[0][0])
            if input().capitalize() in multiple_choice_2[0]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            print(multiple_choice_2[1][0])
            if input().capitalize() in multiple_choice_2[1]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            print(multiple_choice_2[2][0])
            if input().capitalize() in multiple_choice_2[2]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

            print(multiple_choice_2[3][0])
            if input().capitalize() in multiple_choice_2[3]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

            print(multiple_choice_2[4][0])
            if input().capitalize() in multiple_choice_2[4]:
                print("Well done you fucking cleverclogs")
                print("You have completed the test, you may continue through.")
                two_complete()
                exit()
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                    two_complete()
                    exit()

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

        elif chosen == 3:
            print(multiple_choice_3[0][0])
            if input().capitalize() in multiple_choice_3[0]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            print(multiple_choice_3[1][0])
            if input().capitalize() in multiple_choice_3[1]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            print(multiple_choice_3[2][0])
            if input().capitalize() in multiple_choice_3[2]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

            print(multiple_choice_3[3][0])
            if input().capitalize() in multiple_choice_3[3]:
                print("Well done you fucking cleverclogs")
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()

            print(multiple_choice_3[4][0])
            if input().capitalize() in multiple_choice_3[4]:
                print("Well done you fucking cleverclogs")
                print("You have completed the test, you may continue through.")
                two_complete()
                exit()
            
            else:
                lives -= 1
                print("shit off")
                print(f"You have lost a life! You have {lives} left.")
                if lives > 0:
                    print("Despite this, you have completed the test, you may continue through.")
                    two_complete()
                    exit()

            if lives == 0:
                print("You have run out of lives!")
                cont = input("Would you like to continue at the start of this round again? Yes or No: ")
                if cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
                    start_game()
                elif cont == "No" or cont == "N" or cont == "no" or cont == "n":
                    print("Please exit the game and play again whenever you want!")
                    exit()
start_game()
print("Shhhiiiiiitttttt! We never thought you would get here ... you took the onlyh path that dodges all bugs. Hang about for the sequal and we will eventually let you leave")
print("Way to go little guy!")
exit()
game()