from get_tweets import *

text_input = input('Enter the username:')

tweets = get_tweets(text_input, False)

print(tweets)