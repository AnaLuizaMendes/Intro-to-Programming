# Learning how to make a def function

# def + name of function (something that makes sense) + attributes you want to pass
def readable_time(days):
    # getting the integer that represents the number of weeks
    weeks = days // 7
    # getting the integer that represents the number of remaining days
    rem_days = days % 7
    string = '{} week(s) and {} day(s).'.format(weeks, rem_days)
    return string


print(readable_time(40))


# Another example to create a function to calculate the population density
# Input: Population and area
def population_density(population, land_area):
    pop_density = population / land_area
    return pop_density


test1 = population_density(20, 4)
print(f"Result: {test1}")
