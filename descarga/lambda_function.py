import os
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # # Obtener la URL del periódico a descargar
    # url = "https://www.eltiempo.com/"

    # # Realizar la descarga
    # response = requests.get(url)
    # content = response.content

    # # Almacenar en S3
    # s3 = boto3.client("s3")
    # bucket_name = "parcialc1"
    # current_date = datetime.now().strftime("%Y-%m-%d")
    # s3_key = f"news/raw/contenido-{current_date}.html"
    
    # s3.put_object(Bucket=bucket_name, Key=s3_key, Body=content)

    s3_bucket_name = 'parcialc1'
    s3_base_path = 'news/raw'

    newspapers = ['eltiempo', 'elespectador']  # Lista de periódicos

    for newspaper in newspapers:
        url = f'https://www.{newspaper}.com'
        response = requests.get(url)

        if response.status_code == 200:
            content = response.content

            # Generar la ruta en S3
            now = datetime.now()
            s3_path = f'{s3_base_path}/{newspaper}/{now.strftime("%Y-%m-%d")}.html'

            # Subir el contenido a S3
            s3_client = boto3.client('s3')
            s3_client.put_object(Body=content, Bucket=s3_bucket_name, Key=s3_path)

            print(f'Página de {newspaper} descargada y almacenada en S3: {s3_path}')
        else:
            print(f'Error al descargar la página de {newspaper}: {response.status_code}')

    return {
        'statusCode': 200,
        'body': 'Páginas descargadas y almacenadas en S3'
    }
