from django.http import HttpResponse

def credits(request):
    content = "Nicky\nKyle"

    return HttpResponse(content, content_type="text/plain")

def about(request):
    content = "<h1>About page</h1>"

    return HttpResponse(content, content_type="text/html")

def version(request):
    version = "1"

    content = f"web site version {version}"

    return HttpResponse(content, content_type="application/json")
