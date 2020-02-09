from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import User,Project
import re

# view for basic login
def login(request) : 
    if request.session.has_key('user_id') :
        return redirect('projects')
    else :
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
            request.session['user_id']=user_details.id
            return redirect('projects')
        else :
            return redirect('login')

# view for basic signup
def signUp(request) :
    if request.session.has_key('user_id') :
        return redirect('projects')
    return render(request,'signup.html')

# view for handling signup
def signUpHandler(request) :
    email = request.POST.get('email')
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex,email) :
        return redirect('signUp')
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1!=password2 :
         return redirect('signUp')
    user = User(username=username,email=email,password=password1)
    user.save()
    request.session['user_id'] = user.id
    return redirect('projects')

def projects(request) :
    if request.session.has_key('user_id'):
      user_id = request.session['user_id']
      projectList = Project.objects.all().filter(user_id=user_id)
      return render(request,'projects.html',{'projectList' : projectList})
    else :
        return redirect('login')

def createProject(request) :
    return render(request,'addProject.html')

def createProjectHandler(request) : 
    if request.session.has_key('user_id') :
        user_id = request.session['user_id']
        name = request.POST.get('name')
        description = request.POST.get('description')
        project = Project(user_id=user_id,name=name,description=description,createdOn=timezone.now())
        project.save()
        print(project)
        return redirect('projects')
