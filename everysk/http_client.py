###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
import os
import sys
from everysk import six
import json
import os.path

try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except ImportError:
    requests = None

if not requests:
    NO_REQUEST_MSG = '''
    Warning: the Everysk library is falling back to
    "urllib2/urllib" because "requests" is not installed.
    urllib2's SSL implementation doesn't verify server
    certificates. For improved security, we suggest installing requests.
    If you have any questions, please contact support@everysk.com.
    (HINT: running "pip install -U requests" should upgrade your
    requests library to the latest version.)\n\n'''
    sys.stderr.write(NO_REQUEST_MSG)
    
    from everysk.six.moves import urllib
    from everysk.six.moves.urllib.parse import urlparse    


class HTTPClient(object):
    def __init__(self, timeout=60, verify_ssl_certs=True, allow_redirects=False):
        self.timeout = timeout
        self.allow_redirects = allow_redirects
        self.verify_ssl_certs = verify_ssl_certs
        return

    def request(self, method, url, headers, params=None, payload=None):
        raise NotImplementedError(
            'HTTPClient subclasses must implement `request`'
        )


class RequestsClient(HTTPClient):
    def __init__(self, timeout=60, verify_ssl_certs=True, allow_redirects=False):
        super(RequestsClient, self).__init__(timeout=timeout, verify_ssl_certs=verify_ssl_certs, allow_redirects=allow_redirects)
        if self.verify_ssl_certs:
            #https://curl.haxx.se/docs/caextract.html
            certs_file_name = 'ca-certificates.crt'
            certs_path = os.path.join(os.path.dirname(__file__), certs_file_name)
            if os.path.exists(certs_path):
                self.verify_ssl_certs = certs_path
            else:
                raise Exception('Error loading %s' % certs_file_name)
        return

    def request(self, method, url, headers, params=None, payload=None):
        
        response = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            json=payload,
            timeout=self.timeout,
            verify=self.verify_ssl_certs,
            allow_redirects=self.allow_redirects
        )
        return (response.status_code, response.content)        


class Urllib2Client(HTTPClient):
    def __init__(self, timeout=60, verify_ssl_certs=True, allow_redirects=False):
        super(Urllib2Client, self).__init__(timeout=timeout, verify_ssl_certs=verify_ssl_certs, allow_redirects=allow_redirects)
        return

    def request(self, method, url, headers, params=None, payload=None):
        url_ = '%s?%s' % (url, urllib.parse.urlencode(params)) if params else url
        payload_ = json.dumps(payload) if payload else None

        req = urllib.request.Request(url_, payload_, headers)
        if method not in ('get', 'post'):
            req.get_method = lambda: method.upper()

        try:
            response = urllib.request.urlopen(req)
            rbody = response.read()
            rcode = response.code
            #headers = dict(response.info())
        except urllib.error.HTTPError as e:
            rcode = e.code
            rbody = e.read()
            #headers = dict(e.info())
        except (urllib.error.URLError, ValueError) as e:
            self.__handle_request_error(e)

        #lh = dict((k.lower(), v) for k, v in dict(headers).items())
        #return rbody, rcode, lh
        return (rcode, rbody)

    def __handle_request_error(self, e):
        msg = (
            'Unexpected error communicating with Everysk. '
            'If this problem persists, let us know at support@everysk.com.'
        )
        msg = msg + "\n\n(Network error: " + str(e) + ")"
        raise Exception(msg)


def new_default_http_client(*args, **kwargs):
    if requests:
        impl = RequestsClient
    else:
        impl = Urllib2Client
    return impl(*args, **kwargs)