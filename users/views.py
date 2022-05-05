from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm


def register(request):
    """
    This function lets a user register for an account.
    The register function also checks if the account already exists.
    """
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})