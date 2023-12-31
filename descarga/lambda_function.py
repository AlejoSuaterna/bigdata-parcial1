import requests
import boto3
from datetime import datetime


def lambda_handler(event, context):

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
            s3_path = (
                f'{s3_base_path}/{newspaper}/{now.strftime("%Y-%m-%d")}.html'
            )

            # Subir el contenido a S3
            s3_client = boto3.client('s3')
            s3_client.put_object(
                Body=content,
                Bucket=s3_bucket_name,
                Key=s3_path
            )

            print(
                f'Página descargada y almacenada en S3: {s3_path}'
            )
        else:
            print(f'Error al descargar la página: {response.status_code}')

    return {
        'statusCode': 200,
        'body': 'Páginas descargadas y almacenadas en S3'
    }
