from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'all_dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    if request.method == 'POST':
        new_dojo = Dojo.objects.create(
            name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    return redirect('/')

def create_ninja(request):
    if request.method == 'POST':
        new_ninja = Ninja.objects.create(
            first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo = Dojo.objects.get(id= request.POST['dojo']))
    return redirect('/')

    pass

# Create your views here.
