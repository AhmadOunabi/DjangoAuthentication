from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm , ActivationForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            form.save()
            # Send Email
            user=User.objects.get(username=username)
            user_profile=Profile.objects.get(user=user)
            send_mail(
                "Activation Code",
                f"Hello {username} \n use this Code to activate your account \n {user_profile.code}",
                "ahmad@yahoo.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'{username}/activate')
    else:
        form= SignupForm()
    return render(request,'signup.html',{'form':form})


def activate(request, username):
    user=User.objects.get(username=username)
    user_profile=Profile.objects.get(user=user)
    if request.method == 'POST':
        form=ActivationForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == user_profile.code:
                user.is_active == True
                user.save()
                user_profile.code=''
                user_profile.save()
                return redirect('/')
    else:
        form=ActivationForm()
    return render(request,'activate.html',{'form':form} )



def signin(request):
    if request.method == 'POST':
        print('POST')
        form=LoginForm(request.POST)
        if form.is_valid():
            print('VALID')
            username = request.POST.get('username')
            password= request.POST.get('password')
            user=authenticate(request,username=username, password=password)
            
            if user is not None:
                print('Loggedin successfully')
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,f'Invalid username or password')
                print('Login failed')
    else:
        print('Login failed')
        form=LoginForm()
    return render(request,'signin.html',{'form':form})