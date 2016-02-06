from neo4jrestclient.client import GraphDatabase

from ssta.collect.storage.neo.dao.user import UserDAO
from ssta.collect.storage.neo.dao.tweet import TweetDAO


class Neo4JConnector:
    def __init__(self, username, password, host='localhost', port=7474):
        self._db = GraphDatabase('http://' + host + ':' + str(port), username=username, password=password)

        self.entities = {
                            'user': UserDAO(self),
                            'tweet': TweetDAO(self)
                        }

    def get_dao(self, name):
        # TODO: load module from dao package or create new
        if name in self.entities:
            return self.entities[name]
        else:
            return None
            # return Entity(self, model[name])

    @property
    def db(self):
        return self._db
