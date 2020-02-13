# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie =input("Enter:")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("Not watched yet!")

number = 7
user_input = input("Enter 'y' if you want to play: ").lower()

if user_input == "y": 
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) in (1, -1):
        print("You were off by one.")
    else:
        print("Sorry!") 