from django.http import HttpResponse


def get_posts(request):
    return HttpResponse("List Of Posts")
