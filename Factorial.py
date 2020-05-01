# Calculating Factorial in Python

# number to find the factorial of
number = 20
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1
# print the factorial of number
print(product)

# number to find the factorial of
number = 20
# start with our product equal to one
product = 1

# write your for loop here
for each in range(2, (number + 1)):
    product *= each
# print the factorial of number
print(product)

# How to count from a number to another number until a final number
start_num = 2  # provide some start number
end_num = 26  # provide some end number that you stop when you hit
count_by = 2  # provide some number to count by
break_num = 0

# write a condition to check that end_num is larger than start_num before looping
if end_num > start_num:
# write a while loop that uses break_num as the ongoing number to
    while break_num <= end_num:
        start_num += count_by
#   check against end_num
        break_num = start_num
        result = break_num
else:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

print(result)