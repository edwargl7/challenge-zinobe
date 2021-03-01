"""Main"""

from analytic.metrics.country_metrics import (get_country_dataframe,
                                              get_time_spent_metrics)

if __name__ == "__main__":
    df = get_country_dataframe()
    if not isinstance(df, dict):
        print(df)
        time_col = df['Time (ms)']
        time_metrics = get_time_spent_metrics(time_col)
        if not 'msg' in time_metrics:
            total_time = time_metrics['total_time']
            mean_time = time_metrics['mean_time']
            min_time = time_metrics['min_time']
            max_time = time_metrics['max_time']
            print('Tiempo que tardo en procesar todas las filas de la tabla')
            print(f'Tiempo total: {total_time}')
            print(f'Tiempo promedio: {mean_time}')
            print(f'Tiempo mínimo: {min_time}')
            print(f'Tiempo máximo: {max_time}')

