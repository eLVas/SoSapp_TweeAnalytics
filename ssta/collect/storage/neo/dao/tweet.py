import ssta.collect.storage.model.tweet as model
from ssta.collect.storage.neo.entity import Entity


class TweetDAO(Entity):

    def __init__(self, connector, custom_labels=None):
        super().__init__(connector, model, custom_labels)
