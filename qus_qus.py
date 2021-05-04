def tru_fal_b():
    true_or_false_qa_listb = [
        ['Paris is the captial of France: ', 't'],
        ['England is an island:', 'f'],
        ['M&M stands for Mars and Moordale: ', 'f'],
        ['Andorra is between France and Spain: ', 't'],
        ['Iran use to be part of the Perisan Empire: ', 't'],
    ]

    def start_game_b():
        life = 3
        cont = 2
        while (life > 0):
            print(true_or_false_qa_listb[0][0])
            if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[0][1]:
                print("Oui... Bon, Tres Bien!")
            else:
                print("Je déteste cette réponse! ... Not the favourable answer!")
                print("WRONG!!!")
                life -= 1
                print(f"You have {life} left")

            print(true_or_false_qa_listb[1][0])
            if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[1][1]:
                print("OK! You have some skill. Let us see where this goes.")
            else:
                print("Not even Wakanda could save you with this performance!")
                life -= 1
                print(f"You have {life} left")

            print(true_or_false_qa_listb[2][0])
            if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[2][1]:
                print("Don't get Cocky! ")
            else:
                print("You have only gone and blown'... the bloody door off'!")
                print("Wrong!")
                life -= 1
                print(f"You have {life} left")

            print(true_or_false_qa_listb[3][0])
            if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[3][1]:
                print("Good, but can you do it with a distraction? ")
            else:
                print("You have failed this city ...")
                life -= 1
                print(f"You have {life} left")

            print(true_or_false_qa_listb[4][0])
            if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_listb[4][1]:
                print("You may have made it through this stage. Know this ...")
                print("There is more to come.")
            else:
                print("I fear that you will be spooning with the Minotaur ... if you are lucky")
                life -= 1
                print(f"You have {life} left")
            
                print(f"You have {life} to continue with... ")
                break
            break
    start_game_b()