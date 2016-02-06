import ssta.collect.storage.model.user as model
from ssta.collect.storage.neo.entity import Entity


class UserDAO(Entity):

    def __init__(self, connector, custom_labels=None):
        super().__init__(connector, model, custom_labels)