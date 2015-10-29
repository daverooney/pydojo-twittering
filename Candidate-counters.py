import tweepy, time
from tweepy import OAuthHandler
from TwitterKeys import *
from collections import Counter

auth = tweepy.OAuthHandler(APIKEY, APISECRET)
auth.set_access_token(ACCESSTOKEN, ACCESSSECRET)
api = tweepy.API(auth)

stopwords = ["a", "the", "is", "I", "to", "of", "that", "and", "RT", "rt", "in", "Mr.", "Ms.", "Mrs."]
CandidateList = ["Trump", "Carson", "Bush", "Rand Paul", "Kasich", "Fiorina", "Rubio", "Huckabee", "Cruz", "Christie"]
CandCounters = {}
for c in CandidateList:
  CandCounters[c] = Counter()

try:
  while 1:
    for cand in CandidateList:
      tweets = api.search(cand)
      for t in tweets:
        for word in t:
          if word not in stopwords:
            CandCounters[cand][word] += 1
      time.sleep(6)
      CandCounters[cand] = CandCounters[cand].most_common(5000)
      print cand, CandCounters[cand].most_common(10)
except:
  for cand in CandidateList:
    print cand, CandCounters[cand].most_common(10)
  

