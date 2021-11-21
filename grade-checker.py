# Grade Checker

name = input("Enter your name: ")
score = int(input("Enter your score here: "))

# A, B, C, D, E, F

if score >= 79:
    print(f"Hello {name}, You have an A! Congratulations")

elif score in range(65, 79):
    print(f"Hello {name}, You have a B! Very Good")

elif score >= 60 and score <= 64:
    print(f"Hello {name}, You have a C! Good")

elif score >= 55 and score <= 59:
    print(f"Hello {name}, You have a D! Fair")

elif score >= 49 and score <= 54:
    print(f"Hello {name}, You have an E! Poor")

elif score <= 48:
    print(f"Hello {name}, You have an F! Failed")

else:
    print(f"Hello {name}, You have a missing result")