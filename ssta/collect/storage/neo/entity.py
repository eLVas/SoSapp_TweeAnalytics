class Entity:

    def __init__(self, connector, model, custom_labels=None):
        self._connector = connector
        self._db = connector.db
        self._model = model

        self.main_label = self._db.labels.create(self._model.LABEL)
        self.labels = [self._model.LABEL]
        if custom_labels:
            self.labels.extend(custom_labels)

    def get(self, condition=None, **props):
        if condition:
            return self.main_label.filter(**condition)
        else:
            return self.main_label.get(**props)

    def create(self, obj, custom_labels=None):
        props = self._model.build_props(obj)
        node = self._db.nodes.create(**props)

        labels = []
        labels.extend(self.labels)
        if custom_labels:
            labels.extend(custom_labels)

        node.labels.add(labels)
        return node

    def upsert(self, obj, add_labels=None):
        node = self.get_one(obj)

        if not node:
            return self.create(obj, custom_labels=add_labels)
        else:
            node.properties = self._model.build_props(obj)
            return node

    def delete(self, condition=None, **props):
        nodes = self.get(condition=condition, **props)

        count = 0
        for node in nodes:
            node.delete()
            count += 1

        return count

    def get_one(self, obj):
        props = self._model.build_props(obj)

        obj_id = {}
        for key in self._model.ID:
            obj_id[key] = props[key]

        nodes = self.main_label.get(**obj_id)

        if nodes:
            return nodes.next()
        else:
            return None
