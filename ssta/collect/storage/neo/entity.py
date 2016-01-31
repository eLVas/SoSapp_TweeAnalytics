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

        labels = [].extend(self.labels)
        if custom_labels: labels.extend(custom_labels)

        node.labels.add(labels)

        return node


    def update(self, obj, add_labels):


        if not node:
            return self.create(obj, custom_labels=add_labels)
        else:


    def delete(self):


    def exists(self, obj):
        props = self._model.build_props(obj)

        obj_id = {}
        for key in self._model.ID:
            obj_id[key] = props[key]

        return  self.main_label.get(**obj_id)