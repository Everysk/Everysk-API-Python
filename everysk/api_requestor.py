###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
import json
from everysk import http_client
from everysk.six import python_2_unicode_compatible

OK_STATUS_CODE = (200, 202, 303)


@python_2_unicode_compatible
class APIError(Exception):
    def __init__(self, code, message):
        super(APIError, self).__init__(message)
        self.__code = code
        self.__message = json.loads(message) if message else message
        return

    def __str__(self):
        if self.__code and self.__message:
            return json.dumps(self.__message, sort_keys=True, indent=2)
            # return '%s -> %s' % (self.__code, self.__message)
        return 'API ERROR'


class APIRequestor(object):
    def __init__(self, api_entry, api_version, api_sid, api_token, verify_ssl_certs):
        if not api_entry:
            raise Exception('Empty api_entry')
        if api_version != 'v2':
            raise Exception('Invalid api_version (supported version: "v2")')
        if not api_sid:
            raise Exception('Invalid api_sid')
        if not api_token:
            raise Exception('Invalid api_token')

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s:%s' % (api_sid, api_token),
            'User-Agent': 'Everysk PythonBindings/%s' % (api_version)
        }
        self.base_url = '%s/%s' % (api_entry, api_version)
        self.client = http_client.new_default_http_client(
            timeout=60,
            verify_ssl_certs=verify_ssl_certs,
            allow_redirects=False
        )
        return

    def get(self, path, params):
        url = '%s%s' % (self.base_url, path)
        code, response = self.client.request(
            'GET',
            url,
            headers=self.headers,
            params=params
        )
        if code not in OK_STATUS_CODE:
            raise APIError(code, response)
        return json.loads(response)

    def post(self, path, payload):
        url = '%s%s' % (self.base_url, path)
        code, response = self.client.request(
            'POST',
            url,
            headers=self.headers,
            payload=payload
        )
        if code not in OK_STATUS_CODE:
            raise APIError(code, response)
        return json.loads(response)

    def delete(self, path):
        url = '%s%s' % (self.base_url, path)
        code, response = self.client.request(
            'DELETE',
            url,
            headers=self.headers
        )
        if code not in OK_STATUS_CODE:
            raise APIError(code, response)
        return json.loads(response)

    def put(self, path, payload):
        url = '%s%s' % (self.base_url, path)
        code, response = self.client.request(
            'PUT',
            url,
            headers=self.headers,
            payload=payload
        )
        if code not in OK_STATUS_CODE:
            raise APIError(code, response)
        return json.loads(response)
