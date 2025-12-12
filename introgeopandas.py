import geopandas as gpd 
from cargar_archivo import cargar_archivo
from mostrar_info import mostrar_info
from mostrar_mapa import mostrar_mapa
from mostrar_datos import mostrar_datos
from exportar_datos import exportar_datos

my_gdf = cargar_archivo("barrio_legalizado.json")
mostrar_mapa(my_gdf)
exportar_datos(my_gdf,"maria cano")
