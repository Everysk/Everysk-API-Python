###############################################################################
#
# (C) Copyright 2018 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
from everysk.api_resources.api_resource import (
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource,
    FilterableAPIResource
)

class Datastore(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource,
    FilterableAPIResource
):
    @classmethod
    def class_name(cls):
        return 'datastore'

    @classmethod
    def explore(cls, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '/%s/explore' % cls.class_name_list()
        response = api_req.post(url, kwargs)
        return response