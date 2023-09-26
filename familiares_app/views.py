from django.shortcuts import render
from .models import Familiar
# Create your views here.
def home(req):
    familiares = Familiar.objects.all()
    return render(req,"index.html", {"familiares":familiares})


