
# my_list = ['item']
# my_list *= 10
# var= 5
# my_list[0] = var
# print(my_list, var)

# phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
# for word in phrase:
#     print(word, end='-')
# print(phrase, end='-')


# print ("what's your name ")
# my_name = input("Enter your name: ")
# print("hi,{}".format(my_name))
# response_code=200
# match response_code:
#   case 200:
#     print("OK")     
#   case 404:
#     print("Not Found")
#   case 500:
#     print("Server Error")
#   case _:
#     print("Unknown Error")
# # print("hi,{}".format(my_name))

# import sys
# while True:
#   feedback = input("Type exit to quit: ")
#   if feedback =='exit':
#     print("Exiting...")
#     sys.exit()
#   else:
#     print("You entered: ", feedback)


# response_code = 800
# match response_code:
#         case 200 | 201:
#             print("OK")
#         case 300 | 3007:
#             print("Redirect")
#         case 400 | 401:
#           print("bad Request")
#         case 500 | 502:
#           print("Internal Server Error")
#         case _ :
#             print("Unknown Error")


# name = input("Enter your name: ")
# print("hi,{} ".format(name))
# color = input("Enter your favorite color: ")
# print((name)+ " you like " + (color))

# birth_year = int(input("Enter your birth year: "))
# age = 2025 - int (birth_year)
# print("You are {} years old.".format(age))


# name = input("Enter your name: ")
# # name = "jfj"
# if len(name) > 10:
#     print("Your name is too long.")
# elif len(name) < 3:
#     print("Your name is too short.")
# else:
#     print("Your name is just right.")


weight = input("Enter your weight in kg or (L)bs: ") 
unit = input("Enter the unit (kg or lbs): ")
if unit == "kg":
    weight = float(weight) * 2.20462
    print("Your weight in lbs is: {:.2f}".format(weight))
else:
    weight = float(weight) / 2.20462
    print("Your weight in kg is: {:.2f}".format(weight))


    secret_number = 7
    guess_count = 0
    max_guesses = 3
    while guess_count < max_guesses:
        guess = int(input("Guess the secret number (1-10): "))
        guess_count += 1
        if guess == secret_number:
            print("Congratulations! You guessed the secret number.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")