###############################################################################
#
# (C) Copyright 2018 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
from everysk.api_resources.api_resource import (
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource
)

class Process(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource
):
    @classmethod
    def class_name(cls):
        return 'process'

