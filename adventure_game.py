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
    print("'Someone at the door, worthy of the gift of Death, but do they lack courage to accept it?'")
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
        time.sleep(3)
        first_questions()
        
        
def first_questions(figure_questions):
    print("Questions:")
    time.sleep(2)
    for question in figure_questions:
            print(str(question))
    time.sleep(2)
    asking_figure = input("What question do you ask this mysterious figure?:\n")



if __name__ == "__main__":
    main()