#ELIF STATEMENTS
#Elifs Come after the IF and before the last ELSE 
#ELIF works just like an IF statement 

#DAY 6 CHALLENGE
print("SECURE LOGIN")

User = input("Name please: ")
Password = input("Password please: ")
#we can join codes by adding boolean expressions like ("AND", "OR", "NOT")
if User == "Mau" and Password == "Donttryme!":
    print("Hey girlll! what's up. Such an aura you possess.")
    print("You're so amazing and your day is going to be wonderful as you are.")
    print("Have a great!")
    print("Don't forget you're the best! Muaahh Kisses")
elif User == "King" and Password == "mykingdomrules!":
    print("You are humbly welcome")
    print("I would love to have a trip to your palace.")
    print("Your authority is top notch")
elif User == "Belle" and Password == "beautyinallangles!":
    print("Hey beautiful")
    print("As beautiful and bright as the sun is, so are you.")
    print("You are such a beauty goddess!")
else:
    print("\033[31mGO AWAY!\033[0m")
