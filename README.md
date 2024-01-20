# todoList
This is a simple todo list app in django.Here only can add tasks and display the tasks

**Step 1**: Install Django
If you haven't installed Django yet, you can install it using pip: pip install django

**Step 2**: Create a Django Project
In your terminal or command prompt, navigate to the directory where you want to create your Django project and run: django-admin startproject TODOLIST

**Step 3**: Navigate to the Project Directory
Change into the project directory: cd TODOLIST

**Step 4:** Create a Django App
Inside your project, create a Django app. Apps are components that serve specific purposes within a project.
python manage.py startapp home

**Step 5:** Define a Model
In your app directory (home), open the models.py file and define a simple model. For example:

# myapp/models.py
from django.db import models

class task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

**Step 6** : Make Migrations
Run the following commands to create database migrations based on your model:python manage.py makemigrations
This command generates migration files based on the changes to your models.:python manage.py migrate

**Step 7**: Create an Admin User (Optional)
You can create an admin user to manage your Django project. Run: python manage.py createsuperuser

**Step 8:** Run the Development Server
Start the development server to see your Django project in action: python manage.py runserver

Visit http://localhost:8000/ in your web browser. You should see the default Django welcome page.

**Step 9**: Access the Admin Interface
If you created an admin user, you can access the admin interface at http://localhost:8000/admin/. Log in using the admin credentials you created.

