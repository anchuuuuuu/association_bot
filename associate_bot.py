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

    for noun in open("/home/ec2-user/association_bot/association_bot/Noun.csv"):
        noun = noun.split(",")[0]
        nouns.append(noun)
#        print noun

    rand1 = random.randint(0, len(nouns))
    rand2 = random.randint(0, len(nouns))
    rand3 = random.randint(0, len(nouns))

    tweet = "『" + nouns[rand1]  + "』『" + nouns[rand2] + "』『" + nouns[rand3] + "』\n" \
          + "#ランダムな3つの名詞から新製品をひねり出そう"
    print tweet
    api.PostUpdates(tweet)
    api.PostUpdates("@anchuuuuuuuu " + tweet)

if __name__ == '__main__':
    tweet()



