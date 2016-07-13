from tlogger import config as conf
import datetime as dt

class TagsContainer(object):
    __instance = None

    def __new__(cls, *args, **keys):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

TagsContainer().tags = conf.get_tags() or []

__tag_max_length = reduce(lambda max, t: len(t) if max < len(t) else max, TagsContainer().tags, 0)
__format = "[{}] #{} - {}"

def log(tag, body):
    if TagsContainer().tags == None or tag in TagsContainer().tags:
        message = __format.format(dt.datetime.now(), tag.ljust(__tag_max_length), body)
        print(message)
        return message

def set_tags(*tags):
    TagsContainer().tags = list(tags)

