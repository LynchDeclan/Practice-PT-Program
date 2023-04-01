import time
import sys

def main():
    figure_questions = ["[Where am I?]", "[Who are you?]", "[What happened to me?]", "[What lies beyond this gate?]"]
    time.sleep(3)
    print("You awaken, not knowing where you are and having no memory of past events...")
    time.sleep(2)
    print("You observe a barren landscape, the horizon touching an infinitely darkened land, overshadowed by grey clouds...")
    time.sleep(2)
    print("the faint glimmer of the rays of a mysterious light source is the only thing keeping you from not being able to see...")
    time.sleep(2)
    print("But you are drawn to an obscured structure in the distance, beckoning you to come near...")
    time.sleep(2)
    print("And you approach what appears to be a gate. Worn. Rusted. It even seems as though it would be venomous to the touch, yet you do not understand why...")
    time.sleep(3)
    print("A deep voice breaks the silence, and you understand the spoken words:")
    time.sleep(1)
    print("'Someone at the door, worthy of the gift of Death, but do they lack the courage to accept it?'")
    time.sleep(3)
    escape_choice = input("You are suddenly afraid, but do you choose to run?\n")
    if escape_choice[0] in ["Y","y"]:
        time.sleep(3)
        print("You ran as fast as your crumbling legs could take you. You did not choose to accept the gift that the mysterious figure spoke of...")
        time.sleep(2)
        print("In the world beyond, blackened ichor filled a crumbling sky, as the remnants of your sould withered to nothing...")
        time.sleep(4)
        sys.exit()
    if escape_choice[0] in ["N","n"]:
        time.sleep(3)
        name = str(input("You decide to push your fear back inside of you. The mysterious figure suddenly speaks again: 'What is your name, mortal?'\n"))
        time.sleep(2)
        print("You tell the mysterious figure a name you suddenly remembered, in that moment, as your own: " +name+ " but it doesn't really feel like you remember...")
        print("It feels to you as though your mind is being played on by another force, something foreign, twisting your thoughts and making you belive things that you know, deep inside, are true about you.,.")
        time.sleep(2)
        first_questions(figure_questions, name)
        
        
def first_questions(figure_questions, name):
    print("Questions:")
    time.sleep(2)
    for question in figure_questions:
            time.sleep(1)
            print(question)
    time.sleep(2)
    asking_figure = input("What question do you ask this mysterious figure, " +name+ "?:\n")

    if asking_figure == "Where am I?":
         where_am_i()
    
    if asking_figure == "Who are you?":
         who_are_you()
    
    if asking_figure == "What happened to me?":
        what_happened_to_me(figure_questions, asking_figure)

    if asking_figure == "What lies beyond this gate?":
        what_lies_beyond_gate()
     
    
def where_am_i():
     time.sleep(4)
     print("The msyteriosu figure speaks: 'Even I do not know or understand...'")
     time.sleep(1)
     print("'All I ever knew and will know of this dark place is misery, and how it is known as The Sunless Lands. Mortal, you are no longer on the plane on which you lived your life.'")
     time.sleep(3)
     print("'Here you are, in this realm, on the threshold to the barren, dark lands, of Hell...'")
     time.sleep(2)
     print("You are terrified, and speechless. You know not what to say, for you have just discovered that the realm of eternal damnation exists.")
     time.sleep(2)
     print("And you know it to be true. The feeling that you have had since you awakened has almost completely taken over... You are brought to your knees. You know there is no choice but onward...")
     time.sleep(2)
     print("The mysterious figure speaks one last time before you go through the gates: 'Mortal, take these souls of the iniquitous, relics, before you proceed. Collect more thoughout your journey. They are the key to reedeming yourself. Just take 100 to her majesty...'")
     time.sleep(2)
     print("Your objective is sealed. It is now your mission to collect 100 souls in the realm beyond. You feel the realm of eternal damnation before you. The cries of the souls of demons echo through your mind...")
     time.sleep(1)
     print("The voices in your head tell you that there are different types of demon souls. They tell you to be careful of the types you collect...")
     time.sleep(2)
     
