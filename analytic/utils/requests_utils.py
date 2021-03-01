"""Request utilities"""

import requests


def request_get(url, headers=None) -> tuple:
    """Get method requests"""
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
