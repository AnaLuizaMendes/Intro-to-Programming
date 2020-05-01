# List Comprehensions

# Get the names and inputs, and check who passed or not
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

# Create a for loop in one line
# The loop will interact for each name and
# check if value (get function) is >= 65 (min to pass)
passed = [name for name in scores if scores.get(name) >= 65]
print(passed)
print('\n')

# A function to split the names in the blank space character (to get the first name)
# Then lower the name, to return the first name in lower caps
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)
print('\n')

