import tweepy
from ssta.collect.twitter import config


class API:

    instance = None

    def __init__(self, auth=None):

        if not API.instance:
            if not auth:
                auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
                auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

            API.instance = tweepy.API(auth, **config.options)

    def __getattr__(self, name):
        return getattr(self.instance, name)