def who_are_you():
    time.sleep(4)
    print("The mysterious figure speaks: 'I am merely a guardian, a gate-watcher of the realm beyond'")
    time.sleep(1)
    print("'Few who come here get past me, but all they will know beyond this point is suffering'")
    time.sleep(2)
    print("'You have asked me the wrong question, mortal. You needn't know who I am. Now you must answer a riddle...'")
    time.sleep(2)
    print("The gate-keeper gives you his riddle: 'I can fly but have no wings. I can cry, but I have no eyes. Wherever I go, darkness follows me. What am I?'")
    time.sleep(1)
    print("[answer him]")
    print("[hint]")
    time.sleep(1)
    riddle = input("Do you wish to answer? Or do you wish to spend your single opportunity at a hint?:\n")

    if riddle == "answer him":
         time.sleep(1)
         answer_riddle = input("What is your answer to this riddle?:\n")
         if answer_riddle in ["Cloud", "A cloud", "cloud", "a cloud"]:
              time.sleep(2)
              print("The figure speaks: 'Alas! Your answer is correct! Smarter than I thought...'")
              time.sleep(2)
              print("The mysterious figure speaks one last time before you go through the gates: 'Mortal, take these souls of the unworthy, relics, before you proceed. Collect more thoughout your journey. They are the key to reedeming yourself. Just take 100 to her majesty...'")
              time.sleep(1)
              print("'...in the realm of eternal damnation... Hell.'")

    if riddle == "hint":
         time.sleep(2)
         print("The figure speaks: 'You are slightly dissapointing... Oh well, your hint is: I am all around you, overhsadowing everything...'")
         time.sleep(1)
         answer_riddle = input("What is your answer to this riddle?:\n")
         if answer_riddle in ["Cloud", "A cloud", "cloud", "a cloud"]:
              time.sleep(2)
              print("The figure speaks: 'Alas! Your answer is correct! Smarter than I thought...'")
              time.sleep(2)
              print("The mysterious figure speaks one last time before you go through the gates: 'Mortal, take these souls of the unworthy, relics, before you proceed. Collect more thoughout your journey. They are the key to reedeming yourself. Just take 100 to her majesty...'")
              time.sleep(1)
              print("'...in the realm of eternal damnation... Hell.'")

    

def what_happened_to_me(figure_questions, asking_figure):
    time.sleep(4)
    print("The mysterious figure speaks: 'Dear mortal, even though you may not remember it now, you were a bringer of pain and suffering in your realm, with a cruel spirit and a wicked heart.'")
    time.sleep(1)
    print("'But an ally who you thought loyal to you and your cause betrayed you.'")
    time.sleep(2)
    print("'Death was sent to find you and bring you here, and once Death takes mortals to the Sunless Lands, the only way is forward.'")
    time.sleep(3)
    print("You are still confused, but now you are beginning to understand that you died in a past life, even though you may not remember...")
    time.sleep(2)
    print("But you are shocked at the fact that you were once a cruel person...")
    time.sleep(2)
    print("The mysterious figure speaks: 'Well, mortal? Do you wish to proceed?'")
    time.sleep(2)
    print("You know not what lies beyond these gates, but you suddenly feel compelled to continue...")
    time.sleep(2)
    print("The mysterious figure speaks one last time before you go through the gates: 'Mortal, take these souls of the unforgiven, relics, before you proceed. Collect more thoughout your journey. They are the key to reedeming yourself. Just take 100 to her majesty...'")
    time.sleep(2)
    print("Your objective is sealed. It is now your mission to collect 100 souls in the realm beyond. You feel the realm of eternal damnation before you. The cries of the souls of demons echo through your mind...")
    time.sleep(1)
    print("The voices in your head tell you that there are different types of demon souls. They tell you to be careful of the types you collect...")
    time.sleep(2)

def what_lies_beyond_gate():
     time.sleep(4)
     print("The mysterious figure speaks: 'Dear mortal, this gate is what you have been comdemned to go through by her majesty, who was handed conmtrol over your sould as soon as you passed on from the mortal realm...'")
     time.sleep(2)
     print("'Beyond this gate, lies the realm of eternal damnation. I am sure you know what this is...'")
     time.sleep(2)
     print("You do, indeed, know what the mysterious figure is talking about... The voices in your head get louder and louder... You were a sinner in the mortal realm...")
     time.sleep(2)
     print("What lies beyonmd this gate, you know, is the realm of Hell.")
     time.sleep(2)
     print("The mysterious figure speaks one last time before you go through the gates: 'Mortal, take these souls of the iniquitous, relics, before you proceed. Collect more thoughout your journey. They are the key to reedeming yourself. Just take 100 to her majesty...'")
     time.sleep(2)





if __name__ == "__main__":
    main()