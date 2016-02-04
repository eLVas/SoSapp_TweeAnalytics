
from ssta.collect.storage.neo import connector
from ssta.collect.storage.neo import entity
from ssta.collect.storage.model import user as user_model

from ssta.test.objects import user

connector = connector.Neo4JConnector('localhost', 7474, 'neo4j', 'electro')

user_entity = entity.Entity(connector, user_model)
user = user.User(900, 'eLVas', 'Ivan')
print('User: ', user)
print('creating user')
node = user_entity.create(user)
print('user created: ', node)

print('geting user')
nodes = user_entity.get(screen_name='eLVas')
print('got: ')
for node in nodes:
    print(node)

print('Changin username to Ban')
user.name = 'Ban'
print('User: ', user)
node = user_entity.upsert(user)
print('saved: ',node)

print('deleting')
n = user_entity.delete(id=900)
print(n, ' users deleted')
