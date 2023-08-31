# Proyecto de Pipeline de Datos con AWS Lambda y Zappa

Este proyecto tiene como objetivo implementar un pipeline de datos utilizando AWS Lambda y Zappa para la descarga y procesamiento de información de los periódicos "El Tiempo" y "El Espectador".

## Estructura del Proyecto

- `lambda_function.py`: Contiene el código de la función Lambda para descargar y procesar los datos de los periódicos.
- `zappa_settings.json`: Archivo de configuración para Zappa, donde se especifican las opciones de despliegue.
- `requirements.txt`: Archivo que lista las dependencias del proyecto.
- `.gitignore`: Archivo que especifica los archivos y carpetas a ignorar en el control de versiones.
- `README.md`: Documentación del proyecto.

## Requisitos

- Python 3.7+
- AWS Account y configuración de credenciales
- Zappa instalado (`pip install zappa`)

## Configuración y Uso

1. Clona este repositorio: `git clone https://github.com/tu-usuario/tu-repo.git`
2. Crea un entorno virtual y activa el entorno.
3. Instala las dependencias: `pip install -r requirements.txt`
4. Configura tus credenciales de AWS utilizando el AWS CLI o archivos de configuración.
5. Actualiza el archivo `zappa_settings.json` con tu configuración personalizada.
6. Implementa la función Lambda utilizando Zappa: `zappa deploy dev`
7. Ejecuta la función Lambda para descargar y procesar los datos.

## Estructura de Carpetas en S3

- `news/raw/`: Carpeta donde se almacenan los archivos HTML descargados de los periódicos.
- `headlines/final/`: Carpeta donde se almacenan los archivos CSV con los datos procesados.

## Notas Adicionales

- Asegúrate de que el bucket `parcialc1` exista en tu cuenta de AWS y tenga la estructura de carpetas adecuada.
- Verifica que las variables de ruta en el código (`s3_key` y `s3_key_processed`) correspondan a las rutas correctas en tu bucket.
- Puedes ajustar las configuraciones de Zappa en el archivo `zappa_settings.json` según tus necesidades.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes mejoras que sugerir, no dudes en abrir un problema o enviar un pull request.
