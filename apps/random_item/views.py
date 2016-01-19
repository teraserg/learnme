from django.shortcuts import render
from .models import Dictionary


def random_item(request):
    r_item = Dictionary.objects.order_by("?").first()
    context = {'r_item': r_item}
    return render(request, 'random_item/index.html', context)
