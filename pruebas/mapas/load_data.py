# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from models import *


### BUGFIX mágico para solucionar problemas de la base de datos ###
from django.db import connection
connection.connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")
###################################################################

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
lineacostera_mapping = {
    '_id' : 'Id',
    'geometria' : 'MULTILINESTRING'
}
auc_mapping = {
    'geometria' : 'MULTIPOLYGON'
}
cursosagua_mapping = {
    'tipo' : 'Tipo',
    'nombre' : 'Nombre',
    'dist' : 'Dist',
    'geometria' : 'MULTILINESTRING'
}
manzanas_mapping = {
    'id_manz' : 'ID_MANZ',
    'manz_ant' : 'Manz_Ant',
    'zona' : 'Zona',
    'manzana' : 'Manzana',
    'nomencla' : 'Nomencla',
    'x' : 'X',
    'y' : 'Y',
    'geometria' : 'MULTIPOLYGON'
}
barrios_mapping = {
    'barrio' : 'Barrio',
    'area' : 'Area',
    'has' : 'Has',
    'sector' : 'Sector',
    'geometria' : 'MULTIPOLYGON'
}
espaciosverdes_mapping = {
    'nombre' : 'Nombre',
    'geometria' : 'MULTIPOLYGON'
}
cementerio_mapping = {
    'nombre' : 'Nombre',
    'geometria' : 'MULTIPOLYGON'
}
puentes_mapping = {
    'material' : 'Material',
    'atraviesa' : 'Atraviesa',
    'nombre' : 'Nombre',
    'geometria' : 'MULTIPOLYGON'
}
parcelas_mapping = {
    'id_cad' : 'ID_CAD',
    'adrema' : 'ADREMA',
    'manz_ant' : 'Manz_Ant',
    'nomencla' : 'Nomencla',
    'barrio' : 'Barrio',
    'zona' : 'Zona',
    'manzana' : 'Manzana',
    'parcela' : 'Parcela',
    'direccion' : 'Direccion',
    'portal' : 'Portal',
    'salecalle' : 'SaleCalle',
    'notas' : 'Notas',
    'agua' : 'Agua',
    'cloaca' : 'Cloaca',
    'alumbrado' : 'Alumbrado',
    'limpieza' : 'Limpieza',
    'sup_const' : 'Sup_Const',
    'sup_pisc' : 'Sup_Pisc',
    'sup_dif' : 'Sup_Dif',
    'geometria' : 'MULTIPOLYGON'
}
piscinas_mapping = {
    'publica' : 'Publica',
    'nomenclatu' : 'Nomenclatu',
    'perimetro' : 'Perimetro',
    'geometria' : 'MULTIPOLYGON'
}
sitiosinteres_mapping = {
    'x' : 'x',
    'y' : 'y',
    'tipo' : 'Tipo',
    'detalle' : 'Detalle',
    'geometria' : 'MULTIPOINT'
}
areasdeportivas_mapping = {
    'cancha' : 'Cancha',
    'club' : 'Club',
    'geometria' : 'MULTIPOLYGON'
}
aeropuerto_mapping = {
    'nombre' : 'Nombre',
    'perimetro' : 'Perimetro',
    'geometria' : 'MULTIPOLYGON'
}
allparcelas_mapping = {
    'fid' : 'FID_',
    'entity' : 'Entity',
    'handle' : 'Handle',
    'layer' : 'Layer',
    'lyrfrzn' : 'LyrFrzn',
    'lyrlock' : 'LyrLock',
    'lyron' : 'LyrOn',
    'lyrvpfrzn' : 'LyrVPFrzn',
    'lyrhandle' : 'LyrHandle',
    'color' : 'Color',
    'entcolor' : 'EntColor',
    'lyrcolor' : 'LyrColor',
    'blkcolor' : 'BlkColor',
    'linetype' : 'Linetype',
    'entlinetyp' : 'EntLinetyp',
    'lyrlntype' : 'LyrLnType',
    'blklinetyp': 'BlkLinetyp',
    'elevation' : 'Elevation',
    'thickness' : 'Thickness',
    'linewt' : 'LineWt',
    'entlinewt' : 'EntLineWt',
    'lyrlinewt' : 'LyrLineWt',
    'blklinewt' : 'BlkLineWt',
    'refname' : 'RefName',
    'ltscale' : 'LTScale',
    'extx' : 'ExtX',
    'exty' : 'ExtY',
    'extz' : 'ExtZ',
    'docname' : 'DocName',
    'docpath' : 'DocPath',
    'doctype' : 'DocType',
    'docver' : 'DocVer',
    'nuevo_lote' : 'NUEVO_LOTE',
    'geometria' : 'MULTIPOLYGON'
}

