from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.methos == 'POST':
        # print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            # Ready to be saved, but don't save the form
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            form.save()
            messages.success(request,"Your account has been registered successfully!")
            # create the user using create user method
            
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # user = User.objects.create(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
            # user.role = User.CUSTOMER
            # user.save()
            
            return redirect('register-user')
        else:
            print("Invalid form")
            print(form.errors)
    else:
        form = UserForm()
    context = {
        "form": form,
    }
    return render(request,'accounts/registerUser.html',context=context)
