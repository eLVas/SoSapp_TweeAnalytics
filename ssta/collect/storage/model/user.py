LABEL = 'User'
ID = ['id']


def build_props(user):
    props = {'id': user.id, 'screen_name': user.screen_name, 'name': user.name}

    return props


