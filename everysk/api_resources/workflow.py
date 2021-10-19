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
    CreateableAPIResource,
    UpdateableAPIResource
)
from everysk.api_resources.workflow_execution import WorkflowExecution
from everysk import utils

class Workflow(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource
):

    @classmethod
    def class_name(cls):
        return 'workflow'

    @classmethod
    def run(cls, id, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s/run' % (cls.class_url(), id)
        response = api_req.post(url, kwargs)
        return utils.to_object(WorkflowExecution, kwargs, response)
