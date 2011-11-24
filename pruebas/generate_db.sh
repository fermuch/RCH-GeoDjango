#!/bin/sh
echo "eliminando db vieja\n"
rm 'geodjango.db'
echo "creando base de datos nueva"
spatialite geodjango.db < '../init-spatialite.sql'
echo "sincronizando db"
python ./manage.py syncdb
