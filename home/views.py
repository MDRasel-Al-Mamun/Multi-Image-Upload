from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Doc


class HomeView(TemplateView):
    template_name = 'home/index.html'


def uploadView(request):
    if request.method == 'POST':
        files = request.FILES.get('file')
        Doc.objects.create(upload=files)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})
