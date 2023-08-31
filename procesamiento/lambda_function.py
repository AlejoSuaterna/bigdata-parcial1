import os
import boto3
from bs4 import BeautifulSoup
from datetime import datetime
import csv

def lambda_handler(event, context):
    # Conectar a S3
    s3 = boto3.client("s3")
    bucket_name = "parcialc1"
    current_date = datetime.now().strftime("%Y-%m-%d")
    s3_key = f"news/raw/contenido-{current_date}.html"
    
    # Obtener el contenido HTML desde S3
    response = s3.get_object(Bucket=bucket_name, Key=s3_key)
    content = response["Body"].read()
    
    # Procesar con Beautiful Soup
    soup = BeautifulSoup(content, "html.parser")
    # ... Aquí realiza el procesamiento, extrayendo categoría, titular y enlace

    # Guardar en un archivo CSV local
    csv_filename = f"/tmp/news_{current_date}.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Categoría", "Titular", "Enlace"])
        # ... Aquí agrega las filas al CSV

    # Subir el archivo CSV a S3
    s3_key_processed = f"headlines/final/periodico=eltiempo/year={current_date[:4]}/month={current_date[5:7]}/{current_date}.csv"
    s3.upload_file(csv_filename, bucket_name, s3_key_processed)
