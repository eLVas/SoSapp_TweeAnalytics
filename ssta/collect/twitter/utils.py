import time
import tweepy

_interval = 15 * 60


def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError as re:
            print('rate')
            print(re)
            time.sleep(_interval)
        except IOError as ioe:
            print('IO')
            print(ioe)
            time.sleep(_interval)
