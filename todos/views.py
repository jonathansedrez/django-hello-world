from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Todo

def index(request):
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