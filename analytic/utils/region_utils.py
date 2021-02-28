"""Region utilities"""
import pandas as pd
from random import randint
from analytic.utils.requests_utils import request_get
from settings.settings import (HOST_REGION_API, TOKEN_REGION_API,
                               URL_COUNTRY_API, URL_REGION_API)


def get_regions() -> tuple:
    """Get all regions"""
    try:
        url = URL_REGION_API + '/all'
        headers = {
            'x-rapidapi-key': TOKEN_REGION_API,
            'x-rapidapi-host': HOST_REGION_API
        }
        response, error = request_get(url, headers)
        if not error:
            df = pd.DataFrame(response)
            region = df.region.unique()
            region = list(filter(None, region))
            return {'regions': region}, False
        else:
            return response, error
    except AttributeError as aerr:
        return {'msg': 'AttributeError - region',
                'error': f'{aerr}'}, True
    except Exception as ex:
        return {'msg': 'General Error in get_regions',
                'error': f'{ex}'}, True


def get_country_by_region(region) -> tuple:
    """Get Country by Region"""
    try:
        url = URL_COUNTRY_API + f'/{region}'
        response, error = request_get(url)
        if not error:
            if (total := len(response)) > 0:
                # Random country
                country = response[randint(0, total - 1)]
                return {'country': country}, False
            else:
                return {'msg': 'Region without countries',
                        'error': 'Region without countries'}, True
        else:
            return response, error
        pass
    except Exception as ex:
        return {'msg': 'General Error in get_country_by_region',
                'error': f'{ex}'}, True
