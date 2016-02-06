LABEL = 'Tweet'
ID = ['id']


def build_props(tweet):
    props = {'id': tweet.id, 'text': tweet.text}

    return props
