import pandas as pd
import matplotlib.pyplot as plt
def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    df_daily_prices = pd.read_csv("./data_lake/business/precios-diarios.csv")
    plot(df_daily_prices["fecha"], df_daily_prices["precio"])
    print(df_daily_prices.head())


if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()
