from ssta.collect.twitter.api import API
from ssta.collect.storage.neo.connector import Connector


class Tweet:

    TwitterAPI = API()
    DAO = Connector().get_dao('tweet')

    def __init__(self, tid=None, raw=None, node=None, sync=True):
        if raw:
            self._raw = raw
            self.tid = raw.id
        elif node:
            self._node = node
            self.tid = node['id']
        elif tid:
            self.tid = tid
            self._raw = None
            self._node = None
        else:
            raise ValueError('For tweet id should be specified')

        if sync:
            self.sync()

    def load(self):
        self._raw = Tweet.TwitterAPI.get_status(id=self.tid)

    def sync(self):
        if not self._raw:
            self.load()

        self._node = Tweet.DAO.upsert(self._raw)

    def relate_to(self, rel_type, node, direction='to'):
        # TODO: check if already exists
        if direction == 'to':
            return self._node.relationships.create(rel_type, node)
        elif direction == 'from':
            return node.relationships.create(rel_type, self._node)
        elif direction == 'both':
            return [self.relate_to(rel_type, node, direction='to'), self.relate_to(rel_type, node, direction='from')]
