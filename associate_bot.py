# -*- coding: utf-8 -*-

import random
import json
import oauth2 as oauth
import a_key
import twitter

def authorize(num):
    CK = a_key.KEYS[num]['consumerKey']
    CS = a_key.KEYS[num]['consumerSecret']
    AK = a_key.KEYS[num]['accessKey']
    AS = a_key.KEYS[num]['accessSecret']

    print '  consumerKEY    : ' , CK
    print '  consumerSECRET : ' , CS
    print '  accessKEY      : ' , AK
    print '  accessSECRET   : ' , AS

    api = twitter.Api(CK, CS, AK, AS)
    print 'get API[', num ,']succeed...'

    return api

def tweet():
    api = authorize(0)
    nouns = []

    for noun in open("Noun.csv"):
        noun = noun.split(",")[0]
        nouns.append(noun)
#        print noun

    rand1 = random.randint(0, len(noun))
    rand2 = random.randint(0, len(noun))
    rand3 = random.randint(0, len(noun))

    tweet = "『" + nouns[rand1]  + "』『" + nouns[rand2] + "』『" + nouns[rand3] + "』\n" \
          + "#ランダムな3つの名詞から新製品をひねり出そう"
    print tweet
    api.PostUpdates(tweet)

if __name__ == '__main__':
    tweet()



