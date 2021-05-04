life = 3
def tru_fal():
    true_or_false_qa_list = [
        ['Prince Harry is taller than Prince William',  'f',],
        ['The star sign Aquarius is represented by a tiger', 'f' ],
        ['Meryl Streep has won two Academy Awards', 'f'],
        ['Marrakesh is the capital of Morocco', 'f'],
        ['Waterloo has the greatest number of tube platforms in London', 't'],
    ]

    def start_game():
        global life

        if life > 0:
            print(true_or_false_qa_list[0][0])
            if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_list[0][1]:
                print("And Harry had better remember that!")
            else:
                print("YOU LET ME DOWN, YOU LET OUR MONARCH DOWN, BUT MOST OF ALL ... YOU LET YOURSELF DOWN!")
                life -= 1
            print(f"You have {life} left")
        else:
            input("This is the end for you ... dare you continue? y or n : ")
        
        if life > 0:
            print(true_or_false_qa_list[1][0])
            if input("TRUE or FALSE! Enter t or f: ") in true_or_false_qa_list[1][1]:
                print("SOOOO correct")
            else:
                print("YOU COULDN'T BE ANYMORE WRONG, YOU COULD TRY, BUT YOU WOULD FAIL!")
                life -= 1
                print(f"You have {life} left")
        else:
            input("This is the end for you ... dare you continue? y or n : ")

        if life > 0:
            if input(f"OK, what about this: {true_or_false_qa_list[2][0]}: ") in true_or_false_qa_list[2][1]:
                print("Wowzers trouserssssss")
            else:
                print("DON'T BE A DINGBAT!")
                life -= 1
                print(f"You have {life} left")
        else:
            input("This is the end for you ... dare you continue? y or n : ")

        if life > 0:
            if input(f"TRUE or FALSE! {true_or_false_qa_list[3][0]}. Enter t or f : ") in true_or_false_qa_list[3][1]:
                print("Tick-et-E-booOOOo!")
            else:
                print("I think I have found a new use for the hi-five emoji ... he can take your place in this quiz!")
                life -= 1
                print(f"You have {life} left")
        else:
            input("This is the end for you ... dare you continue? y or n : ")

        if life > 0:
            if input(f"Take a breath, compsose yourself ... {true_or_false_qa_list[4][0]}: ") in true_or_false_qa_list[4][1]:
                print("SSSSMMMMOOOKKKKING!")
            else:
                print("Only dogs can hear my screams now!")
                life -= 1
                print(f"You have {life} left")
            
                print(f"You have {life} to continue with... ")
        else:
            input("This is the end for you ... dare you continue? y or n : ")
            if input == "y":
                start_game()
            else:
                exit
    start_game()