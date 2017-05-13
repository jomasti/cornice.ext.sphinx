from cornice import Service
from cornice.validators import colander_validator

from .schemas import GetRequestSchema, PutRequestSchema


def validate(request):
    """Dummy validation."""
    return request


def view_get(request):
    """Provide shoe."""
    return request.validated


def view_put(request):
    """Update shoe"""
    return request.validated

def includeme(config):
    service = Service('Shoe', '/shoe/{colour}')
    service.add_view('GET', view_get, validators=(colander_validator), schema=GetRequestSchema())
    service.add_view('PUT', view_put, validators=(colander_validator, 'validate'),
                     schema=PutRequestSchema())
    config.add_cornice_service(service)
