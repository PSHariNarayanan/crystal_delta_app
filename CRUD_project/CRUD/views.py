from django.shortcuts import render

# login view 
def login(request) : 
    return render(request,'login.html')

def loginHandler(request) :



    return render(request,'projects.html')

def signUp(request) :
    return render(request,'signup.html')

def signupHandler(request) :


    return render(request,'projects.html')