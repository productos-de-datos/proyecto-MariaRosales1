"""
Módulo de ingestión de datos desde repositorio externo
Debe ser ejecutado ya sea desde el directorio actual o desde la raiz del proyecto
"""
import os
import urllib.request

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

    parent_dir = "data_lake"

    if os.path.isdir(parent_dir) and os.path.isdir(parent_dir+"/landing" ):
        os.chdir(parent_dir + "/landing")
        for year in range(1995,2022):
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'
            if year not in (2016, 2017):
                url = url + str(year)+'.xlsx?raw=true'
                urllib.request.urlretrieve(url, str(year) + ".xlsx")
            else :
                url = url + str(year)+'.xls?raw=true'
                urllib.request.urlretrieve(url, str(year) + ".xls")
    else:
        print("There is not landing directory!")


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
