#geraldworks

print("\nWelcome to the Love Calculator!\n")
print("T occurs 1 times || L occurs 1 times")
print("R occurs 0 times || O occurs 0 times")
print("U occurs 2 times || V occurs 0 times")
print("E occurs 2 times || E occurs 2 times")
print("Total is 5       || Total is 3")
print("Love score = 53\n")

name1 = input("What is your name? \n")
name2 = input("What is your crush name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()







if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")