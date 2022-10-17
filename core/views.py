from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

# Create your views here.

def frontpage(request):
    return render(request, 'core/frontpage.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
        
    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {'form': form})
