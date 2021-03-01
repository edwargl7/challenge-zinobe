"""Country Metrics"""
import time

import pandas as pd

from analytic.utils.region_utils import get_regions, get_country_by_region
from analytic.utils.country_utils import (get_country_language_name,
                                          get_country_name)
from analytic.utils.encryption_utils import encrypt_with_sha1


def get_country_dataframe():
    """Get country dataframe"""
    try:
        regions, error = get_regions()
        df = pd.DataFrame(columns=['Region', 'City Name', 'Language', 'Time (ms)'])
        if not error:
            for region in regions['regions']:
                start_time = time.time()
                country, error = get_country_by_region(region)
                if not error:
                    country = country['country']
                    language, error_cl = get_country_language_name(country)
                    if error_cl:
                        language = f'it was not possible to get the language. {language}'
                    else:
                        language = language['language_name']
                        language = encrypt_with_sha1(language)
                    country_name, error_cn = get_country_name(country)
                    if error_cn:
                        country_name = f'the country name could not be obtained. {country_name}'
                    else:
                        country_name = country_name['country_name']
                else:
                    country_name = 'the country name could not be obtained'
                    language = 'it was not possible to get the language'
                time_per_country = time.time() - start_time
                row = {'Region': region,
                       'City Name': country_name,
                       'Language': language,
                       'Time (ms)': time_per_country * 1000
                       }
                df = df.append(row, ignore_index=True)
            return df
        else:
            return df
    except Exception as ex:
        return {'msg': 'General Error in get_country_dataframe',
                'error': ex}


def get_time_spent_metrics(time_col):
    """Get time spent metrics (total, mean, minimum and maximum time
    spent processing each row)

    :param time_col: time column
    :type time_col: pandas.core.series.Series
    """
    try:
        total_time = time_col.sum()
        mean_time = time_col.mean()
        min_time = time_col.min()
        max_time = time_col.max()
        return {
            'total_time': total_time,
            'mean_time': mean_time,
            'min_time': min_time,
            'max_time': max_time
        }
    except Exception as ex:
        return {'msg': 'General error in get_time_spent_metrics',
                'error': ex
                }
