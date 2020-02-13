# def hello():
#     print("Hello!")

# hello()
##########################

# def user_age_in_sec():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}.")

# print("Welcome to this function!")
# user_age_in_sec()
# print("Thanks Bye!")

##########################

friends = ["Rolf", "Bob"]

def add_friends():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name]

    #Cant use friends variable name on place of f because you can't define the same variable name at a same place.
     

add_friends( )