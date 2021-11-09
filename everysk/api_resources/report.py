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
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    UpdateableAPIResource
)
from everysk import utils

class Report(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    UpdateableAPIResource
):
    @classmethod
    def class_name(cls):
        return 'report'  

    def share(self, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s/share' % (self.class_url(), self.get('id'))
        response = api_req.post(url, kwargs)
        data = response[self.class_name()]
        self.update(data)
        self.clear_unsaved_values()
        return self
