"""
Settings for analytic project.
"""
from pathlib import Path

from decouple import config
from database.databases.database_factory import DatabaseFactory

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

FILE_ROOT = BASE_DIR.joinpath('files/')

DATABASE_NAME = config('DATABASE_NAME',
                       default='analytic_database.db')
manage_database = DatabaseFactory.get_manage_database(
    'sqlite',
    {'database_name': DATABASE_NAME}
)

# Region Variables
HOST_REGION_API = config('HOST_REGION_API',
                         default='restcountries-v1.p.rapidapi.com')
TOKEN_REGION_API = config(
    'REGION_TOKEN_API',
    default='08bec50fe0msh830a41291d14550p1a64ccjsnb3578c261142')
URL_REGION_API = config('URL_REGION_API',
                        default='https://restcountries-v1.p.rapidapi.com')

# Country Variables
URL_COUNTRY_API = config('URL_COUNTRY_API',
                         default='https://restcountries.eu/rest/v2/region')
