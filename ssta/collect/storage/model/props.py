def build_props(props_list, obj):
    props = {}

    for prop_name in props_list:
        if type(prop_name) is list:
            props[prop_name[1]] = getattr(obj, prop_name[0])
        else:
            props[prop_name] = getattr(obj, prop_name)

    return props
