import tweepy
from tweepy import OAuthHandler
from TwitterKeys import *
from collections import Counter

auth.set_access_token(ACCESSTOKEN, ACCESSSECRET)
api = tweepy.API(auth)

stopwords = ["a", "the", "is", "I", "to", "of", "that", "and"
CandidateList = ["Trump", "Carson", "Bush", "Rand Paul", "Kasich", "Fiorina", "Rubio", "Huckabee", "Cruz", "Christie"]
CandCntrs = {}
for c in CandidateList:
  CandCntrs[c] = Counter()

try:
  while 1:
    for cand in CandidateList:
        tweets = api.search(cand)
          for t in tweets:
            for word in t:
              if 
api.search('Trump')
