from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello, this is my world.")