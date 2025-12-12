import geopandas as gpd 
from cargar_archivo import cargar_archivo
from mostrar_info import mostrar_info
from mostrar_mapa import mostrar_mapa
from mostrar_datos import mostrar_datos
from exportar_datos import exportar_datos

my_gdf = cargar_archivo("barrio_legalizado.json")
mostrar_info(my_gdf)
exportar_datos(my_gdf,"maria cano")



#valor localidad de inicio de valor 0
# si el usuario pone el nombre de la localidad cuando llama a la funcion se crea un archivo csv de la localidad llamada
#si el usuario no pone el nombre de la localidad la funcion hace un archivo csv general de todo 


#trabajar con datos del gdf
