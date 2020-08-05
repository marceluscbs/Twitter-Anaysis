#!/usr/bin/env python
# coding: utf-8

# # ICA-1: Creating Twitter developer account and collecting data from Twitter using Twitter API

# In[1]:


ACCESS_TOKEN = "INSERT YOUR INFO"
ACCESS_TOKEN_SECRET = "INSERT YOUR INFO" 
CONSUMER_KEY = "INSERT YOUR INFO"
CONSUMER_SECRET = "INSERT YOUR INFO"


# In[2]:


import tweepy as tw


# In[3]:


# Creating the authentication object
auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# Setting your access token and secret
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Creating the API object while passing in auth information
api = tw.API(auth, wait_on_rate_limit=True)

# Testing the Connectivity
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# In[4]:


# Collect the latest 10 Tweets from your Twitter account. You can also use filters if you wish (optional)
collect_tweets = api.home_timeline(count=10, tweet_mode="extended")

#Print the full text for these tweets
tweets = [[tweet.full_text] for tweet in collect_tweets]

tweets

