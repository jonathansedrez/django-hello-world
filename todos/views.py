from django.http import HttpResponse
from django.template import loader

from .models import Todo

# Create your views here.
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