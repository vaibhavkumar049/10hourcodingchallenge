from django.shortcuts import render
from django.utils.safestring import mark_safe

def index(request):
    return render(request, 'chat/index.html', {})

# Create your views here.
