# Create a string and break it in exactly 140 characters
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    # Check if the len of your new string + the value of the next string would be <= 140
    if len(news_ticker) + len(headline) <= 140:
        news_ticker += headline + " "

    else:
        # If we can't add the entire string otherwise will pass the value of 140, then we go by character
        for character in headline:
            if len(news_ticker) + len(character) <= 140:
                news_ticker += character
            else:
                break

print(news_ticker)
print(len(news_ticker))
print('\n')

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

for number in check_prime:
    i = 2
    while i < number:
        if number % i == 0:
            print("{} is not a prime number, because {} is a factor of {}".format(number, i, number))
            break
        if i == (number - 1):
            print('{} is not prime'.format(number))
        i += 1
print('\n')


