'''
Created on 6 juil. 2015

@author: Raphael
'''

import enum


class user_type(enum.IntEnum):
    empty = 0
    mod = 1
    global_mod = 2
    admin = 3
    staff = 4


def user_type__new__(cls, value):
    if not isinstance(value, str):
        # forward call to user_type' superclass
        return super(user_type, cls).__new__(cls, value)
    else:
        return getattr(user_type, value.lower().strip(), user_type.empty)

setattr(user_type, "__new__", user_type__new__)


def get_tags(string):
    tags = dict({(x.split("=")[0], x.split("=")[1])
                 for x in string.split(";")})

    tags['subscriber'] = bool(int(tags['subscriber']))
    tags['turbo'] = bool(int(tags['turbo']))
    tags['user-type'] = user_type(tags['user-type'])

    return tags
