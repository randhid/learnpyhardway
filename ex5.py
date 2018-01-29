#

name = 'Rand Hidayah'
age = 27 # not a lie
height = 159 # centimeters
weight = 68 # kg
eyes = 'Brown'
teeth = 'white'
hair = 'Brown'

kg2lb = 2.2
cm2in = 2.54

heightin = round(height/cm2in)
weightlb = round(weight*kg2lb)


print(f"Let's talk about {name}")
print(f"She's {height} cm tall")
print(f"She's {heightin} in tall")
print(f"She's {weightlb} lb heavy")
print(f"She's {weight} kg heavy.")
print(f"Actually that's not too heavy.")
print(f"She's got {eyes} and {hair} hair")
print(f"Her teeth are usually {teeth} depending on coffee.")


# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")
