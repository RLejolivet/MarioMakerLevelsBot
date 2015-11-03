import enum


class user_type(enum.IntEnum):
    empty = 0
    mod = 1
    broadcaster = 2
    global_mod = 3
    admin = 4
    staff = 5


def user_type__new__(cls, value):
    if not isinstance(value, str):
        # forward call to user_type' superclass
        return super(user_type, cls).__new__(cls, value)
    else:
        return getattr(user_type, value.lower().strip(), user_type.empty)

setattr(user_type, "__new__", user_type__new__)


def get_tags(string, channel=None):
    tags = dict({(x.split("=")[0], x.split("=")[1])
                 for x in string.split(";")})

    if(channel is not None and channel == tags['display-name'].lower()):
        tags['user-type'] = "broadcaster"

    tags['subscriber'] = bool(int(tags['subscriber']))
    tags['turbo'] = bool(int(tags['turbo']))
    tags['user-type'] = user_type(tags['user-type'])

    return tags
