'''
    Return the secret integer in a range based on the response from the guess_bot.

You are given a low and high range (inclusive) and an instance of GuessBot (guess_bot).

You are only to interact with guess_bot by its method: guess_number(num) which returns a string.

guess_bot is a bit of an asshole and only returns the following strings when you call guess_number(number):

    'Smaller': Your guess is too big
    'Larger': Your guess is too small
    'Correct': Your guess is correct
    'You failed, you bring great shame to your family name': You ran out of tries
    'What are you, deaf?': Returned if you continously call guess_number after you already guessed the correct number

__You only have log2(N) calls to guess_number before the bot starts calling you a failure. N is the number of possible integers in the [low, high] range.__
'''


def find_secret_number(low, high, guess_bot):
    while low <= high:
        mid = (low + high) // 2
        guess_bot_answer = guess_bot.guess_number(mid)
        if guess_bot_answer == 'Correct':
            return mid
        if guess_bot_answer == 'Smaller':
            high = mid - 1
        elif guess_bot_answer == 'Larger':
            low = mid + 1
