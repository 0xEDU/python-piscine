def all_thing_is_obj(object: any) -> int:
    if isinstance(object, int):
        print("Type not found")
        return 42

    objType = object.__class__
    typeName = objType.__name__.capitalize() if not isinstance(object, str) else object
    funnyStr = " is in the kitchen" if isinstance(object, str) else ""
    print(f'{typeName}{funnyStr} : {objType}')
    return 42
