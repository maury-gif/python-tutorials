#NESTING
#AN IF STATEMENT IN AN IF STATEMENT
Favmusic = input("What is your fav song? ")
if Favmusic == "Fast":
    print("Wow!, me too")
    Favmusician = input("Who is your fav musician? ")
    if Favmusician == "Juice wrld":
        print("You're such a vibeeee..")
    else:
        print("Ahwell")
elif Favmusic == "Dandelions":
    print("Ugh, why?")
else:
    print("Well, whatever.")


#DAY7 CHALLENGE
print("FAKE FAN FINDER")
Musician = input("Who is your fav Musician? ")
if Musician == "Juice wrld":
    m =input("Oh really?! Name any of his songs? ")
    print("You got that by pure chance. okay then... ")
    Pop = input("What is his most popular song? ")
    if Pop == "Lucid dreams":
        print("I see ")
    else:
        print("yo yo")
elif Musician == "Bob Marley":
    print("okay, that's nice")
else:
    print("\033[31mSee! Fake JW fan!\033[0m")
    