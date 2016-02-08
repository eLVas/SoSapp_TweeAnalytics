from ssta.collect.storage.model import props

LABEL = 'Tweet'
ID = ['id']
PROPS = ['id', 'text']


def build_props(tweet):
    return props.build_props(PROPS, tweet)
