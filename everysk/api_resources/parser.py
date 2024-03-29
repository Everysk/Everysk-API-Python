###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
from everysk.api_resources.api_resource import (
    APIResource
)
from everysk import utils

class Parser(
    APIResource
):

    @classmethod
    def class_name(cls):
        return 'parser'

    @classmethod
    def __call_method(cls, method, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (cls.class_url(), method)
        response = api_req.post(url, kwargs)
        return response

    @classmethod
    def parse(cls, method, **kwargs):
        return cls.__call_method( '%s/parse' % method, **kwargs)