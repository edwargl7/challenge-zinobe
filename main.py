"""Main"""
from pandas import DataFrame

from settings.settings import manage_database
from settings.settings import FILE_ROOT
from analytic.metrics.country_metrics import (get_country_dataframe,
                                              get_time_spent_metrics)
from database.base_schema import create_tables

if __name__ == "__main__":
    create_tables()
    df = get_country_dataframe()
    if isinstance(df, DataFrame):
        print(df)
        time_col = df['Time (ms)']
        time_metrics = get_time_spent_metrics(time_col)
        if 'msg' not in time_metrics:
            total_time = time_metrics['total_time']
            mean_time = time_metrics['mean_time']
            min_time = time_metrics['min_time']
            max_time = time_metrics['max_time']
            print('Tiempo que tardo en procesar todas las filas de la tabla')
            print(f'Tiempo total: {total_time}')
            print(f'Tiempo promedio: {mean_time}')
            print(f'Tiempo mínimo: {min_time}')
            print(f'Tiempo máximo: {max_time}')

        # Save in database
        for index, row in df.iterrows():
            # 'Region', 'City Name', 'Language', 'Time (ms)'
            query = "INSERT INTO regions(name) VALUES(?)"
            region_id = manage_database.query_one(query,
                                                  args=(row['Region'],),
                                                  commit=True)
            query = "INSERT INTO countries(name, language, region_id) VALUES(?, ?, ?)"
            country_id = manage_database.query_one(
                query,
                args=(row['City Name'], row['Language'], region_id,),
                commit=True)
            query = "INSERT INTO metrics(time, country_id) VALUES(?, ?)"
            manage_database.query_one(query,
                                      args=(row['Time (ms)'], country_id),
                                      commit=True)

        # Export DataFrame to JSON file
        df.to_json(FILE_ROOT.joinpath('data.json'))
