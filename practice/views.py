from django.shortcuts import render
from .models import State


# Create your views here.
def index(request):
    states = State.objects.all()
    context = {
        "states": states
    }
    return render(request, "practice/index.html", context)
