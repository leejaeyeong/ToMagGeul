from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreationForm, AuthorCreationForm

def signup(request):
    regi_form = UserCreationForm()
    author_form = AuthorCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        # print(filled_form)
        if filled_form.is_valid():
            print('Valid!')
        #     # filled_form.save()
        #     return redirect('index')

    return render(request, 'signup.html', {'regi_form':regi_form, 'author_form':author_form})