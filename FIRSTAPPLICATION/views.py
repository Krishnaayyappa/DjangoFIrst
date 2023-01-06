from django.shortcuts import render, redirect
from .forms import DetailsForm
from .models import Name
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "home.html")


def showDetails(request):
    details = Name.objects.all()
    return render(request, 'showdetails.html', {'details':details})

def addDetails(request):
    if request.method == "POST":
        form = DetailsForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Details were added sucessfully"))
            return redirect("adddetails")
    

    return render(request, 'adddetails.html')


