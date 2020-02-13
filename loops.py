# number = 7
# while True:

#     user_input = input("Woutd you like to play? (y/n) ").lower()

#     if user_input == "n":
#         break
    
#     user_number = int(input("Guess the number: "))
#     if user_number == number:
#         print("You guessed correctly")
#     elif abs(number - user_number) in (1, -1):
#         print("You were off by one.")
#     else:
#         print("Sorry!") 

friends =["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")  