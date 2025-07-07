from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template import loader

from .models import Todo

def index(request):
    if request.method == "POST":
        if "todo-id" in request.POST:
            todo_id = request.POST.get("todo-id")
            todo = Todo.objects.get(pk=todo_id)
            todo.is_checked = not todo.is_checked
            todo.save()
            return redirect("index")        
        todo_label = request.POST.get("new-todo")
        if todo_label:
            Todo.objects.create(todo_label=todo_label)
            return redirect("index") 
        
    todos_list = Todo.objects.all()
    template = loader.get_template("todos/index.html")
    context = { "todos_list": todos_list }
    return HttpResponse(template.render(context, request))

# OR
# def index(request):
#     todos_list = Todos.objects.all()
#     context = { "todos_list": todos_list }
#     return render(request, "todos/index.html", context)

def details(request, todo_id):  
      try:
           todo = Todo.objects.get(pk=todo_id)
      except Todo.DoesNotExist:
          raise Http404("todo does not exist")      
      return render(request, "todos/details.html", {todo: todo})