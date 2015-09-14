from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello World")

def home_page(request):
    return HttpResponse("homepage")

def num_add(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    s = 0
    for i in range(offset+1):
        s += i
    return HttpResponse(s)

def time_add(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>It is %s,<br />In %s hours<br />It will be %s.</body></html>' %(now, offset, dt)
    return HttpResponse(html)
