from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.


def index(request):
   all_items = Suplement.objects.all()
   return render(request, 'index.html', context={"items" : all_items})


def supplements(request, id):
    item = get_object_or_404(Suplement, pk=id)
    return render(request, 'supplements.html', context={"item": item})