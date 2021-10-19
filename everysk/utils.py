###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
import json
from everysk import api_requestor, get_api_config
from everysk import six

def dumps_json(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

class EveryskObject(dict):
    def __init__(self, retrieve_params, params):
        super(EveryskObject, self).__init__()
        self.__unsaved_values = set()
        self.update(params)
        self.clear_unsaved_values()
        return

    def get_unsaved_values(self):
        return {k:self[k] for k in self.__unsaved_values}
    
    def clear_unsaved_values(self):
        self.__unsaved_values = set()

    def __str__(self):
        return dumps_json(self)

    def __repr__(self):
        ident_parts = [type(self).__name__]
        ident_parts.append('id=%s' % (self.get('id'),))
        unicode_repr = '<%s at %s> JSON: %s' % (
            ' '.join(ident_parts),
            hex(id(self)),
            str(self)
        )
        return unicode_repr

    def update(self, dict_):
        #super(EveryskObject, self).update(dict_)
        for k, v in six.iteritems(dict_):
            self.__setattr__(k, v)
        #    super(EveryskObject, self).__setattr__(k, v)
        return

    def __setattr__(self, k, v):
        if k.startswith('_') or k in self.__dict__:
            return super(EveryskObject, self).__setattr__(k, v)

        self[k] = v
        return None

    def __getattr__(self, k):
        if k.startswith('_'):
            raise AttributeError(k)

        try:
            return self[k]
        except KeyError as err:
            raise AttributeError(*err.args)

    def __delattr__(self, k):
        if k.startswith('_') or k in self.__dict__:
            return super(EveryskObject, self).__delattr__(k)
        else:
            del self[k]

    def __setitem__(self, k, v):
        # if v == "":
        #     raise ValueError(
        #         "You cannot set %s to an empty string. "
        #         "We interpret empty strings as None in requests."
        #         "You may set %s.%s = None to delete the property" % (
        #             k, str(self), k))

        # # Allows for unpickling in Python 3.x
        # if not hasattr(self, '_unsaved_values'):
        #     self._unsaved_values = set()

        self.__unsaved_values.add(k)
        super(EveryskObject, self).__setitem__(k, v)
        return

    def __getitem__(self, k):
        return super(EveryskObject, self).__getitem__(k)
        # try:
        #     return super(EveryskObject, self).__getitem__(k)
        # except KeyError as err:
        #     if k in self._transient_values:
        #         raise KeyError(
        #             "%r.  HINT: The %r attribute was set in the past."
        #             "It was then wiped when refreshing the object with "
        #             "the result returned by Everysk's API, probably as a "
        #             "result of a save().  The attributes currently "
        #             "available on this object are: %s" %
        #             (k, k, ', '.join(list(self.keys()))))
        #     else:
        #         raise err

    def __delitem__(self, k):
        super(EveryskObject, self).__delitem__(k)

        self.__unsaved_values.remove(k)
        return

        # # Allows for unpickling in Python 3.x
        # if hasattr(self, '_unsaved_values'):
        #     self._unsaved_values.remove(k)


class EveryskList(list):
    def __init__(self, retrieve_params, response, key, cls):
        super(EveryskList, self).__init__()
        self.__page_size = retrieve_params.get('page_size', 10)
        self.__next_page_token = response.get('next_page_token', None)
        self.extend([cls({}, params) for params in response[key]])
        return

    def page_size(self):
        return self.__page_size

    def next_page_token(self):
        return self.__next_page_token

def create_api_requestor(params={}):
    return api_requestor.APIRequestor(
        *get_api_config(params)
    )

def to_object(cls, retrieve_params, response):
    key = cls.class_name()
    if (
        (not response) or
        (not key in response) or
        (type(response[key]) is not dict)
    ):
        return None
    return cls(retrieve_params, response[key])

def to_list(cls, retrieve_params, response):
    key = cls.class_name_list()
    if (
        (not response) or
        (not key in response) or
        (type(response[key]) is not list)
    ):
        return None
    #return [cls({}, params) for params in response[key]]
    return EveryskList(retrieve_params, response, key, cls)

