import unittest
import tweepy
import requests
import json

## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Jordan Kaplan 2
## Any names of people you worked with on this assignment:


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points
consumer_key = "0xuo6kBAJTkOwdvTZoLjHRPlp"
consumer_secret = "8LxLPabK9GMhFqPjbghJJvKImeCz9tkxh1zvfbrDOYxpoTaxf1"
access_token = "3084987586-0Md6REUNQDliZV6iJF8nP0QfpkcPJX93GAZ41Ly"
access_token_secret = "un4ggEFahiJRnYS95F2hvKcjbuEsn39esTygf1VOTD9ZS"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.

CACHE_FNAME='Kent_State.txt'
try:
	cache_file=open(CACHE_FNAME, "r")
	cache_contents= cache_file.read()
	CACHE_DICTION_text=json.loads(cache_contents)
	cache_file.close()
	print "done"
except:
	CACHE_DICTION_text={}


## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is. 
def getwithcaching(phrase):
	
	public_tweets = api.home_timeline() # One possible method! Check out: http://tweepy.readthedocs.io/en/v3.5.0/api.html#timeline-methods 
	print(type(public_tweets)," is the type of publictweets")

	for tweet in public_tweets:
    	print("\n*** type of the tweet object that is included ***\n")
    	print(type(tweet),"type of one tweet") 
    	print(tweet) ## Huh. That's not easy to read.
		print 'using cache'
		response_text=CACHE_DICTION_text[full_url]
	else:
		print 'fetching'
		response=requests.get(full_url)
		CACHE_DICTION_text[full_url]=response.text
		response_text=response.text

		cache_file=open(CACHE_FNAME, "w")
		cache_file.write(json.dumps(CACHE_DICTION_text))
		cache_file.close()
	return response_text


## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!


## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.








