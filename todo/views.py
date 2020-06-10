from django.shortcuts import render

from .models import Image, Todo


def home(request):
    count_all = Todo.objects.all().count()
    not_complete = Todo.objects.filter(completed=False).count()
    complete = Todo.objects.filter(completed=True).count()
    tasks = Todo.objects.all()
    context = {
        "tasks": tasks,
        "count_all": count_all,
        "complete": complete,
        "not_complete": not_complete,
    }
    return render(request, 'todo/home.html', context)
