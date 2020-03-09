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
from everysk.api_resources.process import Process

from everysk import utils

class Report(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource
):
    @classmethod
    def class_name(cls):
        return 'report'

    @classmethod
    def create(cls, debug_callback=None, **kwargs):
        debug_callback = (lambda x, y: None) if (debug_callback is None) else debug_callback
        api_req = utils.create_api_requestor()
        url = cls.class_url()
        response = api_req.post(url, kwargs)
        kwargs = {}
        proc = utils.to_object(Process, kwargs, response)
        debug_callback(0, proc)

        loop_sleep = 1
        loop_max = 700
        loop_count = 0
        done = ('completed', 'failed', 'timeout')
        while proc.status not in done:
            time.sleep(loop_sleep)
            proc.refresh()
            loop_count += 1
            debug_callback(loop_count, proc)
            if loop_count > loop_max:
                raise Exception('max run loop achieved')
        time.sleep(loop_sleep)
        result = None
        if proc.status in done:
            result_ = proc.result
            if result_['status'] == 'ok':
                result = utils.to_object(Report, kwargs, {'report': result_['data']})
        return result        

    def share(self, **kwargs):
        api_req = utils.create_api_requestor()
        url = '%s/%s/share' % (self.class_url(), self.get('id'))
        response = api_req.post(url, kwargs)
        data = response[self.class_name()]
        self.update(data)
        self.clear_unsaved_values()
        return self
