import tweepy

from ssta.collect.twitter.api import API
from ssta.collect.storage.neo.connector import Connector
from ssta.collect.tweet import Tweet
from ssta.collect.twitter import utils


class User:

    TwitterAPI = API()
    DAO = Connector().get_dao('user')
    TweetDAO = Connector().get_dao('tweet')

    def __init__(self, raw=None, screen_name=None, uid=None, sync=True):
        if raw:
            self._raw = raw
            self.uid = raw.id
            self.screen_name = raw.screen_name
        elif uid or screen_name:
            self.uid = uid
            self.screen_name = screen_name
            self._raw = None
            self._node = None
        else:
            raise ValueError('For user screen_name or id should be specified')

        if sync:
            self.sync()

    def load(self):
        if self.uid:
            self._raw = User.TwitterAPI.get_user(id=self.uid)
            self.screen_name = self._raw.screen_name
        else:
            self._raw = User.TwitterAPI.get_user(screen_name=self.screen_name)

    def sync(self):
        if not self._raw:
            self.load()

        self.uid = self._raw.id
        self._node = User.DAO.upsert(self._raw)

    def load_tweets(self, save_func=None):
        save_func = save_func or self.wrote_tweet

        if not self._raw:
            self.load()

        cursor = tweepy.Cursor(User.TwitterAPI.user_timeline, id=self.uid, count=200).items()
        user_tweets_iterator = utils.limit_handler(cursor)
        count = 0

        for tweet in user_tweets_iterator:
            save_func(tweet)
            count += 1

        return count

    def get_tweets(self, only_text=False, sync=False):
        tweets = []

        rels = self._node.relationships.outgoing(types=['WROTE'])
        for relation in rels:
            tweet_node = relation.end
            if only_text:
                if sync:
                    Tweet(node=tweet_node, sync=True)

                tweets.append(tweet_node['text'])
            else:
                tweet = Tweet(node=tweet_node)
                tweets.append(tweet)

        return tweets

    def wrote_tweet(self, raw):
        return self.relate_to_tweet(rel_type='WROTE', raw=raw)

    def retweeted_tweet(self, raw):
        return self.relate_to_tweet(rel_type='RETWEET', raw=raw)

    def relate_to_tweet(self, rel_type='WROTE', tid=None, raw=None):
        tweet = Tweet(raw=raw, tid=tid, sync=True)
        return tweet.relate_to(rel_type, self._node, direction='from')
