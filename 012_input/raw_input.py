"""
Notes: =========================================================================
Notes: raw_input(prompt)
Notes:   Ex: raw_input("> "), raw_input("Enter (Y)es/(N)o")
Notes:
"""

highest = 10
answer = 3 

guess = raw_input("Guess a number between 0 to %d :" %highest)
while int(guess) != answer:
    if int(guess) < answer:
        print "Entered number is smaller than answer. Try again."
    else:
        print "Entered number is greater than answer. Try again."
    guess = raw_input("Guess a number between 0 to %d :" %highest)

print "You guessed the number correctly"
