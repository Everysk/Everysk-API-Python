###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
from everysk.api_resources.api_resource import APIResource
from everysk import utils

class MarketData(APIResource):

    def refresh(self):
        return selfs

    @classmethod
    def class_name(cls):
        return 'market_data'
    
    @classmethod
    def class_url(cls):
        return '/%s' % cls.class_name()

    @classmethod
    def __call_method(cls, method, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (cls.class_url(), method)
        response = api_req.post(url, kwargs)
        return response

    @classmethod
    def symbolsSearch(cls, **kwargs):
        return cls.__call_method('symbols_search', **kwargs)

    @classmethod
    def symbolsCheck(cls, **kwargs):
    	return cls.__call_method('symbols_check', **kwargs)

    @classmethod
    def symbolsPrice(cls, **kwargs):
    	return cls.__call_method('symbols_price', **kwargs)
    
    @classmethod
    def symbolsRealtimePrice(cls, **kwargs):
    	return cls.__call_method('symbols_real_time_prices', **kwargs)

    @classmethod
    def symbolsHistorical(cls, **kwargs):
    	return cls.__call_method('symbols_historical', **kwargs)