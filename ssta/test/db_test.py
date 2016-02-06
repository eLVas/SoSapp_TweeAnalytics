
from ssta.collect.storage.neo.connector import Connector

from ssta.test.objects import user

connector = Connector()

user_entity = connector.get_dao('user')
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
