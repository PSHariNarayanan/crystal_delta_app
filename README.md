# crystal_delta_app
Project Structure :

CRUD_project/                  
├── CRUD_project/             
│   ├── __init__.py
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
│   └── asgi.py
├── CRUD/
│   └── __init__.py
│	├── admin.py
│	├── apps.py
│	└── models.py
│	└── tests.py
│	├── urls.py
│	└── views.py
│   └── migrations/
│	├── static/
│	│	└──main.css
│	├── templates/
│			└──base.html
│			└──login.html
│			└──signup.html
│			└──projects.html
│			└──addProject.html
│			└──editProject.html
│
├── manage.py
├── db.sqlite3

Flow :

-http://127.0.0.1:8000/ --Directs you to Home Page

-Home Page redirects either to Login or Signup Page
-Signup Page registers a user and directs to the Projects Page
-Login Page directs the registered  after validation against DB, to the Projects Page 
-Projects Page has functionalities for CRUD operations
-Logout Page ends a user's session and redirects to Login Page
