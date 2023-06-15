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

api_sid = None
api_token = None
api_entry = 'https://api.everysk.com'
api_version = 'v2'
verify_ssl_certs = True

def get_api_config(params):
    
    api_entry_ = params.get('api_entry', None)
    if api_entry_ is None:
      global api_entry
      api_entry_ = api_entry
      api_entry_ = os.getenv('EVERYSK_API_ENTRY', api_entry_)

    api_version_ = params.get('api_version', None)
    if api_version_ is None:
      global api_version
      api_version_ = api_version

    api_sid_ = params.get('api_sid', None)
    if api_sid_ is None:
      global api_sid
      api_sid_ = api_sid
      api_sid_ = os.getenv('EVERYSK_API_SID', api_sid_)

    api_token_ = params.get('api_token', None)
    if api_token_ is None:
      global api_token
      api_token_ = api_token
      api_token_ = os.getenv('EVERYSK_API_TOKEN', api_token_)

    verify_ssl_certs_ = params.get('verify_ssl_certs', None)
    if verify_ssl_certs_ is None:
      global verify_ssl_certs
      verify_ssl_certs_ = verify_ssl_certs

    return (api_entry_, api_version_, api_sid_, api_token_, verify_ssl_certs_)

from everysk.utils import *
from everysk.api_resources import *
