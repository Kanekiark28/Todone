from django.shortcuts import render,redirect
from .models import TodoList,Category

def index(request):
    todos = TodoList.objects.all() #query all todos with the object manager

    categories = Category.objects.all() #query all the categories with the object manager

    if request.method=="POST": #if a request has been made to add a todo
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + "--" + date + " " + category
            Todo = TodoList(title=title,content=content,due_date=date,category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/")

        if "taskDelete" in request.POST: 
            if 








# Create your views here.
