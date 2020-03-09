###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
api_sid = None
api_token = None
api_entry = 'https://api.everysk.com'
api_version = 'v2'
verify_ssl_certs = True

def get_api_config():
    global api_entry, api_version, api_sid, api_token, verify_ssl_certs
    return (api_entry, api_version, api_sid, api_token, verify_ssl_certs)

from everysk.utils import *
from everysk.api_resources import *
