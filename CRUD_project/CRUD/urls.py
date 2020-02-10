from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('loginHandler/', views.loginHandler, name = 'loginHandler'),
    path('signup/', views.signup, name = 'signup'),
    path('signUpHandler/', views.signUpHandler, name = 'signUpHandler'),
    path('projects/', views.projects, name = 'projects'),
    path('createProject/', views.createProject, name = 'createProject'),
    path('createProjectHandler/',views.createProjectHandler, name = 'createProjectHandler'),
    path('deleteProject/<int:id>', views.deleteProject, name = 'deleteProject'),
    path('editProject/<int:id>', views.editProject, name = 'editProject'),
    path('editProjectHandler/', views.editProjectHandler, name = 'editProjectHandler'),
    path('logout/', views.logout, name = 'logout')
]