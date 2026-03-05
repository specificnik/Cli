import random

bars = ["McSorley's Old Ale House",
        "Death & Company",
        "The Back Room",
        "Dominik",
        "PDT"]

people = ["Mattan",
          "Sarah",
          "that person you forgot to text back",
          "Samuel L. Jackson"]

random_bar = random.choice(bars)
random_person_1 = random.choice(people)
random_person_2 = random.choice(people)

print(f"How about you go to {random_bar} with {random_person_1} and {random_person_2}?")
