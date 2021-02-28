"""Region utilities"""

import requests


def get_regions(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json(), False
        else:
            return {'msg': response.json(),
                    'error': f'Status code {response.status_code}'
                    }, True
    except Exception as ex:
        return {'msg': f'Failed request to {url}',
                'error': ex}, True
