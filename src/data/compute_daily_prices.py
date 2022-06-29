import pandas as pd
def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    df_completed = pd.read_csv("./data_lake/cleansed/precios-horarios.csv")
    df_completed = df_completed.groupby('fecha', as_index=False).mean()
    df_completed = df_completed[['fecha','precio']]
    df_completed.to_csv("./data_lake/business/precios-diarios.csv", index=False)

if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
