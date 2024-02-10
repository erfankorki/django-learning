from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def get_products(request) -> HttpResponse:
    return HttpResponse("HELLO")
