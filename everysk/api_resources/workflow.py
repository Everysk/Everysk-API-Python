###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
import time
from everysk.api_resources.api_resource import (
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource
)
from everysk.api_resources.execution import Execution
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
    def run(cls, id, debug_callback=None, loop_sleep=1, loop_max=700, **kwargs):
        debug_callback = (lambda x, y: None) if (debug_callback is None) else debug_callback
        api_req = utils.create_api_requestor()
        url = '%s/%s/run' % (cls.class_url(), id)
        response = api_req.post(url, kwargs)
        kwargs = {}
        exe = utils.to_object(Execution, kwargs, response)
        debug_callback(0, exe)

        # loop_sleep = 1
        # loop_max = 700
        loop_count = 0
        done = ('COMPLETED', 'FAILED', 'TIMEOUT')
        while exe.status not in done:
            time.sleep(loop_sleep)
            exe.refresh()
            loop_count += 1
            debug_callback(loop_count, exe)
            if loop_count > loop_max:
                raise Exception('max run loop achieved')
        time.sleep(loop_sleep)
        result = None
        if exe.status in done:
            result = exe.result
        return result
