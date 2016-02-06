from ssta.collect.twitter.api import API
from ssta.collect.storage.neo.connector import Connector


class User:

    TwitterAPI = API()
    DAO = Connector().get_dao('user')

    def __init__(self, screen_name=None, uid=None, sync=False):
        if uid or screen_name:
            self.uid = uid
            self.screen_name = screen_name
            self._raw = None
            self._node = None
            if sync:
                self.load()
        else:
            raise ValueError('For user screen_name or id should be specified')

    def load(self):
        self._raw = User.TwitterAPI.get_user(id=self.uid, screen_name=self.screen_name)
        self.uid = self._raw.id
        self.screen_name = self._raw.screen_name
        self._node = User.DAO.upsert(self._raw)

    def retrieve_tweets(self):
        # TODO: retrieve
        raise NotImplementedError


