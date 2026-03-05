answer = input("Do you want to hear a joke? ").lower().strip()

if answer in ["yes", "y"]:
    print("What's loud and sounds like an apple?")
    print("AN APPLE")
elif answer in ["no", "n"]:
    print("Fine.")
else:
    print("I don't understand.")