#!/usr/bin/env python

import datetime
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello World !')

def my_homepage_view(request):
    return HttpResponse('Home Page !')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' %now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hours, it will be %s.</body></html>' %(offset,dt)
    return HttpResponse(html)

def sum_n(request,nnum):
    try:
        nnum = int(nnum)
    except ValueError:
        raise Http404() 
    s = 0
    for i in range(nnum):
        s += i
    html = '<html><body>%s.</body></html>' %s
    return HttpResponse(html)
