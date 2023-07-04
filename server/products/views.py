from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello.html', {'items': [1, 2, 34, 5, 5, 45]})
