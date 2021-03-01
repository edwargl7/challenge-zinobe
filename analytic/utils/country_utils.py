"""Country Utilities"""


def get_country_language_name(country) -> tuple:
    """Get country language name"""
    try:
        if len(country['languages']) > 0:
            language_name = country['languages'][0]['name']
            return {'language_name': language_name}, False
        else:
            return {'msg': f"The country hasn't languages. Country: {country}",
                    'error': 'The country has not languages.'}, True
    except KeyError as kerr:
        return {'msg': 'KeyError in get_country_language_name',
                'error': f'{kerr}'}, True
    except Exception as ex:
        return {'msg': 'General Error in get_country_language_name',
                'error': f'{ex}'}, True


def get_country_name(country) -> tuple:
    """Get country name"""
    try:
        country_name = country['name']
        return {'country_name': country_name}, False
    except KeyError as kerr:
        return {'msg': 'KeyError in get_country_name',
                'error': f'{kerr}'}, True
    except Exception as ex:
        return {'msg': 'General Error in get_country_name',
                'error': f'{ex}'}, True
