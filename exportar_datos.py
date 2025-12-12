import geopandas as gpd

def exportar_datos(gdf, barrio=None):

    columna_loc = "NOMBRE"   # ← Adaptado a tu JSON
    if barrio is None or barrio.strip() == "":
        salida = "general.csv"
        gdf.drop(columns="geometry").to_csv(salida, index=False)
        print(f"✔️ Archivo general creado: {salida}")
        return

    barrio = barrio.strip().upper()

    filtrado = gdf[gdf[columna_loc].str.upper() == barrio]

    if filtrado.empty:
        print(f"EL BARRIO'{barrio}' NO EXISTE EN EL ARCHIVO.")
        return

    salida = f"{barrio.replace(' ', '_')}.csv"
    filtrado.drop(columns="geometry").to_csv(salida, index=False)

    print(f"✔️ Archivo generado de la localidad '{barrio}': {salida}")
