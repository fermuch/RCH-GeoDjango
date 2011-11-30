# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mapas.models import *


def index(request):
    ferrocarril = Ferrocarril.objects.all()
    return render_to_response('mapas/index.html', {
        'ferrocarril': ferrocarril,
    })
