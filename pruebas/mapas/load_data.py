# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from models import *

ferrocarril_mapping = {
    'nombre' : 'Nombre',
    'geometria' : 'MULTILINESTRING'
}
lagos_mapping = {
    'nombre' : 'Nombre',
    'geometria': 'MULTIPOLYGON'
}
caminos_mapping = {
    '_id' : 'Id',
    'material' : 'Material',
    'estado' : 'Estado',
    'sentido' : 'Sentido',
    'distancia' : 'Distancia',
    'fecantigue' : 'FecAntigue',
    'fecmejora' : 'FecMejora',
    'nombre' : 'Nombre',
    'nrocalle' : 'NroCalle',
    'geometria' : 'MULTILINESTRING'
}
zonaindustrial_mapping = {
    'produccion' : 'Produccion',
    'tipo' : 'Tipo',
    'empresa' : 'Empresa',
    'geometria' : 'MULTIPOLYGON'
}


shapes = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.dirname('data/Parcelas.shp')))

def run(verbose=True):
    print "Shapes: %s" % shapes
    
    print ">>> Importando Ferrocarriles"
    lm = LayerMapping(Ferrocarril, shapes, ferrocarril_mapping, transform=True, layer=0)
    lm.save(verbose=verbose)

    print ">>> Importando Lagos"
    lm = LayerMapping(Lagos, shapes, lagos_mapping, transform=True, layer=1)
    #lm.save(verbose=verbose)

    print ">>> Importando Caminos"
    lm = LayerMapping(Caminos, shapes, caminos_mapping, transform=True, layer=3)
    lm.save(verbose=verbose)

    print ">>> Importando Zona Industrial"
    lm = LayerMapping(ZonaIndustrial, shapes, zonaindustrial_mapping, transform=True, layer=4)
    lm.save(verbose=verbose)

    