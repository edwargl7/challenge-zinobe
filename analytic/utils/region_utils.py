"""Region utilities"""
import pandas as pd

from analytic.utils.requests_utils import request_get
from settings.settings import (HOST_REGION_API, TOKEN_REGION_API,
                               URL_REGION_API)


def get_regions():
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
        return {'msg': 'General Error',
                'error': f'{ex}'}, True
