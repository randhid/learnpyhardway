# printing stuff
print("Mary had a little lamb.")
# another way to print. format whatever is in the {}
# is what is being formatted
print("It's fleece was white as {}.".format('snow'))
print("ANd everywhere that Mary went.")
print("." * 10) # what'd that do?
# ooooh, it printed ten dots!

#Assigns single letter string variables to each endX
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10= "g"
end11= "e"
end12= "r"

# watch end = '' at the end. try removing
# it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
#If I remove the end = ' ' at the end, the print returns
# Burger on a separate line.
print(end7 + end8 + end9 + end10 +end11 + end12)
