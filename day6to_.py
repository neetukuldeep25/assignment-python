# Practice: Check whether a number is even or odd

# number = int(input("enter a number:"))

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")



# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))

# for i in range(rows):
#     for j in range(columns):
#         print("*", end=" ")
#     print()

# book_type = input("Enter book type (standard/reference): ").lower()
# days = int(input("Enter overdue days: "))
# premium = input("Are you a premium member? (yes/no): ").lower()

# # Calculate fine
# if book_type == "standard":
#     if days <= 5:
#         fine = days * 5
#     else:
#         fine = (5 * 5) + ((days - 5) * 10)

# elif book_type == "reference":
#     fine = days * 20

# else:
#     fine = 0
#     print("Invalid book type!")

# # Apply premium discount
# if book_type == "standard" or book_type == "reference":
#     if premium == "yes":
#         fine = fine - (fine * 20 / 100)

#     print("Total library fine: Rs", fine)



# import json
# import os

# FILE_NAME = "tasks.json"

# # Load saved tasks
# if os.path.exists(FILE_NAME):
#     with open(FILE_NAME, "r") as file:
#         tasks = json.load(file)
# else:
#     tasks = []


# def save_tasks():
#     with open(FILE_NAME, "w") as file:
#         json.dump(tasks, file, indent=4)


# def show_tasks():
#     if len(tasks) == 0:
#         print("No tasks found!")
#     else:
#         for i, task in enumerate(tasks, start=1):
#             status = "Done" if task["completed"] else "Pending"
#             print(i, task["name"], "-", status)


# while True:
#     print("\n--- MY TODO APP ---")
#     print("1. Add task")
#     print("2. View tasks")
#     print("3. Complete task")
#     print("4. Delete task")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter task name: ").strip()

#         if name:
#             tasks.append({"name": name, "completed": False})
#             save_tasks()
#             print("Task added successfully!")

#     elif choice == "2":
#         show_tasks()

#     elif choice == "3":
#         show_tasks()

#         try:
#             number = int(input("Enter task number to complete: "))

#             if 1 <= number <= len(tasks):
#                 tasks[number - 1]["completed"] = True
#                 save_tasks()
#                 print("Task completed!")
#             else:
#                 print("Invalid task number!")

#         except ValueError:
#             print("Please enter a valid number!")

#     elif choice == "4":
#         show_tasks()

#         try:
#             number = int(input("Enter task number to delete: "))

#             if 1 <= number <= len(tasks):
#                 deleted_task = tasks.pop(number - 1)
#                 save_tasks()
#                 print("Deleted:", deleted_task["name"])
#             else:
#                 print("Invalid task number!")

#         except ValueError:
#             print("Please enter a valid number!")

#     elif choice == "5":
#         print("Goodbye! Your tasks are saved.")
#         break

#     else:
#         print("Invalid choice! Please try again.")


# words = input("Enter words separated by spaces: ").split()

# if words:
#     longest_word = max(words, key=lambda word: len(word))
#     print("Longest word:", longest_word)
# else:
#     print("Please enter at least one word.")


# Prices = {
#     "apple": 20,
#     "banana": 10,
#     "milk": 30,
#     "bread": 25,
#     "eggs": 50
# }

# out_of_stock = {"milk", "eggs"}

# Order = [
#     ["apple", "banana"],
#     ["milk", "bread"],
#     ["apple", "eggs"],
#     ["banana", "bread"]
# ]

# total = 0

# for order in Order:
#     for item in order:
#         if item in out_of_stock:
#             print(item, "is unavailable")
#         else:
#             total = total + Prices[item]

# print("Final order value: Rs", total)

# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     result = num1 / num2
#     print("Result:", result)

# except ValueError:
#     print("Invalid input! Please enter numbers only.")

# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# finally:
#     print("Calculator program finished.")
