from os import system
import random

def sayit(what="Hello World!", who="Victoria"):
    """Say something with the Mac text to speech feature
        what -- the string message you want to say (default = "Hello World!")
        who -- String name of built in system voice. "random" to choose one randomly
    """

    mymessage = "say " + what + " -v " + who
    system(mymessage)


def introduce(name):
    """ For testing out the different voices, "random" for random name """
    if name.upper() == "RANDOM":
        name = random_name()

    sayit("Hello, I am" + name, name)

def everybody(nameslist=""):
    # if all_names is default you get an error
    if nameslist == "": nameslist = all_names

    for name in nameslist:
        introduce(name)

def discuss(message_a, message_b, person_a="Victoria", person_b="Alex"):

    sayit(message_a, person_a)
    sayit(message_b, person_b)

def random_name(nameslist=""):
    
    if nameslist == "": nameslist = all_names
    return random.choice(nameslist)

feminine_names = ["Agnes", "Kathy", "princess", "Vicki", "Victoria"]
masculine_names = ["Alex", "Bruce", "Fred", "Junior", "Ralph"]
novelty_voices = [ "Albert", "Bad News", "Bahh", "Boing", "Bubbles",
        "Cellos", "Deranged", "Good News", "Hysterical",
        "Pipe Organ", "Trinoids", "Whisper", "Zarvox" ]

all_names = feminine_names + masculine_names + novelty_voices

if __name__ == '__main__':

    # make input ok in python 2
    try:
        input = raw_input
    except NameError:
        pass
    
    #discuss("Hello, How are you?", "Me? I am fine.")
    user_message = input("What to say: ")
    
    user_who_says_it = input("Who to say it: ")
    
    # use a random voice
    if user_who_says_it.upper() == "RANDOM":
        user_who_says_it = random_name(all_names)

    if user_who_says_it in all_names:
        sayit(user_message, user_who_says_it)
    else:
        sayit(user_message)

