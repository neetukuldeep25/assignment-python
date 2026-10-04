age = int(input("Enter age: "))
female = input("Are you female? (yes/no): ")
alone = input("Are you traveling alone? (yes/no): ")
tatkal = input("Is it a Tatkal ticket? (yes/no): ")
blackout = input("Is it a blackout day? (yes/no): ")

if (age >= 60 or (female == "yes" and alone == "yes")) and tatkal == "no" and blackout == "no":
    print("Condition is true")
else:
    print("Condition is not true")