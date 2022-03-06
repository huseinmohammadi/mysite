from django.http import HttpResponse , JsonResponse

def httpreq(request):
    return HttpResponse('<b> Hello World </b>')

def json_test(request):
    return JsonResponse({'name':'ali'})