###############################################################################
#
# (C) Copyright 2020 EVERYSK TECHNOLOGIES
#
# This is an unpublished work containing confidential and proprietary
# information of EVERYSK TECHNOLOGIES. Disclosure, use, or reproduction
# without authorization of EVERYSK TECHNOLOGIES is prohibited.
#
###############################################################################
from everysk.api_resources.api_resource import (
    DeletableAPIResource,
    RetrievableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource
)

class ReportTemplate(
    RetrievableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    UpdateableAPIResource
):
    @classmethod
    def class_name(cls):
        return 'report_template'

