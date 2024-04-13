# Peter Madin
# Section 03
# 04/27/20
# Assignment 2

# Bricks & Mortar

# Calculates the supplies and information of Brick & Mortar laying

# CONSTANTS == fixed numebers
BRICK_VOLUME = 0.00120705 # brick volume, includes mortar volume
BRICK_MASS = 2.3 # in kilograms
BRICK_COST = 0.65 # n dollars per brick
MORTAR_VOLUME = 0.025 # in m^3, mortar makes 15% of the volume in foundation
MORTAR_MASS = 43 # in kilograms
MORTAR_COST = 7.25 # in dollars per bag
MORTAR_PERCENT = 0.15 # percent of mortar in decimal form

# INPUTS == information the user put in
text = '\nEnter the "length" of your brick foundation in meters: '
length = float(input(text))

text = '\nEnter the "width" of your brick foundation in meters: '
width = float(input(text))

text = '\nEnter the "height" of your brick foundation in meters: '
height = float(input(text))
    
text = '\nEnter the "thickness" of your brick foundation in meters: '
thicc = float(input(text))

# PROCESSING == calculations preformed
overall_area = length * width # in meters cube

enclosed_length = length - thicc * 2 # two sides of the length thickness

enclosed_width = width - thicc * 2 # two sides of the width thickness

enclosed_area = enclosed_length * enclosed_width # simplifies enclosed area

total_volume = (overall_area - enclosed_area) * height # total area in meters cube

wall_volume = length * height * thicc # the volume of the foundation/wall

number_of_bricks = total_volume / BRICK_VOLUME # calculates the amount of bricks
 
bags_of_mortar = (MORTAR_PERCENT * total_volume) / MORTAR_VOLUME # amount of mortar need

total_mass = (number_of_bricks * BRICK_MASS) + (bags_of_mortar * MORTAR_MASS) # whole mass of everything

materials_cost = (number_of_bricks * BRICK_COST) + (bags_of_mortar * MORTAR_COST) # The cost of all items

# OUTPUTS == shown outcomes
print('+-----------------------------------------------------------------------'\
      + '-------+')

print('\n Here are your results:')
print('\n Overall Area: (Square Meters): ' + format(overall_area, '.2f'))
print('\n Enclosed Area: (Square Meters): ' + format(enclosed_area, '.2f'))
print('\n Total Volume: (Cubic Meters): ' + format(total_volume, '.2f'))
print('\n Number of Bricks: ' + format(number_of_bricks, '.0f'))
print('\n Bags of Mortar: ' + format(bags_of_mortar, '.0f'))
print('\n Total Mass: (Kilograms): ' + format(total_mass, '.2f'))
print('\n Total Materials Cost: $' + format(materials_cost, '.2f'))

# DOCUMENTATION

# Program was tesd with two following inputs

# input one

# length = 12
# width = 9
# height = 2
# thickness = 1

# produced results

# Overall Area: 108.00  
# Enclosed Area: 70.00
# Total Volume: 76.00
# Number of Bricks: 62963
# Bags of Mortar: 456
# Total Mass: 164423.87
# Materials Cost: 44232.23

# input two

# length = 24
# width = 7
# height = 3
# thickness = 1.5

# produced results

# Overall Area: 168.00  
# Enclosed Area: 84.00
# Total Volume: 252.00
# Number of Bricks: 208773
# Bags of Mortar: 1512
# Total Mass: 545194.95
# Materials Cost: 146664.75

# These results were verified by hand, which produced successful calculations
# Additionally the results match to example instructions results
