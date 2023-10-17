#!/usr/bin/python3
def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False

    if isinstance(obj.__class__, a_class.__class__.__bases__):
        return True

    return False
