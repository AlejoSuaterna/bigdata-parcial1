import os
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Obtener la URL del periódico a descargar
    url = "https://www.eltiempo.com/"

    # Realizar la descarga
    response = requests.get(url)
    content = response.content

    # Almacenar en S3
    s3 = boto3.client("s3")
    bucket_name = "parcialc1"
    current_date = datetime.now().strftime("%Y-%m-%d")
    s3_key = f"news/raw/contenido-{current_date}.html"
    
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=content)
