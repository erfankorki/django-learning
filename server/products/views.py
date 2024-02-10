from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def say_hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello!!!")
