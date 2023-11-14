from enum import Enum


class ProductsContentTypes(Enum):
    '''ID of ContetType instances for actors models.'''
    GOOD = 13
    SERVICE = 14
    PARKING = 15


products_ids = [member.value for member in ProductsContentTypes]
