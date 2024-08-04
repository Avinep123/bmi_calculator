from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def home(request):
    return render(request, 'bmi/home.html')

def calculate_bmi(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('view_data')
    else:
        form = UserForm()
    return render(request, 'bmi/calculate_bmi.html', {'form': form})

def view_data(request):
    users = User.objects.all()
    return render(request, 'bmi/view_data.html', {'users': users})

def suggestions(request, bmi_classification):
    return render(request, 'bmi/suggestions.html', {'bmi_classification': bmi_classification})
