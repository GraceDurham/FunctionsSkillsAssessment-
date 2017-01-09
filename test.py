# def hello_world():
#     """function does not take any arguments and
#     prints "Hello World".

#     For example::

#         >>> hello_world()
#         Hello World

#     """

#     print "Hello World"

# hello_world()


#Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


# >>> say_hi("Balloonicorn")
#     Hi Balloonicorn

# def say_hi(name):
#     print "Hi", name 




# say_hi("Balloonicorn")

#Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.

# >>> print_product(3, 5)
#     15

# 


# 





#write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".



# def print_sign(num):
#     if num > 0:
#         print "Higher than 0"
#     elif num < 0:
#         print "Lower than 0"
#     else:
#         print "Zero"



# print_sign(5)
# #    Higher than 0


#Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.



# >>> print_sign(0)


#     Zero




# Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


# def is_divisible_by_three(num):

#     if (num % 3) == 0:
#         return True
#     else:
#         return False 




# print is_divisible_by_three(11)
    # True



#Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.

# def num_spaces(sentence):
#     count = 0
#     for space in sentence:
#         if space == " ":
#             count = count + 1

#     print count 



# num_spaces("Balloonicorn is awesome!")
#  #   2
# num_spaces("Balloonicorn is       awesome!")
# #   8


# Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


# def total_meal_price(price, tip = .15):


#     total_amount_paid = (price + price * tip)
#     return total_amount_paid




# print total_meal_price(30)
#  #   34.5

# print total_meal_price(30, .3)
#    # 39.0


#9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.



# def sign_and_parity(num):

#     signs_and_parity = []

#     if (num % 2 == 0):
#         signs_and_parity.append("Even")

#     else:
#         signs_and_parity.append("Odd")

#     if num >= 0:
#         signs_and_parity.append("positive")
#     else: 
#         signs_and_parity.append("Negative")



#     return signs_and_parity

#     sign,parity = signs_and_parity


# print sign_and_parity(3)





#sign_and_parity(-2)
    #['Even', 'Negative']

# def full_title(name,job_title = "Engineer"):
#     print job_title, name
#     return 

# full_title("Balloonicorn")





#1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.


# def full_title(name, job_title ="Engineer"):
#     # print name, job_title


#     combine_job_name = job_title + name 

#     return combine_job_name 

#     split_letters=combine_job_name.split(",") 

#     split_letters = split_letters + " " + " "
#     return split_letters

#     # for letter in split_letters:
#     #     return letter + " "
    

# print full_title("Balloonicorn")   


# def full_title(name,job_title = "Engineer"):
#     return job_title, name


#2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.



# def write_letter(recipient_name, job_title, sender_name):
#     print "Dear %s %s, I think you are amazing! Sincerely, %s" % (job_title,recipient_name,sender_name)










# write_letter("Jane Hacks", "Hacker", "Balloonicorn")
#   Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn



# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

# """

# PART ONE:

#     >>> town_name("sweet_springs")
#     True 


#     >>> town_name("chilicothe")
#     False 


# """

# def first_last(first,last):
#     first_last_name = first + last 
#     return first_last_name 


# print first_last("Grace", "Durham")    
# def town_name(home_town):

#     
# if home_town == "sweet_springs":
#         print True 
#     else:
#         print False 




# town_name("mexico")

# def first_last_home_town(hometown, first_last):


#     town_name = town_name("sweet_springs")
#     first_last = first_last("grace", "durham")


# first_last_home_town(town_name, first_last)



#PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


# def is_berry(fruit):
#     """Determines if fruit is a berry"""

#     # for letter in fruit:
#     #     if not letter.contain("berry"):
#     #         print True 
#     #     else:
#     #         print False 
#     if "berry" in fruit:
#         return True
#     else: 
#         return False 


# # is_berry("blackberry")
# #  #   True
# # is_berry("durian")
# #   False


# #b) Write another function, shipping_cost(), which calculates shipping cost
# #     by taking a fruit name as a string and calling the is_berry() function
# #     within the shipping_cost() function. Your function should return 0 if
# #     is_berry() == True, and 5 if is_berry() == False.

# def shipping_cost(fruit):
#     """Calculates shipping cost of fruit"""

#     if is_berry(fruit) == True:
#         return "0"
#     elif is_berry(fruit) == False:
#         return 5




# print shipping_cost("black")
#     #0
#shipping_cost("durian")
   # 5


#2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

# def append_to_list(lst, num):
#     """Creates a new list consisting of the old list with the given number
#        added to the end."""

#     appends_to_list = []

#     for item in lst:
#         appends_to_list.append(item)
#     appends_to_list.append(num)



#     return appends_to_list



# print append_to_list([3, 5, 7], 2)
#    [3, 5, 7, 2]


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.



# def calculate_price(base_price,two_letter_state, tax = .05):

#     total_price_with_tax = base_price + base_price * tax
#     # print total_price_with_tax
#     if two_letter_state == "CA":
#         ca_total_with_fee = total_price_with_tax * .03
#         total_cost_item = ca_total_with_fee + total_price_with_tax
#         return round(total_cost_item)
#     elif two_letter_state == "NM" or "OR":
#         return total_price_with_tax
#     elif two_letter_state == "PA":
#         pa_total_with_fee = total_price_with_tax + pa_fee
#         return pa_total_with_fee




# # print calculate_price(25, "CA")
# #   #  27.0

# # print calculate_price(400, "NM")
# # #    # 420.0

# # print calculate_price(150, "OR", 0)
# #    # 150

# print calculate_price(60, "PA")
# #    # 65.0

# print calculate_price(38, "MA")
# #  #   40.9

# calculate_price(126, "MA")


  #  135.3

#PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def multi(**args):

    multis = []

    #This function takes in multiple arguments
    # I got to create an empty list and I know I have to append to the list 
    #I got stuck how to call the other functions and then append to the list 
    #I got a refence before assignment error 


    return multis

print multi() 


def outer(word):
    def inner(num):

        #multiplys the word in outer by 3
        return (word * num)


    return inner(3)

outer = outer("Balloonicorn")
print outer 































































































































































































































































