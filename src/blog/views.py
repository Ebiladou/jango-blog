from django.http import HttpResponse

def blog (request):
    return HttpResponse ('blog is up')
