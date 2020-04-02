from .base.enrich_base import EnrichBase
from .base.search_base import SearchBase
from ..response.company import CompanyEnrichResponse, CompanySearchResponse
from ..schema.company import CompanyEnrichSchema, CompanySearchSchema


class Company(EnrichBase, SearchBase):
    r"""
    Class that provides methods to perform
    Company Enrich and Search operations.
    """
    enrich_endpoint = "company.enrich/"
    _enrich_request_handler = CompanyEnrichSchema()
    _enrich_response_handler = CompanyEnrichResponse

    search_endpoint = "company.search/"
    _search_request_handler = CompanySearchSchema()
    _search_response_handler = CompanySearchResponse
