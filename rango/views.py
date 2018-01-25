from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "crunchy, creamy, cookie, candy, cupcake"}
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("rango says yo <br/> <a href='/rango/about/'>About</a>") #, html)

def about(request):
    #return HttpResponse("rango says here is the about page <br/> <a href = '/rango/'>Index</a>")
    return render(request, 'rango/about.html')
