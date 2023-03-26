import time
import sys

def main():
    figure_questions = ["'Where am I?'", "'Who are you?'", "'What happened to me?'", "'What lies beyond this gate?'"]
    time.sleep(5)
    print("You awaken, not knowing where you are and having no memory of past events...")
    time.sleep(3)
    print("You observe a barren landscape, the horizon touching an infinitely darkened land...")
    time.sleep(3)
    print("the faint glimmer of the rays of a mysterious light source is the only thing keeping you from not being able to see...")
    time.sleep(3)
    print("But you are drawn to an obscured structure in the distance, beckoning you to come near...")
    time.sleep(2)
    print("And you approach what appears to be a gate. Worn. Rusted. It even seems as though it would be venomous to the touch, yet you do not understand why...")
    time.sleep(4)
    print("A deep voice breaks the silence, and you understand the spoken words:")
    time.sleep(1)
    print("'Someone at the door, worthy of the gift of Death, but do they lack the courage to accept it?'")
    time.sleep(4)
    escape_choice = input("You are suddenly afraid, but do you choose to run?\n")
    if escape_choice == "yes":
        time.sleep(4)
        print("You ran as fast as your crumbling legs could take you. You did not choose to accept the gift that the mysterious figure spoke of...")
        time.sleep(2)
        print("In the world beyond, blackened ichor filled a crumbling sky, as the remnants of your sould withered to nothing...")
        time.sleep(5)
        sys.exit()
    if escape_choice == "no":
        time.sleep(4)
        print("You decide to push your fear back inside of you. You then wish to question the mysterious figure...")
        time.sleep(2)
        first_questions(figure_questions)
        
        
def first_questions(figure_questions):
    print("Questions:")
    time.sleep(2)
    for question in figure_questions:
            time.sleep(1)
            print(str(question))
    time.sleep(2)
    asking_figure = input("What question do you ask this mysterious figure?:\n")

    if asking_figure == "Where am I?":
         where_am_i()
    
    if asking_figure == "Who are you?":
         who_are_you()
    
    if asking_figure == "What happened to me?":
        what_happened_to_me(figure_questions)

    if asking_figure == "What lies beyond this gate?":
        what_lies_beyond_gate()
     
    
def where_am_i():
     time.sleep(5)
     print("The msyteriosu figure speaks: 'Even I do not know or understand...'")
     time.sleep(1)
     print("'All I ever knew and will know of this dark place is misery, and how it is known as The Sunless Lands. Mortal, you are no longer on the plane on which you lived your life.'")
     time.sleep(3)
def who_are_you():
    time.sleep(5)
    print("The mysterious figure speaks: 'I am merely a guardian, a gate-watcher of the realm beyond'")
    time.sleep(1)
    print("'Few who come here get past me, but all they will know beyond this point is suffering'")
    time.sleep(3)

def what_happened_to_me(figure_questions):
    time.sleep(5)
    print("The mysterious figure speaks: 'Dear mortal, even though you may not remember it now, you were a bringer of pain and suffering in your realm, with a cruel spirit and a wicked heart.'")
    time.sleep(1)
    print("'But an ally who you thought loyal to you and your cause betrayed you.'")
    time.sleep(2)
    print("'Death was sent to find you and bring you here, and once Death takes mortals to the Sunless Lands, the only way is forward.'")
    time.sleep(3)
    print("You are still confused, but now you are beginning to understand that you died in a past life, even though you may not remember...")
    time.sleep(2)
    print("But you are shocked at the fact that you were once a very bad person...")
    time.sleep(2)
    print("The mysterious figure speaks: 'Well, mortal? Do you wish to proceed?'")
    time.sleep(3)
    print("Hesistant, you would like to ask this mysterious figure one more question: ")
    for question in figure_questions:
        time.sleep(1)
        print(str(question))
    time.sleep(2) 
    input("What would you like to ask?: ")

def what_lies_beyond_gate():
     time.sleep(5)





if __name__ == "__main__":
    main()