from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def RegisterUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username') # for alert messages
            messages.success(request, f'Account successfully created for {user_name}')
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def Profile(request):
    return render(request, 'profile.html')