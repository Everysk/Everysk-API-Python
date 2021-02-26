###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
from everysk import utils

class APIResource(utils.EveryskObject):
    def __init__(self, retrieve_params, params):
        super(APIResource, self).__init__(retrieve_params, params)
        self.__retrieve_params = retrieve_params    
        return

    def refresh(self, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (self.class_url(), self.get('id'))
        kwargs = self.__retrieve_params
        response = api_req.get(url, kwargs)
        data = response[self.class_name()]
        self.update(data)
        self.clear_unsaved_values()
        return self
 
    @classmethod
    def class_name(cls):
        raise NotImplementedError('APIResource is an abstract class.')

    @classmethod
    def class_name_list(cls):
        cn = cls.class_name()
        if cn[-1] in ('s', 'x'):
            cn += 'es'
        else:
            cn += 's'
        return cn

    @classmethod
    def class_url(cls):
        return '/%s' % cls.class_name_list()

class RetrievableAPIResource(APIResource):

    @classmethod
    def retrieve(cls, id, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (cls.class_url(), id)
        response = api_req.get(url, kwargs)
        return utils.to_object(cls, kwargs, response)

class ListableAPIResource(APIResource):

    @classmethod
    def list(cls, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = cls.class_url()
        response = api_req.get(url, kwargs)
        return utils.to_list(cls, kwargs, response)

    @classmethod
    def auto_paging_iter(cls, **kwargs):
        params = dict(kwargs)
        page = cls.list(**params)
        while True:
            for item in page:
                yield item
            if page.next_page_token() is None:
                return
            params['page_token'] = page.next_page_token()
            page = cls.list(**params)

class DeletableAPIResource(APIResource):

    def delete(self, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (self.class_url(), self.get('id'))
        response = api_req.delete(url)
        data = response[self.class_name()]
        self.clear()
        self.update(data)
        self.clear_unsaved_values()
        return self

    @classmethod
    def remove(cls, id, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (cls.class_url(), id)
        response = api_req.delete(url)
        data = response[cls.class_name()]
        return utils.to_object(cls, {}, response)

class CreateableAPIResource(APIResource):

    @classmethod
    def create(cls, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = cls.class_url()
        response = api_req.post(url, kwargs)
        return utils.to_object(cls, kwargs, response)

class UpdateableAPIResource(APIResource):

    @classmethod
    def modify(cls, id, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (cls.class_url(), id)
        response = api_req.put(url, kwargs)
        data = response[cls.class_name()]
        return utils.to_object(cls, kwargs, response)

    def save(self, **kwargs):
        api_req = utils.create_api_requestor(kwargs)
        url = '%s/%s' % (self.class_url(), self.get('id'))
        #response = api_req.put(url, self)
        unsaved_values = self.get_unsaved_values()
        response = api_req.put(url, unsaved_values)
        data = response[self.class_name()]
        self.update(data)
        self.clear_unsaved_values()
        return self
