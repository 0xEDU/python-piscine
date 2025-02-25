import math


def NULL_not_found(object: any) -> int:
    objType = object.__class__
    funnyName = ''

    if isinstance(object, None.__class__):
        funnyName = "Nothing"
    elif isinstance(object, bool) and not object:
        funnyName = "Fake"
    elif isinstance(object, float) and math.isnan(object):
        funnyName = "Cheese"
    elif isinstance(object, int) and object == 0:
        funnyName = "Zero"
    elif isinstance(object, str) and object == '':
        funnyName = "Empty"
    else:
        print("Type not found")
        return 1

    print(f'{funnyName}: {object} {objType}')
    return 0
