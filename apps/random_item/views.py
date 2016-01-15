from django.shortcuts import render
from .models import Word


def index(request):
    words = Word.objects.order_by("text")
    context = {'words': words}
    return render(request, 'random_item/index.html', context)
