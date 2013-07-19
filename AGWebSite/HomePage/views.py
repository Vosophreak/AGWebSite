from django.http import HttpResponse
from django.shortcuts import render
import datetime
import bootstrap

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><link href=\"{{STATIC_URL}}/bootstrap/css/bootstrap.css\" rel=\"stylesheet\">\
            <link href=\"{{STATIC_URL}}/bootstrap/css/bootstrap-responsive.css\" rel=\"stylesheet\">\
            <body>It is now %s. </body></html>" % now
    return render(request, 'main.html')

