from django.http import HttpResponse , JsonResponse

def home_view(request):
    return HttpResponse('<h1>home Page</h1>')

def about_view(request):
    return HttpResponse('<h1>About Page</h1>')

def contact_view(request):
    return HttpResponse('<h1>Contact Page</h1>')
    