# # creating a chatbox basically
# Define the following variables
# name, last_name, species, eye_color, hair_color

name = 'Steph'
last_name = 'Robinson'
species = 'giraffe'
eye_colour = 'Green'
hair_colour = 'Blonde'
age = 23

# Prompt user for input and Re-assign these
#also capitising names and stripping any white space
name = input('What new name would you like to have?     :')
name = name.strip().lower().capitalize()

last_name = input('what new last name would you like to have?       :')
last_name = last_name.strip().lower().capitalize()

species = input('what new species would you like to be?     :')
species = species.strip().lower()

eye_colour = input('what new eye colour do you want?        :')
eye_colour = eye_colour.strip().lower()

hair_colour = input('what new hair colour would you like?       :')
hair_colour = hair_colour.strip().lower()

age = input('how old would you like to be?     :')
age = age.strip().lower()

# Print them back to the user as conversation
print(f'Hello {name} {last_name}, you are now a {species}, your age is {age}, \n your eyes are {eye_colour} and your hair colour is {hair_colour}!')

# Section 2 - Calculate in what year was the person born? and responde back.
new_age = input('\n how old are you again? (please use numerical values in years)      :')
new_age = new_age.strip()
birth_year = 2020 - int(new_age)

print(f'\n Since you said you was {new_age}, you was born in {birth_year}!')


