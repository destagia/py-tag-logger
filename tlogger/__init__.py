import datetime as dt

__format = "[{}] #{} - {}"

class TagsContainer(object):
    __instance = None

    def __new__(cls, *args, **keys):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.is_verbose = False
            cls.__instance.tags = None
            cls.__instance.tag_max_length = len("default")
        return cls.__instance

def log(*args):
    if len(args) == 1:
        tag = 'default'
        body = args[0]
    elif len(args) == 2:
        tag = args[0]
        body = args[1]
    if TagsContainer().is_verbose or (TagsContainer().tags != None and tag in TagsContainer().tags):
        message = __format.format(dt.datetime.now(), tag.ljust(TagsContainer().tag_max_length), body)
        print(message)
        return message

def set_tags(*tags):
    TagsContainer().tags = list(tags)
    TagsContainer().tag_max_length = reduce(lambda max, t: len(t) if max < len(t) else max, TagsContainer().tags, len("default"))

def set_verbose(verbose):
    TagsContainer().is_verbose = verbose
