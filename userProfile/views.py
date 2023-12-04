from django.shortcuts import render, redirect
from .models import userProfile
from django.contrib.auth.forms import UserCreationForm

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save
            userProfile.objects.create(user = user)

            return redirect('/login/')

    else:
        form = UserCreationForm()
    
    form = UserCreationForm()

    return render(request, 'userProfile/signup',{
        'form' : form
    })