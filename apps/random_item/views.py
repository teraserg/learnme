from django.shortcuts import render
from .models import Dictionary


def index(request):
    items = Dictionary.objects.order_by("item")
    context = {'items': items}
    return render(request, 'random_item/index.html', context)
