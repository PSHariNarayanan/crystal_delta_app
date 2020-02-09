from django.shortcuts import render,redirect
from .models import User
import re

# view for basic login
def login(request) : 
    return render(request,'login.html')

# view for handling login
def loginHandler(request) :
    username = request.POST.get('username')
    password_form = request.POST.get('password')
    if not username and not password_form :
        return redirect('login')
    else : 
        user_details = User.objects.get(username=username)
        if not user_details :
            return redirect('login')
        password_db = user_details.password
        print(password_db)
        if password_db==password_form :
            return redirect('projects')
        else :
            return redirect('login')

# view for basic signup
def signUp(request) :
    return render(request,'signup.html')

# view for handling signup
def signupHandler(request) :
    email = request.POST.get('email')
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex,email) :
        return redirect('signup')
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1!=password2 :
         return redirect('signup')
    user = User(username=username,email=email,password=password1)
    user.save()
    return redirect('projects')