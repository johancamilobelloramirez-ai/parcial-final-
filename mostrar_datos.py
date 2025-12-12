def mostrar_datos(gdf):
    columnas=["NOMBRE","CODIGO_LOCALIDAD"]

    filtrado= gdf[columnas]

    print(filtrado.head())