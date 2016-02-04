import ssta.collect.storage.model.user as model


class UserRecord:

    def __init__(self, connector, custom_labels=None):
        self._connector = connector
        self._db = connector.db()

        self.main_label = self._db.labels.create("User")
        self.labels = [self.main_label]
        if custom_labels:
            self.labels.extend(custom_labels)

    def get(self, condition=None, **props):
        if condition:
            return self.main_label.filter(**condition)
        else:
            return self.main_label.get(**props)

    def save(self, user):
        user_props = model.build_props(user)
        self._db.nodes.create(**user_props)