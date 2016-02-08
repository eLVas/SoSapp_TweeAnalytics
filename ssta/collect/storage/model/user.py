from ssta.collect.storage.model import props

LABEL = 'User'
ID = ['id']
PROPS = [
    # identification
    'id',
    'screen_name',
    'name',
    'description',
    'created_at',
    #location
    'geo_enabled',
    'location',
    'time_zone',
    'utc_offset',
    'lang',
    #social
    'statuses_count',
    'followers_count',
    'friends_count',
    'listed_count'
]


def build_props(user):
    return props.build_props(PROPS, user)


