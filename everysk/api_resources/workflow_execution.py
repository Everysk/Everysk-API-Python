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

class WorkflowExecution(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource
):
    @classmethod
    def class_name(cls):
        return 'workflow_execution'

    @classmethod
    def retrieve(cls, workflow_id, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '/workflows/%s%s' % (workflow_id, cls.class_url())
        response = api_req.get(url, kwargs)
        return utils.to_object(WorkflowExecution, kwargs, response)