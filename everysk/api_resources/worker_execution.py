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
    DeletableAPIResource
)
from everysk import utils

class WorkerExecution(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource
):
    @classmethod
    def class_name(cls):
        return 'worker_execution'

    @classmethod
    def retrieve(cls, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '/workflows%s' % (cls.class_url())
        response = api_req.get(url, kwargs)
        return utils.to_object(WorkerExecution, kwargs, response)

