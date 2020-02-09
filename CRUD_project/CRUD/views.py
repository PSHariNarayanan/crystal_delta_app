from django.shortcuts import render

# login view 
def login(request) : 
    return render(request,'login.html')

def loginHandler(request) : 
    return render(request,'projects.html')