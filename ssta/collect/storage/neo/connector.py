from ssta.collect.storage.neo.neo4j_connector import Neo4JConnector

from ssta.collect.storage.neo import config


class Connector:

    instance = None

    def __init__(self, **kwargs):

        if not Connector.instance:
            kwargs['username'] = config.USER_NAME if 'username' not in kwargs else None
            kwargs['password'] = config.PASSWORD if 'password' not in kwargs else None
            Connector.instance = Neo4JConnector(**kwargs)

    def __getattr__(self, name):
        return getattr(self.instance, name)
