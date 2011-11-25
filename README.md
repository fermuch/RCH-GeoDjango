# Proyecto con «GeoDjango» de «RCHIT»

## ¿Cómo instalar la base de datos?
ejecutar ./pruebas/generate_db.sh

## ¿Cómo importar los datos?
python ./pruebas/manage.py
>>> from mapas import load_data
>>> load_data.run()
