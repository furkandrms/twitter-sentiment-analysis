#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sentiment_analysis import * 
import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "2ZiR2rHtY93OHPyZKNIeWiV6c"
consumer_secret = "HeEyXCh0e8LYTnRvvf9apNwBdBMvIzwGLn947czv8nWbudC4yU"
access_key = "1270725984673689600-sx15Jx8h111NjoX4rq1tXixtU3COsC"
access_secret = "PQWhAIpUzo4cJFZwbHL2PuXOHz9DI1hEXQGOyJ7e3impi"

#method to get a user's last tweets
def get_tweets(username, asData = True):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	number_of_tweets = 10

	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        #create array of tweet information: username, tweet id, date/time, text
		# username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")
		tweets_for_csv.append(tweet.text)

	if asData:

		print(type(tweets_for_csv))
		return ""


	#write to a new csv file from the array of tweets
	outfile = username + "_tweets.csv"

	with open(outfile, 'w+', encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow(["Tweet","Score","Status"])
		
		for tweet in tweets_for_csv: 
			a = get_sentiment(tweet)
			b = (a.split(" ")[1])
			c = (a.split(" ")[2])
			writer.writerow([tweet, c, b])
   


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print("Error: enter one username")

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
