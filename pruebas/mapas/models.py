# -*- coding: utf-8 -*-
from django.contrib.gis.db import models

# TODO: poner __unicode__


class Ferrocarril(models.Model):
	nombre = models.CharField(max_length=45)

	mpoly = models.MultiLineStringField()
	objects = models.GeoManager()

class Lagos(models.Model):
	nombre = models.CharField(max_length=45)
	t = models.IntegerField()
	supm2 = models.FloatField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class GridX(models.Model):
	extx = models.FloatField()
	exty = models.FloatField()
	extz = models.FloatField()

	mpoly = models.MultiLineStringField()
	objects = models.GeoManager()

class Caminos(models.Model):
	_id = models.IntegerField()
	material = models.CharField(max_length=20)
	estado = models.CharField(max_length=20)
	sentido = models.CharField(max_length=20)
	distancia = models.FloatField()
	permeable = models.IntegerField(max_length=4)
	fecantigue = models.CharField(max_length=10)
	fecmejora = models.CharField(max_length=10)
	nombre = models.CharField(max_length=50)
	nrocalle = models.IntegerField()

	mpoly = models.MultiLineStringField()
	objects = models.GeoManager()

class ZonaIndustrial(models.Model):
	produccion = models.CharField(max_length=50)
	tipo = models.CharField(max_length=30)
	empresa = models.CharField(max_length=50)
	supm2 = models.FloatField()
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class LineaCostera(models.Model):
	_id = models.IntegerField()

	mpoly = models.MultiLineStringField()
	objects = models.GeoManager()

class AUC(models.Model):
	supm2 = models.FloatField()
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class CursosAgua(models.Model):
	tipo = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	dist = models.FloatField()

	mpoly = models.MultiLineStringField()
	objects = models.GeoManager()

class Manzanas(models.Model):
	id_manz = models.CharField(max_length=50)
	manz_ant = models.CharField(max_length=10)
	zona = models.CharField(max_length=10)
	manzana = models.CharField(max_length=10)
	nomencla = models.CharField(max_length=30)
	x = models.FloatField()
	y = models.FloatField()
	supm2 = models.FloatField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class Barrios(models.Model):
	barrio = models.CharField(max_length=50)
	area = models.FloatField()
	has = models.FloatField()
	sector = models.CharField(max_length=3)
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class EspaciosVerdes(models.Model):
	nombre = models.CharField(max_length=50)
	supm2 = models.FloatField()
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class Cementerio(models.Model):
	nombre = models.CharField(max_length=50)
	supm2 = models.FloatField()
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()


class Puentes(models.Model):
	material = models.CharField(max_length=20)
	atraviesa = models.CharField(max_length=20)
	nombre = models.CharField(max_length=50)
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()


class Parcelas(models.Model):
	id_cad = models.CharField(max_length=50)
	adrema = models.CharField(max_length=30)
	manz_ant = models.CharField(max_length=10)
	nomencla = models.CharField(max_length=30)
	barrio = models.CharField(max_length=50)
	zona = models.CharField(max_length=30)
	manzana = models.CharField(max_length=10)
	parcela = models.CharField(max_length=10)
	direccion = models.CharField(max_length=80)
	portal = models.CharField(max_length=10)
	salecalle = models.IntegerField()
	notas = models.CharField(max_length=150)
	agua = models.IntegerField()
	cloaca = models.IntegerField()
	alumbrado = models.IntegerField()
	limpieza = models.IntegerField()
	supm2 = models.FloatField()
	sup_const = models.FloatField()
	sup_pisc = models.FloatField()
	sup_dif = models.FloatField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()


class Piscinas(models.Model):
	publica = models.IntegerField()
	club = models.CharField(max_length=50)
	nomenclatu = models.CharField(max_length=30)
	supm2 = models.FloatField()
	perimetro = models.FloatField()
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()


class SitiosInteres(models.Model):
	x = models.FloatField()
	y = models.FloatField()
	tipo = models.CharField(max_length=20)
	detalle = models.CharField(max_length=30)

	mpoly = models.MultiPointField()
	objects = models.GeoManager()

class AreasDeportivas(models.Model):
	cancha = models.CharField(max_length=25)
	club = models.CharField(max_length=50)
	supm2 = models.FloatField()
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class Aeropuerto(models.Model):
	nombre = models.CharField(max_length=50)
	supm2 = models.FloatField()
	perimetro = models.FloatField()
	t = models.IntegerField()

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()

class GridY(models.Model):
	extx = models.FloatField()
	exty = models.FloatField()
	extz = models.FloatField()

	mpoly = models.MultiLineStringField()
	objects = models.GeoManager()


class AllParcelas(models.Model):
	fid = models.IntegerField()
	entity = models.CharField(max_length=16)
	handle = models.CharField(max_length=16)
	layer = models.CharField(max_length=254)
	lyrfrzn = models.IntegerField()
	lyrlock = models.IntegerField()
	lyron = models.IntegerField()
	lyrvpfrzn = models.IntegerField()
	lyrhandle = models.CharField(max_length=16)
	color = models.IntegerField()
	entcolor = models.IntegerField()
	lyrcolor = models.IntegerField()
	blkcolor = models.IntegerField()
	linetype = models.CharField(max_length=254)
	entlinetyp = models.CharField(max_length=254)
	lyrlntype = models.CharField(max_length=254)
	blklinetyp = models.CharField(max_length=254)
	elevation = models.FloatField()
	thickness = models.FloatField()
	linewt = models.IntegerField()
	entlinewt = models.IntegerField()
	lyrlinewt = models.IntegerField()
	blklinewt = models.IntegerField()
	refname = models.CharField(max_length=254)
	ltscale = models.FloatField()
	extx = models.FloatField()
	exty = models.FloatField()
	extz = models.FloatField()
	docname = models.CharField(max_length=254)
	docpath = models.CharField(max_length=254)
	doctype = models.CharField(max_length=32)
	docver = models.CharField(max_length=16)
	nuevo_lote = models.CharField(max_length=4)

	mpoly = models.MultiPolygonField()
	objects = models.GeoManager()