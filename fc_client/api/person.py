from .base.enrich_base import EnrichBase
from ..response.person import PersonEnrichResponse
from ..schema.person import PersonSchema


class Person(EnrichBase):
    r"""
    Class that provides methods to perform
    Person Enrich operations, with MultiField Capabilities.
    """
    enrich_endpoint = "person.enrich/"
    _enrich_request_handler = PersonSchema()
    _enrich_response_handler = PersonEnrichResponse
