LABEL = 'User'
ID = ['id']


def build_props(user):
    props = {}
    props['id'] = user.id
    props['screen_name'] = user.screen_name
    props['name'] = user.name

    return props


