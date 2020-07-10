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
from everysk.api_resources.api_resource import APIResource
from everysk import utils

class Calculation(APIResource):

    def refresh(self):
        return self

    @classmethod
    def class_name(cls):
        return 'calculations'    
    
    @classmethod
    def class_url(cls):
        return '/%s' % cls.class_name()

    @classmethod
    def __call_method(cls, method, **kwargs):
        api_req = utils.create_api_requestor()
        url = '%s/%s' % (cls.class_url(), method)
        response = api_req.post(url, kwargs)
        return response

    @classmethod
    def riskAttribution(cls, **kwargs):
    	return cls.__call_method('risk_attribution', **kwargs)

    @classmethod
    def stressTest(cls, **kwargs):
    	return cls.__call_method('stress_test', **kwargs)

    @classmethod
    def exposure(cls, **kwargs):
    	return cls.__call_method('exposure', **kwargs)

    @classmethod
    def properties(cls, **kwargs):
    	return cls.__call_method('properties', **kwargs)

    @classmethod
    def backtest(cls, **kwargs):
        return cls.__call_method('backtest', **kwargs)

    @classmethod
    def backtestStatistics(cls, **kwargs):
        return cls.__call_method('backtest_statistics', **kwargs)

    @classmethod
    def aggregations(cls, **kwargs):
        return cls.__call_method('aggregations', **kwargs)

    @classmethod
    def fundamentals(cls, **kwargs):
        return cls.__call_method('fundamentals', **kwargs)

    @classmethod
    def daysToUnwind(cls, **kwargs):
        return cls.__call_method('days_to_unwind', **kwargs)

    @classmethod
    def sensitivity(cls, **kwargs):
        return cls.__call_method('sensitivity', **kwargs)

    @classmethod
    def optimize(cls, **kwargs):
        return cls.__call_method('optimize', **kwargs)