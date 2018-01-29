# Assigning variables, atom autocompletes
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# Calculating information of interest
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Print out variables of interest for this car
# organization program
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avaialable.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# Error is study drill
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
#
# added a _ to a variable name, that calls a new variable, on which is
# undefined in the code.
# python returns an error.
#
# ctrl + / comments out a selection
