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
    def parse(cls, id, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s/parse' % (cls.class_url(), id)
        response = api_req.post(url, kwargs)
        return utils.to_object(cls, kwargs, response)
