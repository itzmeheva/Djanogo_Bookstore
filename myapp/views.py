from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    id = '001'
    name = 'Somchai'
    email = 'somchai@mail.com'
    activities = [
        'Football',
        'Running',
        'Badminton',
        ]

    return render(request, 'index.html', {
        'id': id,
        'name': name,
        'email': email,
        'activities': activities,
    })

def hello(request, id):
    return HttpResponse('Hello World Id=' + str(id))

def article(request, year, slug):
    return HttpResponse('Article Year=' + str(year) + 'slug=' + slug)

