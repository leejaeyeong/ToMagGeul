from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .forms import UserCreationForm, AuthorCreationForm

def signup(request):
    user_form = UserCreationForm()
    author_form = AuthorCreationForm()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if user.is_author:
                author_form = AuthorCreationForm(request.POST, request.FILES)
                if author_form.is_valid():
                    author = author_form.save(commit=False)
                    user.save()
                    author.user = user
                    author.save()

                    return redirect('thank')
            else:
                user.save()
                return redirect('thank')
 
    return render(request, 'signup.html', {'regi_form':user_form, 'author_form':author_form})

def thankyou(request):
    return render(request, 'thankyou.html')