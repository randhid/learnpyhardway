types_of_people = 10
x = f"There are {types_of_people} types of people."

# making string variables using the pre defined
# variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#printing statements
print(x)
print(y)

# using print statements with the strign variables
# three levels of embedded strings
print(f"I said: {x}")
print(f"I also said: {y}")

# Set a boolean, not the capital letter
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"


print(joke_evaluation.format(hilarious))

w = " This is the lef side of..."
e= "a string with a right side"

# this adds both strings together in the order from
# left to right
print(w + e)
