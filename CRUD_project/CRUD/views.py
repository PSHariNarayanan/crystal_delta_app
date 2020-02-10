from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import User,Project
import re

def home(request) : 
    return render(request,'home.html')
'''
login checks for user-login status using session
and directs to projects page else redirects to login page
'''
def login(request) : 
    if request.session.has_key('userID') :
        return redirect('projects')
    else :
       return render(request,'login.html')

'''
loginHandler validates user credentials from login page against DB 
and directs to projects page else redirects to login page
'''
def loginHandler(request) :
    username = request.POST.get('username')
    formPassword = request.POST.get('password')
    if not username and not formPassword :
        return redirect('login')
    else : 
        userDetails = User.objects.get(username=username)
        if not userDetails :
            return redirect('login')
        dbPassword = userDetails.password
        print(dbPassword)
        if dbPassword==formPassword :
            request.session['userID']=userDetails.id
            return redirect('projects')
        else :
            return redirect('login')

'''
signUp checks for user-login status using session
and directs to projects page else redirects to signup page 
'''
def signup(request) :
    if request.session.has_key('userID') :
        return redirect('projects')
    else :
       return render(request,'signup.html')

'''
signUpHandler gets user credentials from signup page, stores in the DB 
and directs to projects page else redirects to signup page
'''
def signUpHandler(request) :
    email = request.POST.get('email')
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex,email) :
        return redirect('signUp')
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1!=password2 :
         return redirect('signup')
    user = User(username=username,email=email,password=password1)
    user.save()
    request.session['userID'] = user.id
    return redirect('projects')

'''
projects checks for user-login status and directs to projects page
along with projects of the coresponding user else redirects to login page
'''
def projects(request) :
    if request.session.has_key('userID'):
      userID = request.session['userID']
      projectList = Project.objects.all().filter(userID=userID)
      return render(request,'projects.html',{'projectList' : projectList})
    else :
        return redirect('login')

'''
createProjects directs the user to addproject page
'''
def createProject(request) :
    if request.session.has_key('userID') :
        return render(request,'addProject.html')
    else :
        return redirect('login')

'''
createProjectHandler checks for user-login status,stores the project details in DB
and directs to projects page
'''
def createProjectHandler(request) : 
    if request.session.has_key('userID') :
        userID = request.session['userID']
        name = request.POST.get('name')
        description = request.POST.get('description')
        project = Project(userID=userID,name=name,description=description,createdOn=timezone.now())
        project.save()
        return redirect('projects')

'''
deleteProject checks for user-login status and deletes the project details using project id
'''
def deleteProject(request,id) :
    if request.session.has_key('userID') :
        Project.objects.get(id=id).delete()
        return redirect('projects')
    else :
        return redirect('login')

'''
editProject checks for user-login status and directs to editProject page along with project id
else redirects to login page
'''
def editProject(request,id) :
    if request.session.has_key('userID') : 
        project = Project.objects.get(id=id)
        return render(request,'editProject.html',{'project' : project})
    else :
        return redirect('login')

'''
editProjectHandler checks for user-login status and updates the project details using project id
else redirects to login page
'''
def editProjectHandler(request) :
    if request.session.has_key('userID') : 
        name = request.POST.get('name')
        description = request.POST.get('description')
        project_id = request.POST.get('project_id')
        Project.objects.filter(id=project_id).update(name=name,description=description)
        return redirect('projects')
    else :
        return redirect('login')

def logout(request) : 
    try:
        del request.session['userID']
    except KeyError:
        pass
    return redirect('login')
