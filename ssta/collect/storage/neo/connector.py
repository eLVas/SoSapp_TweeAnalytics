from neo4jrestclient.client import GraphDatabase


class Neo4JConnector:

    def __init__(self, host, port, username, password):
        self._db = GraphDatabase('http://' + host + ':' + str(port), username=username, password=password)

    @property
    def db(self):
        return self._db
