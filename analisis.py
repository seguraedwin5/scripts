import pandas as pd
import matplotlib.pyplot as plt
from azure.storage.blob import BlobServiceClient, BlobClient, __version__, ContainerClient
import time,os
import shutil as sh

#connection string for Azure storage
connect_str = 'DefaultEndpointsProtocol=https;AccountName=egsfpython;AccountKey=66EOT1fYA2aAil49rDP1ojxDYY4oCbYXcQcmxolxTVwOb8NNa4qy4mDgeLEJlTJ44SqREfWnAqIc+ASt8obY0A==;EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
#crear nombre para el container donde se almacenará la información
container_name =  'csvfiles'
#crear el contenedor
try:
    if blob_service_client.get_container_client(container=container_name).exists():
        blob_service_client.delete_container(container=container_name)
        print('se está limpiando el almacenamiento, por favor espere')
        time.sleep(15)

    
    container_client = blob_service_client.create_container(container_name)
    print('contenedor creado')
     #Crear Directorio Local para almacenar los archivos 
    local_path='./data'
    if os.path.exists('./data'):
        sh.rmtree('./data')
        
    os.mkdir(local_path)
except Exception as ex:
    print('Exception:')
    print(ex)

df_titles = pd.read_csv("./titles.csv")
df_credits = pd.read_csv("./credits.csv")

#unir los dos datasets para obtener los actores por titulo
df_tc = pd.merge(df_titles,df_credits,how='inner')
#guardar dataframe
nombre_archivo= 'df_merged.csv'
ruta_upload = os.path.join(local_path,nombre_archivo)
df_tc.to_csv(ruta_upload)
#inicializar blob storage en  azure
blob_client = blob_service_client.get_blob_client(container=container_name, blob=nombre_archivo)
print('subiendo archivo a azure storage com blob: \n\t'+ nombre_archivo)
#subir archivo al blob storage de  azure
with open(ruta_upload,'rb') as data:
    blob_client.upload_blob(data)
    print('archivo cargado correctamente')

print("\n")

#conteo tipos PELICULA/SHOW
print('\n---------CONTEO DE TIPOS---------')
df_tipos =df_titles.value_counts(subset=['type'])
nombre_archivo= 'df_tipos.csv'
ruta_upload = os.path.join(local_path,nombre_archivo)
df_tipos.to_csv(ruta_upload)
#inicializar blob storage en  azure
blob_client = blob_service_client.get_blob_client(container=container_name, blob=nombre_archivo)
print('subiendo archivo a azure storage com blob: \n\t'+ nombre_archivo)
#subir archivo al blob storage de  azure
with open(ruta_upload,'rb') as data:
    blob_client.upload_blob(data)
    print('archivo cargado correctamente '+nombre_archivo)


#Los generos más lanzados en cada año
print('\n---------años de lanzamiento por genero---------')
df_genres_year = df_titles.value_counts(subset=['release_year', 'genres']).head(10)
print(df_genres_year)
nombre_archivo= 'df_genres_year.csv'
ruta_upload = os.path.join(local_path,nombre_archivo)
df_genres_year.to_csv(ruta_upload)
#inicializar blob storage en  azure
blob_client = blob_service_client.get_blob_client(container=container_name, blob=nombre_archivo)
print('subiendo archivo a azure storage com blob: \n\t'+ nombre_archivo)
#subir archivo al blob storage de  azure
with open(ruta_upload,'rb') as data:
    blob_client.upload_blob(data)
    print('archivo cargado correctamente '+nombre_archivo)


#Los directores mas ofertados
print('\n---------Los directores mas ofertados---------')
df_directores = df_tc.loc[df_tc['role']=='DIRECTOR']
print(df_directores.value_counts(subset=['name']).head(10))
nombre_archivo= 'directores.csv'
ruta_upload = os.path.join(local_path,nombre_archivo)
df_directores.to_csv(ruta_upload)
#inicializar blob storage en  azure
blob_client = blob_service_client.get_blob_client(container=container_name, blob=nombre_archivo)
print('subiendo archivo a azure storage com blob: \n\t'+ nombre_archivo)
#subir archivo al blob storage de  azure
with open(ruta_upload,'rb') as data:
    blob_client.upload_blob(data)
    print('archivo cargado correctamente '+nombre_archivo)

#los actores mas ofertados
print('\n---------los actores mas ofertados---------')
df_actores = df_tc.loc[df_tc['role']=='ACTOR']
df_mejores_actores = df_actores.value_counts(subset=['name']).head(10)
nombre_archivo= 'df_actores.csv'
ruta_upload = os.path.join(local_path,nombre_archivo)
df_mejores_actores.to_csv(ruta_upload)
#inicializar blob storage en  azure
blob_client = blob_service_client.get_blob_client(container=container_name, blob=nombre_archivo)
print('subiendo archivo a azure storage com blob: \n\t'+ nombre_archivo)
#subir archivo al blob storage de  azure
with open(ruta_upload,'rb') as data:
    blob_client.upload_blob(data)
    print('archivo cargado correctamente '+nombre_archivo)


# creación y almacenamiento de los paises con más lanzamientos 
print('\n---------los paises con mas lanzamientos---------')
df_paisesxprod = df_titles.value_counts(subset=['production_countries']).head(10)
print(df_paisesxprod)

nombre_archivo= 'df_paises.csv'
ruta_upload = os.path.join(local_path,nombre_archivo)
df_paisesxprod.to_csv(ruta_upload)
#inicializar blob storage en  azure
blob_client = blob_service_client.get_blob_client(container=container_name, blob=nombre_archivo)
print('subiendo archivo a azure storage com blob: \n\t'+ nombre_archivo)
#subir archivo al blob storage de  azure
with open(ruta_upload,'rb') as data:
    blob_client.upload_blob(data)
    print('archivo cargado correctamente '+nombre_archivo)