shapes = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.dirname('data/Parcelas.shp')))

def run(verbose=True):
    print "Shapes: %s" % shapes
    
    print "#>>> Importando Ferrocarriles"
    lm = LayerMapping(Ferrocarril, shapes, ferrocarril_mapping, transform=True, layer=0)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Lagos"
    lm = LayerMapping(Lagos, shapes, lagos_mapping, transform=True, layer=1)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Caminos"
    lm = LayerMapping(Caminos, shapes, caminos_mapping, transform=True, layer=3)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Zona Industrial"
    lm = LayerMapping(ZonaIndustrial, shapes, zonaindustrial_mapping, transform=True, layer=4)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Línea Costera"
    lm = LayerMapping(LineaCostera, shapes, lineacostera_mapping, transform=True, layer=5)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando AUC"
    lm = LayerMapping(AUC, shapes, auc_mapping, transform=True, layer=6)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Cursos Agua"
    lm = LayerMapping(CursosAgua, shapes, cursosagua_mapping, transform=True, layer=7)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Manzanas"
    lm = LayerMapping(Manzanas, shapes, manzanas_mapping, transform=True, layer=8)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Barrios"
    lm = LayerMapping(Barrios, shapes, barrios_mapping, transform=True, layer=9)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Espacios Verdes"
    lm = LayerMapping(EspaciosVerdes, shapes, espaciosverdes_mapping, transform=True, layer=10)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Cementerio"
    lm = LayerMapping(Cementerio, shapes, cementerio_mapping, transform=True, layer=11)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Puentes"
    lm = LayerMapping(Puentes, shapes, puentes_mapping, transform=True, layer=12)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Parcelas"
    # TODO: un polígono tiene errores al importar, por eso saqué el strict.
    lm = LayerMapping(Parcelas, shapes, parcelas_mapping, transform=True, layer=13)
    #lm.save(verbose=False, strict=False, progress=True)

    print "#>>> Importando Piscinas"
    lm = LayerMapping(Piscinas, shapes, piscinas_mapping, transform=True, layer=14)
    #lm.save(verbose=False, strict=True, progress=True)

    print "#>>> Importando Sitios de Interés"
    lm = LayerMapping(SitiosInteres, shapes, sitiosinteres_mapping, transform=True, layer=15)
    #lm.save(verbose=False, strict=True, progress=True)
    
    print "#>>> Importando Áreas Deportivas"
    lm = LayerMapping(AreasDeportivas, shapes, areasdeportivas_mapping, transform=True, layer=16)
    #lm.save(verbose=False, strict=True, progress=True)
    
    print "#>>> Importando Aeropuerto"
    lm = LayerMapping(Aeropuerto, shapes, aeropuerto_mapping, transform=True, layer=17)
    #lm.save(verbose=False, strict=True, progress=True)
    
    print "#>>> Importando All Parcelas"
    # TODO: un polígono tiene errores al importar, por eso saqué el strict.
    lm = LayerMapping(AllParcelas, shapes, allparcelas_mapping, transform=True, layer=19)
    lm.save(verbose=False, strict=False, progress=True)




    print "#>>> Finalizado! :D"