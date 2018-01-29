
# four format slots within a string variable
formatter = "{} {} {} {}"

#Populates variables with integers
print(formatter.format(1,2,3,4))
# '' with stings
print(formatter.format("one", "two", "three", "four"))
# '' with variables
print(formatter.format(True, False, False, True))
# populates with the formatter string
print(formatter.format(formatter, formatter, formatter, formatter))
# My own text
print(formatter.format(
"Over the wintry forest,",
"winds howl",
"in rage",
"with no leaves to blow."
))
