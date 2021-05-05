from django.shortcuts import render
from django.template import RequestContext
from templates.registration import *

# Create your views here.
def fileupload(request):
    return render(request, 'registration/fileupload.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')