# If name == "Mau" or "Mau"(this means is name is = Mau for the first Mau but the 2nd Mau means does the word Mau exist?)
#correct way: if name == "Mau" or name == "Mau"

# #PROJECT DAY
#For today's project, i'm going to build affirmation generator.

print("\033[33mCUSTOM AFFIRMATION GENERATOR\033[0m")
print()
name = input("Who are you? ")
print ("Hey beautiful/handsome.. ", name)
print (name, "You're becoming better and better everyday, you're confident, capable and in control of your life ")
happy = input("What makes you happy? ")
print("You are worthy of all the success and happiness in the world", name)
print()
Dream = input("What is stopping you from achieving your dream life?" )
if Dream == "nothing":
    print("\033[31mThen get up and show up for yourself!\033[0m")
    Day = input("What day is it today? ")
    if Day == "Wednesday" or Day == "Friday" or Day == "Saturday":
        print("Such a great day! init")
    elif Day == "Monday" or "Tuesday" or "Thursday" or "Sunday":
        print("Ugh...")
    else:
        print("Yeah right!")
        print()
        print("With 1=extremely sad and 10=extremely happy")
    scale = input("On a scale of 1-10, how do you feel today? ")
    if scale == "1" or "2" or "3" or "4"or "5":
        print("Don't worry. Life happens. You'll be fine and i know that you", name, "are becoming the best version of yourself. ")
    elif scale == "6" or "7" or "8" or "9" or "10":
        print("Ikrr..Life keeps on getting better everyday!")
    else:
        print("You'll do great!")
elif Dream == "I dont know":
    print("I understand how you feel but you wanna make it in life, your feelings should be off. And besides,", name, ",i believe in you and i know you have what it takes to make it.")
else:
    print("You better stop being sad about your life and get things going. No one is going to save you.")
